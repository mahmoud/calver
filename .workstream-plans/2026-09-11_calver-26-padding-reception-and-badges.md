# CalVer 26.0: unpadded-default reception + badge research

Date: 2026-09-11. Researcher: omp session 01a09396 (branch `calver-26`).
Question: will the 26.0 unpadded recommendation (`YYYY.M.D`) and the token
notation flip be well-received, and what happens to calver badges in the wild?

## Bottom line

1. **Unpadded-by-default is the safe call.** Every ecosystem with an opinion
   already enforces it: PEP 440 integer normalization strips padding on PyPI;
   SemVer forbids leading zeroes, so Cargo and Go modules reject padded
   versions outright. The big adopters (Home Assistant, pip, certifi, Black,
   JetBrains) are unpadded. Nobody found arguing *against* unpadded as a
   default; the padded camp (bumpver, RAPIDS/NGC, Ubuntu, ISO/container-tag
   contexts) pads for lexical string sorting, which 26.0's "when to pad"
   exception explicitly covers. That constituency is served, not snubbed.
2. **The notation flip matches expectations, it doesn't fight them.** In the
   2020 HN thread on calver.org, top comments called the old convention
   backwards: "I would have expected D to be short day ... and DD be zero
   padded" (wodenokoto); "DD being short day is just *wrong* by conventional
   usage" (chrismorgan). 26.0 adopts exactly what they expected, aligned with
   Java DateTimeFormatter/moment/day.js/ICU.
   https://news.ycombinator.com/item?id=21967879
3. **Badges in the wild: ~600 occurrences, none break, many go stale.**
   GitHub code search for `img.shields.io/badge/calver` finds 572 files.
   They are static shields images chosen by each project, so nothing renders
   differently; but the scheme *text* is pre-26.0 notation:
   - `YY.MM.MICRO`: 247 occurrences (old meaning: unpadded month; new
     notation reads it as padded) - the meaning-flip population.
   - `0M`/`0D`/`0Y` tokens: ~68 occurrences - notation 26.0 retires.
   - Already-valid-under-26.0 unpadded strings (`YYYY.M.D`, `YY.M.MICRO`,
     `YYYY.M.MICRO`...): ~32, incl. conda and mozilla projects.
   - Cute: labgrid already badges `YY.MINOR[.MICRO]` bracket notation.
   The pre-26.0 notation note on the site is the right and sufficient
   remedy; no outreach campaign needed.
4. **Decision (author Q&A this session): stay on shields.io static badges;
   no self-hosting.** Rationale: (a) precedent - conventionalcommits.org and
   psf/black both delegate to shields; semver.org and keepachangelog.com
   offer no badge at all; no versioning-spec site self-hosts; (b) risk -
   calver.org has had four TLS-cert expiries (issues #8, #14, #19, #23);
   self-hosted badge images would put site uptime inline in hundreds of
   READMEs. Static hosting *would* be technically trivial (badge-maker npm,
   shields' own lib, pre-rendered per scheme; or shields endpoint badges fed
   by static JSON), but it buys branding control at availability risk for a
   population shields already serves.
5. **Decision 2: add a copy-paste "Badges" section to overview.md.** Done
   this session (see Actions). 600+ copied badges prove people want the
   snippet; now the notation flip has a canonical landing spot.

## Evidence: padding friction (all URLs verified live)

- PEP 440 integer normalization: https://packaging.python.org/en/latest/specifications/version-specifiers/#integer-normalization
- SemVer item 2 "MUST NOT contain leading zeroes": https://semver.org/#spec-item-2
- setuptools-scm deprecating `normalize=False`/`NonNormalizedVersion`, the
  last escape hatch for padded calver in Python packaging (June 2026, open):
  https://github.com/pypa/setuptools-scm/issues/1409 (cites #1354 "CalVer
  padding cannot work due to PEP 440 integer normalization")
- release-it crashed on `YY.0M.MICRO` because `21.04.1` fails semver
  validation: https://github.com/release-it/release-it/issues/754
- grype false positive: security advisory wrote `2023.07.22`, certifi ships
  `2023.7.22`, string compare says different versions:
  https://github.com/anchore/grype/issues/1430
- certifi's own drift padded->unpadded (`2015.04.28` -> `2017.4.17`->today's
  `YYYY.M.D`): https://pypi.org/simple/certifi/
- bumpver README, the articulate pro-padding position (lexical sort), which
  itself marks `YYYY.0M.0D` "PEP440: no": https://github.com/mbarkhau/bumpver
- setuptools normalization by design since 2014 (dstufft):
  https://github.com/pypa/setuptools/issues/302
- Seth Larson on zero-prefix normalization quirks: https://sethmlarson.dev/pep-440
- Home Assistant unpadded `YYYY.M` since 2020.12, zero format controversy:
  https://www.home-assistant.io/blog/2020/12/13/release-202012/
- PEP 2026 discussion (rejected; padding never raised as a concern):
  https://discuss.python.org/t/pep-2026-calendar-versioning-for-python/55782
- Lobsters/Tomlinson calver-regret thread: complaint is missing semantics,
  not padding: https://lobste.rs/s/bzmpqk/sometimes_i_regret_using_calver

## Badge mechanics (for the record)

- Shields static badge: `img.shields.io/badge/calver-<SCHEME>-22bfda.svg`;
  dots pass through; literal dash doubled (`--`); brackets percent-encoded
  (`%5B`/`%5D`). Docs: https://shields.io/badges
- Shields endpoint badge accepts a *plain static JSON file* on any HTTPS
  host (`schemaVersion:1, label, message, color`): https://shields.io/badges/endpoint-badge
  Viable later if central restyling ever matters; adds a second point of
  failure per render, so skipped for now.
- badge-maker (npm, shields' official generator, MIT/Apache-2.0) can
  pre-render SVGs at build time if self-hosting is ever revisited:
  https://www.npmjs.com/package/badge-maker
- Optional future nicety, deliberately not pursued now: register a CalVer
  logo with simple-icons so badges can carry `logo=calver`
  (conventionalcommits.org pattern).

## Actions taken this session

- Added `# Badges` section to `entries/overview.md` (after Case studies,
  before FAQ): copy-paste markdown snippet in new notation, escaping rules,
  and a pre-26.0 badge decoding note linking `#scheme`. Verified rendered
  on the running chert dev server (heading, TOC anchor, code block, and
  `#scheme` target all present). Left uncommitted alongside the in-flight
  26.0 overview rewrite owned by the sibling session.
- This report.

## Handoff suggestions (optional, for the 26.0 implementer)

- The "To pad or not to pad?" FAQ could cite the grype/certifi advisory
  mismatch (anchore/grype#1430) as a one-sentence concrete harm, and
  setuptools-scm#1409 as evidence the padded escape hatch is closing.
- The plan's bumpver outreach item gains urgency: bumpver's README is the
  main pro-padding reference and uses `0M`-style tokens throughout; its
  `MM`/`DD`/`WW` invert meaning under 26.0.
