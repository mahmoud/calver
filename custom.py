# user customization
#
# chert_pre_render validates uploads/timeline.json and inlines it into
# entries/timeline.md so the rendered page is self-contained. Note that
# chert swallows exceptions raised inside hooks, so errors are surfaced by
# printing to stderr and injecting a visible error block instead of raising.
import json
import re
import sys
from pathlib import Path

TIMELINE_ENTRY_ROOT = 'timeline'
TIMELINE_MARKER = '<!-- timeline-data -->'
TIMELINE_JSON = Path('uploads') / 'timeline.json'
_DATE_RE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')
_EVENT_KEYS = ('date', 'title', 'detail', 'kind', 'url')


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
