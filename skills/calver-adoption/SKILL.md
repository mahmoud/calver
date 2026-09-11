---
name: calver-adoption
description: >-
  Walk a project through adopting Calendar Versioning (CalVer): detect the
  current version, choose a scheme, document it with a link to calver.org,
  and cut the first calver release. Use when asked to "adopt calver",
  "switch to calendar versioning", "use date-based versions", or when the
  user cites calver.org and wants it applied to their project.
version: "26.0"
---

# calver-adoption

Take a project from whatever version it has today to its first calendar
version, with the scheme documented and the release cut. Five steps, in
order. Steps 1 through 4 are always done; step 5 is offered and only
executed on request.

Vocabulary: schemes are written in [calver.org 26.0
notation](https://calver.org/#scheme). Single letters are unpadded (`M`,
`D`, `W`), doubled letters are zero-padded (`MM`, `DD`, `WW`), `YYYY` is
the full year and `YY` the two-digit year. `MINOR` and `MICRO` are
ordinary counters. Optional trailing segments go in square brackets:
`YYYY.M.D[.MICRO]`.

## 1. Detect the current version (before asking anything)

Check these sources in order and record every one that yields a value:

1. `git tag --sort=-v:refname | head -5`
2. `package.json` → `.version`
3. `pyproject.toml` → `[project].version`, then `[tool.poetry].version`
4. `Cargo.toml` → `[package].version`
5. `setup.cfg` (`[metadata] version`) or `setup.py` (`version=`)
6. A source file exporting `__version__` or `VERSION`
7. `CHANGELOG.md` / `CHANGES.md` / `NEWS` headings
8. GitHub releases (`gh release list --limit 5`, if `gh` is available)

Multiple sources disagreeing: the highest *published* version (a tag or
release) wins, and the drift is reported to the user, since every source
gets rewritten in step 5. Also note the tag style (`v1.4.2` vs `1.4.2`);
step 5 must match it.

Nothing found: ask one question, "What's the current version, or has this
project not been released yet?" An unreleased project skips every
migration concern below; its first release simply uses the chosen scheme's
value for the planned release date.

## 2. Ask about time commitments (one question)

"Do you have support schedules, deprecation windows, LTS cadence, or
compliance deadlines that the versioning docs should state?"

Default answer is "none", and most projects say so. If there is
something, capture the window lengths for the step 4 paragraph. Two
exemplars of what a good answer turns into:

- Ubuntu: each release supported N months; LTS every two years, five
  years of support.
- NVIDIA GPU Operator: a new major every six months, twelve months of
  support, so end-of-life is readable off the version.

## 3. Choose a scheme

Present this table and recommend one row based on what step 1 revealed
about the project (library vs. application, release cadence, ecosystem).

| Scheme | Example | Flagship users | Fits |
|---|---|---|---|
| `YYYY.MINOR.MICRO` | 2026.2.0 | JetBrains, Kali, Spring Cloud | apps and platforms with a few releases a year |
| `YY.MINOR.MICRO` | 26.2.1 | pip, attrs, CockroachDB, Mesa | libraries that want a year signal plus a counter |
| `YYYY.M.MICRO` | 2026.9.0 | Home Assistant, Betaflight, mise | monthly-cadence projects; **default recommendation for packages** |
| `YY.M.MICRO` | 26.9.0 | Black, conda, Twisted | same, shorter |
| `YY.MM` | 26.04 | Ubuntu, NixOS, OpenWrt | date-named platform releases that need fixed-width sorting |
| `YYYY.M.D[.MICRO]` | 2026.9.11 | yt-dlp (padded variant), certifi | tools that release per date |

State the ecosystem constraints that apply, from
[calver.org's padding section](https://calver.org/#padding):

- **crates.io and Go modules** reject zero-padded segments (SemVer's
  "MUST NOT contain leading zeroes"). Go modules additionally cannot take
  a year as the major version without a `/v2026`-style import path
  suffix every year, so advise Go libraries against CalVer entirely.
- **PyPI** normalizes padding away (PEP 440): `2026.04` and `2026.4` are
  the same release, and PyPI displays the unpadded form. Pick unpadded.
- **npm** requires exactly three numeric segments: `YYYY.M.MICRO`
  publishes, bare `YYYY.M` does not.
- **Ordering**: the first calendar version must compare greater than the
  current version in the ecosystem's comparator. `2026.x > 4.x`
  numerically everywhere, so this almost always holds. If the current
  major is already large (a project on 3000.x, or already on a
  date-like number), flag it for manual review before proceeding.

Unpadded is the default; pad only when the versions are sorted as
strings (image tags, ISO filenames, object-store keys).

## 4. Document it

Ask where the versioning statement should live: a README "Versioning"
section (default), `CONTRIBUTING.md`, or a docs page. Insert this
paragraph, filled in:

> ## Versioning
>
> <Project> uses [Calendar Versioning](https://calver.org). Versions
> follow **`<SCHEME>`**; for example, `<EXAMPLE>` <one sentence naming
> each segment>. <If step 2 yielded commitments: "Each release is
> supported for <N> months." / "Deprecations are announced at least <N>
> releases before removal.">

Example of the filled sentence for `YYYY.M.MICRO`: "`2026.9.0` is the
first release of September 2026; the final number counts fixes within
that month."

## 5. Cut the first release (offer; execute only on request)

1. Compute the first calendar version from the planned release date and
   the chosen scheme. Append `.0` where the scheme has a `MICRO`
   segment.
2. Update **every** version source found in step 1, in sync. A stale
   `__version__` next to a new tag is the most common way this goes wrong.
3. Add a changelog entry that names the scheme change and links
   https://calver.org.
4. Commit.
5. `git tag` in the repo's existing style (`v` prefix or bare, per step
   1), then push the tag.
6. Publish with the ecosystem's command: `npm publish`, `uv build` then
   `uv publish` (or `twine upload`), `cargo publish`, `gh release create`.

Two cautions to state at the end:

- Verify the registry sorts the new version above the old one before
  announcing (`npm view <pkg> versions`, the PyPI release list, and so
  on).
- Never retro-tag old commits with calendar numbers. The scheme starts
  now; history keeps its old versions.

## Install

- Claude Code: symlink or copy this directory to
  `~/.claude/skills/calver-adoption`.
- Oh My Pi, Codex, and other agents using the Agent Skills layout:
  `~/.agents/skills/calver-adoption`. The skill's name and description
  are picked up automatically; no other configuration is needed.

## Self-update

This skill ships with calver.org and tracks its notation. If the scheme
table, the constraints, or the procedure drift from what
https://calver.org says, or a step fails on a real project, open an issue
or pull request at https://github.com/mahmoud/calver with the fix, bump
`version` to the spec version it now matches, and keep the file under
~200 lines.
