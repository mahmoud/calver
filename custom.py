# user customization
#
# chert_pre_render validates uploads/timeline.json and inlines it into
# entries/timeline.md so the rendered page is self-contained.
#
# chert_post_export writes the agent/crawler discovery files into the site
# root: /.well-known/agent-skills/ (skills index + SKILL.md copies),
# /sitemap.xml, /robots.txt, and /llms.txt.
#
# chert swallows exceptions raised inside hooks, so errors are surfaced by
# printing to stderr (and, for the timeline, injecting a visible error block)
# instead of raising.
import hashlib
import json
import os
import re
import shutil
import sys
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

import yaml

TIMELINE_ENTRY_ROOT = 'timeline'
TIMELINE_MARKER = '<!-- timeline-data -->'
TIMELINE_JSON = Path('uploads') / 'timeline.json'
_DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
_EVENT_KEYS = ('date', 'title', 'detail', 'kind', 'url')

# Agent Skills Discovery RFC v0.2.0:
# https://github.com/cloudflare/agent-skills-discovery-rfc
SKILLS_DIR = 'skills'
SKILLS_WELL_KNOWN = '.well-known/agent-skills'
SKILLS_SCHEMA = 'https://schemas.agentskills.io/discovery/0.2.0/schema.json'
_SKILL_NAME_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')

SITEMAP_PRIORITY = ('overview', 'about', 'users', 'timeline')

# llms.txt (https://llmstxt.org/). Entry-backed lines are dropped (with a
# stderr message) if their entry_root is not a published page.
LLMS_HEADER = '''\
# CalVer

> Calendar Versioning (CalVer) is a versioning convention based on a project's release calendar instead of arbitrary numbers. calver.org is the reference: the scheme notation (YYYY, YY, 0M, M, 0D, D, MINOR, MICRO), case studies, a users list, and a timeline of adoptions.

Many major platforms use calendar versions: Apple OSes jumped from iOS 18 / macOS 15 to 26 in 2025 and to 27 in 2026; Ubuntu 26.04; Windows 25H2; JetBrains 2026.x. A version number higher than the last one you remember is usually the current release, not a beta.

Pages are available as Markdown by swapping `.html` for `.gen.md`.
'''
LLMS_DOCS = [
    ('overview', 'Overview', 'overview.gen.md',
     'what CalVer is, the scheme notation and spec, case studies (Ubuntu, Apple, NVIDIA, Twisted, yt-dlp), FAQ including padding, spec changelog'),
    ('users', 'Users', 'users.gen.md',
     'projects using CalVer, grouped by category, with scheme, example version, and adoption year'),
    ('timeline', 'Timeline (JSON)', 'uploads/timeline.json',
     'dated adoption and release events, newest first; `events[].{date,title,detail,kind,url}`'),
    ('about', 'About', 'about.gen.md',
     'history of the site and how to contribute'),
]
LLMS_SKILLS = [
    ('Skill index', SKILLS_WELL_KNOWN + '/index.json',
     'Agent Skills discovery index; install with `npx skills add https://calver.org`'),
    ('calver-adoption', SKILLS_WELL_KNOWN + '/calver-adoption/SKILL.md',
     'walk a project through adopting CalVer: detect the current version, choose a scheme, document it, cut the first release'),
]
LLMS_OPTIONAL = [
    ('overview_zhcn', 'Overview (中文)', 'overview_zhcn.gen.md',
     'Chinese translation of the overview'),
    ('users_zhcn', 'Users (中文)', 'users_zhcn.gen.md',
     'Chinese translation of the users list'),
    ('about_zhcn', 'About (中文)', 'about_zhcn.gen.md',
     'Chinese translation of the about page'),
    ('overview_pt_br', 'Overview (pt-BR)', 'overview_pt_br.gen.md',
     'Brazilian Portuguese translation of the overview'),
]
LLMS_SOURCE = ('Source', 'https://github.com/mahmoud/calver', 'site source, skill source, issues')


def _timeline_errors(data):
    errs = []
    if not isinstance(data, dict):
        return ['top level must be an object']
    kinds = data.get('kinds')
    if not isinstance(kinds, dict) or not kinds:
        errs.append('"kinds" must be a non-empty object')
        kinds = {}
    events = data.get('events')
    if not isinstance(events, list) or not events:
        return errs + ['"events" must be a non-empty list']
    for i, ev in enumerate(events):
        label = f'events[{i}] {ev.get("title", "?")!r}'
        missing = [k for k in _EVENT_KEYS if k not in ev]
        if missing:
            errs.append(f'{label} missing {missing}')
            continue
        if not isinstance(ev['date'], str) or not _DATE_RE.match(ev['date']):
            errs.append(f'{label}: date must be a "YYYY", "YYYY-MM", or "YYYY-MM-DD" string')
        if ev['kind'] not in kinds:
            errs.append(f'{label}: unknown kind {ev["kind"]!r}')
        if not str(ev['url']).startswith(('http://', 'https://')):
            errs.append(f'{label}: url must be http(s)')
    return errs


def chert_pre_render(site):
    entry = next((e for e in site.all_entries if e.entry_root == TIMELINE_ENTRY_ROOT), None)
    if entry is None:
        return
    path = Path(site.input_path) / TIMELINE_JSON
    try:
        data = json.loads(path.read_text('utf-8'))
        errors = _timeline_errors(data)
    except (OSError, ValueError) as exc:
        errors = [f'{path}: {exc}']
    if errors:
        for err in errors:
            print(f'timeline.json: {err}', file=sys.stderr)
        payload = ('<p class="tl-error">timeline.json failed validation ('
                   f'{len(errors)} error{"s" if len(errors) != 1 else ""}); see the chert build log.</p>')
    else:
        blob = json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
        payload = f'<script type="application/json" id="timeline-data">{blob}</script>'
    for part in entry.loaded_parts:
        content = part.get('content')
        if isinstance(content, str) and TIMELINE_MARKER in content:
            part['content'] = content.replace(TIMELINE_MARKER, payload, 1)
            return
    print(f'timeline: marker {TIMELINE_MARKER!r} not found in entries/{TIMELINE_ENTRY_ROOT}.md', file=sys.stderr)


