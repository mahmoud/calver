---
title: Calendar Versioning
entry_root: overview
publish_date: July 1, 2019
orig_publish_date: March 25, 2016
---

_CalVer is a versioning convention based on your project's release
calendar, instead of arbitrary numbers._

**Versioning gets better with time.**

For maintainers, versioning allows us to specify precise dependencies
within an ever-expanding ecosystem. For sellers and promoters, a
project's version is a dynamic part of a brand. For all of us,
versioning lets us reference the past while upgrading to the future.

Different projects use different systems for versioning, but common
practices have emerged. For instance, point-separated numbers (e.g.,
_3.1.4_) are all but given. Another common versioning pattern
incorporates a time-based element, usually part of the release date.

This date-based approach has come to be called Calendar Versioning, or
**CalVer** for short.

[TOC]

# Scheme

There are multiple calendar versioning schemes, long used by projects
big and small. Rather than declaring a single scheme to be CalVer,
it's important to recognize the practicality of each and
[design the scheme][designing_a_version] to fit the project. First,
the parts of the version:

- **Major** - The first number in the version. 2 and 3 are Python's famous
  major versions. The major segment is the most common calendar-based component.
- **Minor** - The second number in the version. The 7 in Python 2.7 is
  its minor version.
- **Micro** - The third and usually final number in the version. Sometimes
  referred to as the "patch" segment.
- **Modifier** - An optional text tag, such as "dev", "alpha", "beta",
  "rc1", and so on.

The vast majority of modern version identifiers are composed of two or
three numeric segments, plus the optional modifier. Convention
suggests that four-numeric-segment versions are discouraged.

[designing_a_version]: https://sedimental.org/designing_a_version.html

