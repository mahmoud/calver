---
title: CalVer Users
entry_root: users
special: true
publish_date: September 11, 2026
orig_publish_date: March 29, 2018
---

Calendar versioning has a long history, and CalVer users can be found
in all areas. This ever-growing, never-complete list of project names
and example versions is [open to expansion][issues]. To keep it
useful, a listed project should be recognizable within its ecosystem
and have either a public adoption announcement or a sustained
calendar-versioned release history.

[issues]: https://github.com/mahmoud/calver/issues

[TOC]

Schemes are written in the notation from the [CalVer
overview][overview]: `M`, `D`, and `W` are unpadded; `0M`, `0D`, and
`0W` are zero-padded; `YY` is the short year and `0Y` the zero-padded
one. See the overview for detailed case studies.

[overview]: /overview.html

# Operating systems and platforms

Whole systems have many parts and long support windows, which is
where a date in the version pays off most.

Project                                   | Scheme                      | Example        | Since
----------------------------------------- | --------------------------- | -------------- | -----
[Apple][apple] (iOS, iPadOS, macOS, watchOS, tvOS, visionOS, Xcode, Safari) | `YY.MINOR` (model year) | macOS 26.5 | 2025
[Microsoft Windows][ms_win]               | `YY`/`YYYY`                 | 95, 98, 2000   | 1995
[Microsoft Windows 10 and 11][ms_win_rel] | `YY0M`, then `YYH1`/`YYH2`  | 1607, 20H2, 24H2 | 2015
[Ubuntu][ubuntu]                          | `YY.0M.MICRO`               | 26.04          | 2004
[Kali Linux][kali]                        | `YYYY.MINOR`                | 2026.2         | 2016
[OpenWrt][openwrt]                        | `YY.0M.MICRO`               | 25.12          | 2018
[NixOS][nixos]                            | `YY.0M`                     | 25.05          | 2013
[OPNsense][opnsense]                      | `YY.M.MICRO`                | 26.7.3         | 2015
[Arch Linux ISO][archlinux]               | `YYYY.0M.0D`                | 2026.09.01     | pre-2016
[GrapheneOS][grapheneos]                  | `YYYY0M0DNN`                | 2026091000     | long-standing
[Nura][nura] (formerly postmarketOS)      | `YY.0M`                     | 26.06          | ~2020
[Slack for Mobile][slack]                 | `YY.0M.MICRO`               | 26.09.20       | ~2018
[Tesla firmware][tesla_fw]                | `YYYY.W.MICRO`              | 2026.32.3      | ≤2019
[Rivian firmware][rivian_fw]              | `YYYY.0W.MICRO`             | 2026.31.40     | 2021

[apple]: /overview.html#apple
[ms_win]: https://en.wikipedia.org/wiki/Microsoft_Windows
[ms_win_rel]: https://learn.microsoft.com/en-us/windows/release-health/windows11-release-information
[ubuntu]: /overview.html#ubuntu
[kali]: https://www.kali.org/releases/
[openwrt]: https://openwrt.org/releases/start
[nixos]: https://nixos.org/blog/announcements/2025/nixos-2505/
[opnsense]: https://opnsense.org/blog/
[archlinux]: https://archlinux.org/releng/releases/
[grapheneos]: https://grapheneos.org/releases
[nura]: https://nura.eco/blog/
[slack]: https://apps.apple.com/us/app/slack/id618783545
[tesla_fw]: https://www.notateslaapp.com/software-updates/
[rivian_fw]: https://rivianroamer.com/software-updates

# Databases and infrastructure

Infrastructure software tends to publish support windows, and a
calendar version lets operators read the window off the number.

Project                                   | Scheme                  | Example           | Since
----------------------------------------- | ----------------------- | ----------------- | -----
[ClickHouse][clickhouse]                  | `YY.M.MICRO.BUILD`      | 26.8.2.7          | 2018
[CockroachDB][cockroachdb]                | `YY.MINOR.MICRO`        | 26.2.2            | 2019
[Neo4j][neo4j]                            | `YYYY.0M.MICRO`         | 2025.01.0         | 2025
[ScyllaDB][scylladb]                      | `YYYY.MINOR`            | 2025.1            | 2022
[OpenStack][openstack]                    | `YYYY.MINOR`            | 2026.1 "Gazpacho" | 2023
[Vertica][vertica]                        | `YY.QUARTER`            | 25.3              | 2023
[authentik][authentik]                    | `YYYY.M.MICRO`          | 2026.8            | ~2020
[NVIDIA GPU Operator][nvidia_gpu_op]      | `YY.M.MICRO`            | 22.9.0            | 2022
[NVIDIA RAPIDS][nvidia_rapids]            | `YY.0M.MICRO`           | 26.04             | 2021
[NVIDIA NGC containers][nvidia_ngc]       | `YY.0M`                 | 26.06             | ≤2019
[NVIDIA Legate][nvidia_legate]            | `YY.0M.MICRO[.devXXX]`  | 24.06             | 2021
[Spring Cloud][spring_cloud]              | `YYYY.MINOR.MICRO`      | 2025.1            | 2020
[FairCom][faircom]                        | `YY.M`                  | 26.10 (planned)   | 2026