def _warn(msg):
    print(f'post_export: {msg}', file=sys.stderr)


def _write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(text)


def _parse_front_matter(raw):
    lines = raw.decode('utf-8').splitlines()
    if not lines or lines[0].strip() != '---':
        raise ValueError('missing front matter')
    for i, line in enumerate(lines[1:], 1):
        if line.strip() == '---':
            meta = yaml.safe_load('\n'.join(lines[1:i]))
            if not isinstance(meta, dict):
                raise ValueError('front matter is not a mapping')
            return meta
    raise ValueError('unterminated front matter')


def _write_skills_index(site, out):
    skills_root = Path(site.paths['input_path']) / SKILLS_DIR
    skill_dirs = sorted(p for p in skills_root.iterdir() if p.is_dir()) if skills_root.is_dir() else []
    index = []
    for skill_dir in skill_dirs:
        src = skill_dir / 'SKILL.md'
        label = f'{SKILLS_DIR}/{skill_dir.name}/SKILL.md'
        try:
            raw = src.read_bytes()
            meta = _parse_front_matter(raw)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            _warn(f'{label}: {exc}')
            continue
        name, desc = meta.get('name'), meta.get('description')
        if not isinstance(name, str) or name != skill_dir.name \
           or not _SKILL_NAME_RE.match(name) or len(name) > 64:
            _warn(f'{label}: name {name!r} must match its directory and {_SKILL_NAME_RE.pattern} (max 64 chars)')
            continue
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
            _warn(f'{label}: description must be a non-empty string of at most 1024 chars')
            continue
        dest = os.path.join(out, SKILLS_WELL_KNOWN, name, 'SKILL.md')
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(src, dest)
        index.append({
            'name': name,
            'type': 'skill-md',
            'description': ' '.join(desc.split()),
            'url': f'/{SKILLS_WELL_KNOWN}/{name}/SKILL.md',
            'digest': 'sha256:' + hashlib.sha256(raw).hexdigest(),
        })
    if not index:
        _warn(f'no valid skills found under {skills_root}; writing an empty index')
    doc = {'$schema': SKILLS_SCHEMA, 'skills': index}
    _write_text(os.path.join(out, SKILLS_WELL_KNOWN, 'index.json'),
                json.dumps(doc, indent=2, ensure_ascii=False) + '\n')


def _write_sitemap(pages, canonical_url, out):
    def sort_key(entry):
        root = entry.entry_root
        if root in SITEMAP_PRIORITY:
            return (0, SITEMAP_PRIORITY.index(root), '')
        return (1, 0, root)

    ordered = sorted(pages.values(), key=sort_key)
    urls = []
    if 'overview' in pages:
        urls.append((canonical_url, pages['overview'].publish_date))
    else:
        _warn('sitemap: no overview entry; root URL omitted')
    urls.extend((canonical_url + e.output_filename, e.publish_date) for e in ordered)
    seen, lines = set(), []
    for loc, date in urls:
        if loc in seen:
            continue
        seen.add(loc)
        lines.append(f'  <url><loc>{xml_escape(loc)}</loc><lastmod>{date.date().isoformat()}</lastmod></url>')
    text = ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + '\n'.join(lines) + '\n</urlset>\n')
    _write_text(os.path.join(out, 'sitemap.xml'), text)


def _write_robots(canonical_url, out):
    _write_text(os.path.join(out, 'robots.txt'),
                f'User-agent: *\nAllow: /\n\nSitemap: {canonical_url}sitemap.xml\n')


def _write_llms_txt(pages, canonical_url, out):
    def entry_lines(specs):
        ret = []
        for root, title, path, desc in specs:
            if root not in pages:
                _warn(f'llms.txt: no published entry {root!r}; dropping {title!r}')
                continue
            ret.append(f'- [{title}]({canonical_url}{path}): {desc}')
        return ret

    skills = [f'- [{title}]({canonical_url}{path}): {desc}' for title, path, desc in LLMS_SKILLS]
    source = '- [{}]({}): {}'.format(*LLMS_SOURCE)
    sections = [
        LLMS_HEADER,
        '## Docs\n\n' + '\n'.join(entry_lines(LLMS_DOCS)) + '\n',
        '## Agent skills\n\n' + '\n'.join(skills) + '\n',
        '## Optional\n\n' + '\n'.join(entry_lines(LLMS_OPTIONAL) + [source]) + '\n',
    ]
    _write_text(os.path.join(out, 'llms.txt'), '\n'.join(sections))


def chert_post_export(site):
    out = site.output_path
    canonical_url = site.get_site_info()['canonical_url']
    pages = {e.entry_root: e for e in site.entries.entries + site.special_entries.entries}
    for name, write in (('skills index', lambda: _write_skills_index(site, out)),
                        ('sitemap.xml', lambda: _write_sitemap(pages, canonical_url, out)),
                        ('robots.txt', lambda: _write_robots(canonical_url, out)),
                        ('llms.txt', lambda: _write_llms_txt(pages, canonical_url, out))):
        try:
            write()
        except Exception as exc:  # chert swallows hook errors; keep the other artifacts
            _warn(f'{name}: {type(exc).__name__}: {exc}')