As seen in the [case studies](#case-studies) below, projects have
found more than one useful way to leverage dates in their
versions. Rather than choose a single scheme, CalVer introduces
standard terminology for developers, in addition to the "semantic"
versions:

- **`YYYY`** - Full year - 2006, 2016, 2106
- **`YY`** - Two-digit year, zero-padded - 06, 16 (as in 16.04)
- **`Y`** - Short year, unpadded - 6, 16, 106
- **`MM`** - Zero-padded month - 01, 02 ... 11, 12
- **`M`** - Short month - 1, 2 ... 11, 12
- **`WW`** - Zero-padded week (since start of year) - 01, 02, 33, 52
- **`W`** - Short week - 1, 2, 33, 52
- **`DD`** - Zero-padded day - 01, 02 ... 30, 31
- **`D`** - Short day - 1, 2 ... 30, 31

A few real versions, decomposed:

- `2026.9.11` is **`YYYY.M.D`** (certifi's scheme)
- `26.04` is **`YY.MM`** (Ubuntu)
- `2026.2` is **`YYYY.MINOR`** (JetBrains, Kali Linux)
- `2026.08.19` is **`YYYY.MM.DD`** (yt-dlp)

Doubled letters are zero-padded and single letters are not, the same
repeat-count convention used by the [date-formatting
libraries][dayjs_format] most developers already know: Java's
DateTimeFormatter, moment.js, day.js, and ICU.

Note that traditional, incremented version numbers are 0-based,
whereas date segments are 1-based, and the short years are relative
to the year 2000. `Y` is a technicality: `Y` and `YY` only produce
different strings for the years 2000-2009 and 2100 onward. Ubuntu's
first release, 4.10 (October 2004), is the one well-known unpadded
year; in practice, projects write `YY`.

Trailing optional segments are written in square brackets, so
`YYYY.MM.DD[.MICRO]` is a date version that sometimes carries a
fourth number, as yt-dlp's does.

Weeks deserve caution. There are several definitions in common use
(`strftime`'s `%W` counts Monday-started weeks from 00, `%U` does the
same from Sunday, and ISO 8601's `%V` runs 01 through 53 with its own
week-based year), and depending on the definition a year can have as
many as 54 numbered weeks. A project using weeks should state which
definition it means. Usage of weeks is mutually exclusive with months
and days.

> **Pre-26.0 notation.** Before spec 26.0, this site wrote padded
> tokens with a zero prefix (`0Y`, `0M`, `0W`, `0D`) and used `YY`,
> `MM`, `WW`, and `DD` for the *unpadded* forms. The old `YYYY.0M.0D`
> reads as `YYYY.MM.DD` today, and the old `YY.MM` reads as `YY.M`.
> See the [spec changelog](#spec-changelog).

The [Gregorian calendar][gregorian] is assumed, as is the convention
of [UTC][utc]. Technically any calendar can be used, provided projects
state which one.

[dayjs_format]: https://day.js.org/docs/en/display/format
[gregorian]: https://en.wikipedia.org/wiki/Gregorian_calendar
[utc]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time

## Padding

Unpadded is the sensible default: `YYYY.M.D`, not `YYYY.MM.DD`. The
version comparators that matter treat `04` and `4` as the same
number. dpkg and rpm compare numerically, and [PEP 440 normalizes
leading zeros away][pep440_norm], so PyPI shows `2025.4` no matter
what you tagged. Padding buys nothing there, and it costs something
elsewhere: a padded segment is invalid [SemVer][semver] ("MUST NOT
contain leading zeroes"), which Cargo and Go modules reject outright.
NVIDIA's GPU Operator [says it plainly][nvidia_lifecycle]: "Zero
padding is omitted for month to be still compatible with semantic
versioning."

Padding earns its keep in one place: string sorting. When versions
live in filenames, image tags, or object-store keys that get listed
by `ls` or sorted lexically, fixed-width segments keep `26.04` ahead
of `26.10`. That is why Ubuntu, NixOS, the Arch Linux ISOs, and
NVIDIA's monthly NGC containers pad, and it is fine that they do. Pad
when your versions are sorted as strings; otherwise, don't.

[pep440_norm]: https://packaging.python.org/en/latest/specifications/version-specifiers/#integer-normalization
[semver]: https://semver.org/
[nvidia_lifecycle]: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/life-cycle-policy.html

# Case studies

CalVer has quite a few users. These are projects selected for their
notability and variety of use cases.

## Ubuntu

<img src="https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg" />

**[Ubuntu][ubuntu]**, one of the most prominent Linux-based operating
systems available, uses a three-segment CalVer scheme, with a short
year and zero-padded month. It has done so
[from the very start][ubuntu_releases], in October 2004, making 4.10
the first general release of Ubuntu.

Even a simple operating system involves many, many parts, making it
difficult to communicate much meaning with an arbitrary number. By
dating the project release, the calendar-based version is much more
than an arbitrary number, communicating useful information that is
rooted in simple fact.

Ubuntu derives additional benefit from its CalVer scheme, by
integrating it with their support schedule. Ubuntu currently has
five-year support periods for their long-term support (LTS) releases,
and only 9 months for non-LTS releases. Thanks to CalVer and
elementary arithmetic, any user can easily determine whether their
version is still supported. The current LTS release at the time of
writing, [26.04 LTS][ubuntu_cycle], will be supported until 2031.

[ubuntu]: https://ubuntu.com/
[ubuntu_releases]: https://en.wikipedia.org/wiki/List_of_Ubuntu_releases
[ubuntu_cycle]: https://ubuntu.com/about/release-cycle

## Apple

<img src="https://img.shields.io/badge/calver-YY.MINOR-22bfda.svg" />

At WWDC in June 2025, **[Apple][apple_ios26]** moved every one of its
operating systems to a single year-based number: iOS 18 became iOS
26, macOS 15 became macOS 26, and iPadOS, watchOS, tvOS, and visionOS
made the same jump, with Xcode 26 and Safari 26 following. The
releases shipped in September 2025 but carry the number of the year
ahead, the way car model years do. WWDC 2026 [confirmed the pattern
is annual][apple_wwdc26], with the 27 family.

In CalVer terms the scheme is `YY.MINOR` with the year offset by one:
the calendar supplies the major version, point releases count up
underneath it, and the rounding is marketing-friendly rather than
strictly literal. The payoff is the one Ubuntu found twenty years
earlier. A single number now tells a customer, a developer, or a
support engineer how current any Apple platform is, and the numbers
line up across platforms instead of drifting (iOS 18 beside macOS 15
beside watchOS 11 took a lookup table). Measured by devices, it is
likely the largest calendar versioning adoption to date.

[apple_ios26]: https://www.apple.com/newsroom/2025/06/apple-elevates-the-iphone-experience-with-ios-26/
[apple_wwdc26]: https://www.apple.com/newsroom/2026/06/apple-unveils-next-generation-of-apple-intelligence-siri-ai-and-more/

## NVIDIA

<img src="https://img.shields.io/badge/calver-YY.M.MICRO-22bfda.svg" />

**NVIDIA** runs calendar versions across much of its infrastructure
software, and its documentation is unusually explicit about why. The
[GPU Operator][nvidia_lifecycle] for Kubernetes went from SemVer 1.11
to 22.9.0 in September 2022, with a new major every six months and a
twelve-month support window, so the version alone tells an operator
when support ends. [RAPIDS][rapids_calver], the CUDA data science
libraries, jumped from 0.19 to 21.06.00 in June 2021. The [NGC
deep-learning containers][ngc_notes] (PyTorch, TensorFlow, TensorRT,
Triton) have shipped monthly as `YY.MM` since at least 19.08.
[Legate][legate_versions] uses `YY.MM.PP` with `.devXXX` weeklies and
promises API and ABI stability within each month version.

The instructive wrinkle is that one company uses both padding
styles. GPU Operator is unpadded, and says so: "Zero padding is
omitted for month to be still compatible with semantic versioning."
RAPIDS, NGC, and Legate pad, because their versions are container
tags that sort as strings. Each chose correctly for its own artifact
(see [Padding](#padding)).

[rapids_calver]: https://docs.rapids.ai/notices/rgn0013/
[ngc_notes]: https://docs.nvidia.com/deeplearning/frameworks/container-release-notes/index.html
[legate_versions]: https://docs.nvidia.com/legate/latest/versions.html

## Twisted

<img src="https://img.shields.io/badge/calver-YY.M.MICRO-22bfda.svg" />

**[Twisted][twisted]**, the venerated Python networking and
asynchronous execution framework, uses a three-segment CalVer scheme,
with a short year in the major version slot, short month in the minor
version slot, and micro/patch version in the third and final slot.

First released in 2002 and still actively developed today (26.4.0 at
the time of writing), Twisted is a [mature][twisted_wp] library that
has grown to match its large scope. It features everything from an
IRC client to an HTTP server to a slew of utilities for concurrent
programming. Like an operating system, Twisted has a lot of parts,
making SemVer a poor fit due to the individual parts deprecating and
breaking compatibility individually.

The non-deprecated parts of Twisted are backwards-compatible between
each successive version, and breaking changes are done on a time basis,
where one year must pass and two releases issued between the release
deprecating the functionality and the removal of the functionality.

Its versioning scheme has spread to related projects, including
[Klein][klein], [Treq][treq], and even one of Twisted's dependencies,
[PyOpenSSL][pyopenssl].

[twisted]: https://twisted.org/
[twisted_wp]: https://en.wikipedia.org/wiki/Twisted_%28software%29
[klein]: https://github.com/twisted/klein
[treq]: https://github.com/twisted/treq
[pyopenssl]: https://github.com/pyca/pyopenssl

## yt-dlp

<img src="https://img.shields.io/badge/calver-YYYY.MM.DD%5B.MICRO%5D-22bfda.svg" />

**[yt-dlp][yt-dlp]**, the community successor to youtube-dl, is the
understated ally of Internet media archivists everywhere. youtube-dl
pioneered the scheme, a full date with a micro segment appended when
a same-day fix is needed, and has been dormant since 2021.12.17;
yt-dlp forked in January 2021 and inherited the scheme unchanged,
tagging [2026.08.19][ytdlp_release] in the usual style.

Despite the name, yt-dlp's scope is expansive. It supports extracting
audio and video from a long, ever-expanding list of sites. Consider
the rapid release cycle of supported services, and it becomes clear
why the project has adopted CalVer to such a great degree.

The tags are zero-padded, but PyPI lists the same release as
`2026.8.19`, the [PEP 440][pep440_norm]-normalized form. It is a live
illustration of the [padding note](#padding) above: the two strings
are one version.

[yt-dlp]: https://github.com/yt-dlp/yt-dlp
[ytdlp_release]: https://github.com/yt-dlp/yt-dlp/releases/tag/2026.08.19

## The IANA/Olson timezone database

<img src="https://img.shields.io/badge/calver-YYYYa..z-22bfda.svg" />

The [IANA/Olson timezone database][iana_tz] represents the history of local
time for many representative locations around the globe, and is the source
of truth for essentially every operating system, database, website, or other
computer that deals with timezones or daylight savings time.

It is updated periodically to reflect changes made by political bodies to
time zone boundaries, UTC offsets, and daylight-saving rules.  Because these
changes follow political and legislative whim rather than a fixed schedule,
the database is [versioned][tz_version] with a four-digit year followed by
lower-case letter (a through z, then za through zz, then zza through zzz,
and so on).  Calendar versioning offers a date-stamped snapshot of an
otherwise chaotic system.

[iana_tz]: https://www.iana.org/time-zones
[tz_version]: https://data.iana.org/time-zones/tz-link.html

## Other notable projects

- [boltons][boltons] - **`YY.MINOR.MICRO`** - A broad library of
  utilities supplementing the Python standard library.
- [certifi][certifi] - **`YYYY.M.D`** - certifi is a wrapper around
  Mozilla's certificate authority bundle, used for secure Internet
  communication. Similar to [the IANA timezone database](#the-iana-olson-timezone-database),
  certificate updates do not follow a fixed schedule, but timely,
  dateable updates are critical to security.
- [CockroachDB][cockroachdb] - **`YY.MINOR.MICRO`** - Distributed SQL
  database, on CalVer since 19.1.
- [fusefs-ntfs][fusefs-ntfs] - **`YYYY.M.D_MICRO`** - One of the
  earliest and most cross-compatible NTFS access layers for Unix
  systems.
- [Home Assistant][ha] - **`YYYY.M.MICRO`** - Open-source home
  automation platform, released monthly since 2020.12.
- [JetBrains IDEs][jetbrains] - **`YYYY.MINOR.MICRO`** - IntelliJ
  IDEA, PyCharm, and the rest of the family, since 2016.1.
- [LibreOffice][libreoffice] - **`YY.M`** - free and powerful office suite,
  and a successor to OpenOffice.org (commonly known as OpenOffice).
- [OpenSCAD][openscad] - **`YYYY.MM`** - The premiere open-source
  offering for solid 3D CAD modelling.
- [pip][pip] - **`YY.MINOR.MICRO`** - Official package manager for Python.
- [Stripe's API][stripe] - **`YYYY-MM-DD.MODIFIER`** - An API-first
  payments platform. Integrations pin a dated API version; since 2024
  the twice-yearly breaking releases carry a plant name, as in
  `2024-09-30.acacia`.

[boltons]: https://boltons.readthedocs.io/en/latest/
[certifi]: https://pypi.org/project/certifi/
[cockroachdb]: https://www.cockroachlabs.com/blog/calendar-versioning/
[fusefs-ntfs]: https://www.freshports.org/sysutils/fusefs-ntfs
[ha]: https://www.home-assistant.io/blog/2020/12/13/release-202012/
[jetbrains]: https://www.jetbrains.com/idea/whatsnew/
[libreoffice]: https://www.libreoffice.org/
[openscad]: https://openscad.org/
[pip]: https://pip.pypa.io/en/stable/news/
[stripe]: https://stripe.com/blog/introducing-stripes-new-api-release-process

See the [Users page][users] for a growing list of CalVer users.

[users]: /users.html

# When to use CalVer

If both you and people you don't know use your project seriously, then
use a serious version. Luckily, the decision on whether to use CalVer
for that version is easier than ever:

- Does your project feature a large or constantly-changing scope?
  - Large systems and frameworks, like [Ubuntu](#ubuntu) and [Twisted](#twisted).
  - Amorphous sets of utilities, like [Boltons](#other-notable-projects).
- Is your project time-sensitive in any way? Do other external changes
  drive new project releases?
  - Business requirements, such as [Ubuntu](#ubuntu)'s focus on support schedules.
  - Security updates, such as [certifi](#other-notable-projects)'s need to update certificates.
  - Political shifts, such as [the IANA database](#the-iana-olson-timezone-database)'s handling of timezone changes.

If you answered yes to any of these questions, CalVer's semantics make
it a strong choice for your project.

# FAQ

## What about breaking changes?

CalVer does not encode API breaks in the number, and that is
deliberate. There is no consensus on what counts as a breaking change
(is a new field breaking? a reworded error?), so a version bump that
claims to carry that meaning [substitutes for the documentation and
communication that actually keep dependents working][designing_a_version].
Pair a calendar version with a time-based deprecation policy and say
it out loud: Twisted requires one year and two releases between
deprecating something and removing it. For a rewrite large enough
that the policy can't cover it, rename the project. Further
discussion in [#4][issue_4].

## Multiple releases per day?

Append an incrementing micro segment: `2026.9.11`, then `2026.9.11.1`,
written `YYYY.M.D[.MICRO]` in scheme notation. Avoid intra-day
timestamps; they trade a readable number for one that either runs
out of resolution (two releases in the same minute) or grows too
long, and humans don't convert a second-counter to a wall clock in
their heads. If an automated pipeline genuinely needs the timestamp,
build metadata (`+HHMMSS`) carries it without affecting precedence.
Further discussion in [#49][issue_49] and [#62][issue_62].

## Padded or unpadded?

Unpadded, unless your versions are sorted as strings (filenames,
image tags, object-store keys). See [Padding](#padding) for the
reasoning and the exceptions.

[issue_4]: https://github.com/mahmoud/calver/issues/4
[issue_49]: https://github.com/mahmoud/calver/issues/49
[issue_62]: https://github.com/mahmoud/calver/issues/62