See the [NVIDIA case study](/overview.html#nvidia) for how one company ended up with
both padding styles.

[clickhouse]: https://clickhouse.com/docs/whats-new/changelog
[cockroachdb]: https://www.cockroachlabs.com/blog/calendar-versioning/
[neo4j]: https://feedback.neo4j.com/changelog/important-update-calendar-versioning-cypher-25
[scylladb]: https://www.scylladb.com/2025/04/08/announcing-scylladb-2025-1/
[openstack]: https://releases.openstack.org/
[vertica]: https://www.rocketsoftware.com/en-us/insights/whats-new-in-vertica-23-3
[authentik]: https://docs.goauthentik.io/releases/2026.8/
[nvidia_gpu_op]: https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/life-cycle-policy.html
[nvidia_rapids]: https://docs.rapids.ai/notices/rgn0013/
[nvidia_ngc]: https://docs.nvidia.com/deeplearning/frameworks/container-release-notes/index.html
[nvidia_legate]: https://docs.nvidia.com/legate/latest/versions.html
[spring_cloud]: https://github.com/spring-cloud/spring-cloud-release/wiki/Supported-Versions
[faircom]: https://github.com/mahmoud/calver/issues/74

# Languages and standards

Programming language standards are conventionally named for their year
(`YY`/`YYYY`), and comprise some of the oldest notable usages of
calendar versioning.

Project                           | Scheme            | Example                     | Since
--------------------------------- | ----------------- | --------------------------- | -----
[Ada][ada]                        | `YY`/`YYYY`       | 83, 95, 2012                | 1983
[ALGOL][algol]                    | `YY`              | 58, 60, 68                  | 1958
[C][c]                            | `YY`              | 89, 99, 11                  | 1989
[C++][cpp]                        | `0Y`              | 98, 03, 11, 14, 17          | 1998
[Fortran][fortran]                | `YY`/`YYYY`       | 66, 77, 90, 95, 2003, 2008  | 1966
[ECMAScript][js] (aka JavaScript) | `YYYY`            | 2015, 2020                  | 2015
[Python manylinux][manylinux]     | `YYYY`            | 2010 ("backwards compatible to") | 2018

Python itself came close. [PEP 2026][pep2026] proposed calendar
versioning for CPython (3.26 in 2026, `3.YY`) in 2024. The Steering
Council rejected it in early 2025 on a close vote, citing ecosystem
churn rather than the idea itself.

[ada]: https://en.wikipedia.org/wiki/Ada_(programming_language)
[algol]: https://en.wikipedia.org/wiki/ALGOL_60
[c]: https://en.wikipedia.org/wiki/C_(programming_language)
[cpp]: https://en.wikipedia.org/wiki/C%2B%2B
[fortran]: https://en.wikipedia.org/wiki/Fortran
[manylinux]: https://www.python.org/dev/peps/pep-0571/
[js]: https://en.wikipedia.org/wiki/ECMAScript#Versions
[pep2026]: https://peps.python.org/pep-2026/

# Libraries

CalVer software libraries allow developers to evaluate their software
freshness with just a glance at the dependency list.

Project                         | Scheme              | Example      | Since
------------------------------- | ------------------- | ------------ | -----
[boltons][boltons]              | `YY.MINOR.MICRO`    | 26.2.0       | 2015
[Twisted][twisted]              | `YY.M.MICRO`        | 26.4.0       | pre-2016
[attrs][attrs]                  | `YY.MINOR.MICRO`    | 26.1.0       | 2021
[structlog][structlog]          | `YY.MINOR.MICRO`    | 26.1.0       | 2021
[certifi][certifi]              | `YYYY.0M.0D`        | 2026.07.22   | pre-2016
[tzdata][tzdata] and [pytz][pytz] | `YYYY.MINOR`      | 2026.3       | long-standing
[xarray][xarray]                | `YYYY.0M.MICRO`     | 2026.09.0    | 2022

[boltons]: https://boltons.readthedocs.io/en/latest/
[twisted]: /overview.html#twisted
[attrs]: https://www.attrs.org/en/stable/changelog.html
[structlog]: https://pypi.org/project/structlog/
[certifi]: https://pypi.org/project/certifi/
[tzdata]: https://pypi.org/project/tzdata/
[pytz]: https://pypi.org/project/pytz/
[xarray]: https://github.com/pydata/xarray/issues/6176

# Utilities and tools

Tools ship often and get installed everywhere, so the version people
report in bug reports should say how old it is.

Project                                   | Scheme              | Example        | Since
----------------------------------------- | ------------------- | -------------- | -----
[pip][pip]                                | `YY.MINOR.MICRO`    | 26.2.1         | 2018
[Black][black]                            | `YY.M.MICRO`        | 26.5.1         | 2018
[conda][conda]                            | `YY.M.MICRO`        | 26.7.2         | 2022
[Home Assistant][ha]                      | `YYYY.M.MICRO`      | 2026.9.2       | 2020
[yt-dlp][yt-dlp] (successor to youtube-dl) | `YYYY.0M.0D[.MICRO]` | 2026.08.19   | 2021
[pipenv][pipenv]                          | `YYYY.M.MICRO`      | 2026.8.0       | ~2022
[mise][mise]                              | `YYYY.M.MICRO`      | 2026.9.5       | ~2023
[Helix][helix]                            | `YY.0M.MICRO`       | 25.07.1        | 2022
[LibreOffice][libreoffice]                | `YY.M`              | 26.2           | 2024
[Mesa][mesa]                              | `YY.MINOR.MICRO`    | 26.2.3         | 2017
[KDE Gear][kde_gear]                      | `YY.0M.MICRO`       | 26.08.1        | ≤2020
[JetBrains IDEs][jetbrains]               | `YYYY.MINOR.MICRO`  | 2026.2         | 2016
[Android Studio][android_studio]          | `YYYY.MINOR.MICRO`  | 2026.1.4       | 2022
[MediaInfo][mediainfo]                    | `YY.0M`             | 26.05          | 2017
[Betaflight][betaflight]                  | `YYYY.M.MICRO`      | 2025.12.0      | 2025
[Minecraft snapshots][minecraft]          | `YYw0Wa`            | 22w42a         | long-standing

[pip]: https://pip.pypa.io/en/stable/news/
[black]: https://github.com/psf/black/releases
[conda]: https://github.com/conda/ceps/blob/main/cep-0008.md
[ha]: https://www.home-assistant.io/blog/2021/01/06/release-20211/
[yt-dlp]: /overview.html#yt-dlp
[pipenv]: https://pypi.org/project/pipenv/
[mise]: https://github.com/jdx/mise/releases
[helix]: https://github.com/helix-editor/helix/releases
[libreoffice]: https://wiki.documentfoundation.org/ReleasePlan
[mesa]: https://docs.mesa3d.org/release-calendar.html
[kde_gear]: https://kde.org/announcements/gear/
[jetbrains]: https://www.jetbrains.com/idea/whatsnew/
[android_studio]: https://developer.android.com/studio/releases
[mediainfo]: https://github.com/MediaArea/MediaInfo/releases/tag/v17.10
[betaflight]: https://betaflight.com/blog/2025/09/01/Calendar%20Versioning%20Change
[minecraft]: https://minecraft.wiki/w/Version_formats

# APIs and services

Versioned APIs pin a date, and the date tells both sides of the
integration how far behind it is.

Project                                   | Scheme                  | Example             | Since
----------------------------------------- | ----------------------- | ------------------- | -----
[Stripe API][stripe]                      | `YYYY-0M-0D.MODIFIER`   | 2024-09-30.acacia   | 2011
[Shopify APIs][shopify]                   | `YYYY-0M`               | 2026-07             | 2019
[Anaconda Distribution][anaconda]         | `YYYY.0M-MICRO`         | 2026.07-1           | 2018

Stripe integrations pin a dated version, and since 2024 the
twice-yearly breaking releases carry a plant name. Shopify cuts a
version each quarter, supports each for at least twelve months with
at least nine months of overlap, and echoes the version a request
was served with in the `X-Shopify-API-Version` header.

[stripe]: https://stripe.com/blog/introducing-stripes-new-api-release-process
[shopify]: https://shopify.dev/docs/api/usage/versioning
[anaconda]: https://www.anaconda.com/docs/getting-started/anaconda/release-notes

# Tooling

Implementations that compute, bump, or validate calendar versions.
Notation compatibility with this site is noted where it matters.

- [bumpver][bumpver] (Python CLI): pattern-based bumping for any
  language's version files, with the most complete calver.org token
  support. Its `MM`, `DD`, and `WW` are the pre-26.0 deprecated
  spellings of `M`, `D`, and `W`, with the same unpadded meaning.
- [calver][calver_setuptools] (setuptools plugin): derives a version
  from the build date via `strftime`. Used by PyPA's trove-classifiers.
- [hatch-calver][hatch_calver] (Hatch plugin): date-derived versions
  for Hatch-built Python packages.
- [node-calver][node_calver] (JavaScript): parse, validate, and
  increment calendar versions in Node.
- [release-please][release_please] (Google's release automation): a
  `calendar` versioning strategy is in review as of this writing.
- [calver-adoption][skill] (agent skill): walks a coding agent
  through adopting CalVer in an existing project, from detecting the
  current version to cutting the first calendar release.

[bumpver]: https://github.com/mbarkhau/bumpver
[calver_setuptools]: https://pypi.org/project/calver/
[hatch_calver]: https://pypi.org/project/hatch-calver/
[node_calver]: https://github.com/muratgozel/node-calver
[release_please]: https://github.com/googleapis/release-please/pull/2637
[skill]: https://github.com/mahmoud/calver/tree/master/skills/calver-adoption

# Other

If you know of a CalVer usage that does not fit into these categories,
please [submit it here][issues].
