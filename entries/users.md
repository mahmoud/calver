---
title: CalVer Users
entry_root: users
special: true
publish_date: March 29, 2018
---

Calendar versioning has a long history, and CalVer users can be found
in all areas. This ever-growing, never-complete list of project names
and example versions is [open to expansion][issues].

[issues]: https://github.com/mahmoud/calver/issues

[TOC]

For more details about the notation and for more detailed use cases,
see the [CalVer overview][overview].

[overview]: /overview.html

# Applications

From small to large, closed and open, many systems and applications
from incorporating calendar dates into their projects.

Project                         | CalVer Format      | Examples
------------------------------- | ------------------ | ---------------
[Ubuntu][ubuntu]                | `YY.0M`            | 4.10 - 20.04
[NixOS][nixos_releases]         | `YY.0M`            | 13.10 - 17.03
[Microsoft Windows][ms_win]     | `YY`/`YYYY`        | 95, 98, 2000
[OpenSCAD][openscad]            | `YYYY.0M`          | 2015.03
[JetBrains PyCharm][pycharm]    | `YYYY.MINOR.MICRO` | 2017.1.2
[ArchLinux][archlinux]          | `YYYY.0M.0D`       | 2018.03.01
[Unity][unity]                  | `YYYY.MINOR.MICRO` | 2019.2.2
[Slack for Mobile][slack]       | `YY.0M.MICRO`      | 19.08.10
[CockroachDB][cockroachdb]      | `YY.MINOR.MICRO`   | 19.1.0
[Dgraph][dgraph]                | `YY.0M.MICRO`      | 20.03.0, 20.03.1-beta.Jun15
[Spring Cloud][spring_cloud]    | `YYYY.MINOR.MICRO` | 2020.0.0-RC2
[Tesla Firmware][tesla_fw]      | `YYYY.WW.MICRO`    | 2020.12.10
[KDE Apps][kde_apps]            | `YY.0M.MICRO`      | 20.12.0
[Consensys Quorum][quorum]      | `YY.MM.MICRO`      | 20.10.0
[Home Assistant][ha]            | `YYYY.MM.MICRO`    | 2020.12.1
[Bookstack][bookstack]          | `vYY.0M.MICRO`     | v23.01.1

[ubuntu]: /overview.html#ubuntu
[nixos_releases]: https://nixos.org/news.html
[ms_win]: https://en.wikipedia.org/wiki/Microsoft_Windows
[openscad]: https://en.wikipedia.org/wiki/OpenSCAD
[pycharm]: https://en.wikipedia.org/wiki/PyCharm
[archlinux]: https://www.archlinux.org/releng/releases/
[unity]: https://unity3d.com/unity/whats-new/
[slack]: https://slack.com/release-notes/android
[cockroachdb]: https://www.cockroachlabs.com/blog/calendar-versioning/
[dgraph]: https://dgraph.io/blog/post/dgraph-calendar-versioning/
[spring_cloud]: https://spring.io/blog/2020/04/17/spring-cloud-2020-0-0-m1-released
[tesla_fw]: https://teslafi.com/firmware/
[kde_apps]: https://kde.org/announcements/releases/2020-12-apps-update/
[quorum]: https://consensys.net/blog/quorum/consensys-quorum-is-moving-to-calendar-versioning/
[ha]: https://www.home-assistant.io/blog/2020/12/13/release-202012/
[bookstack]: https://github.com/BookStackApp/BookStack/issues/2570

# Standards

Programming language standards are conventionally named for their year
(`YY`/`YYYY`), and comprise some of the oldest notable usages of
calendar versioning.

Project                           | CalVer Format     | Examples
--------------------------------- | ----------------- | ---------------
[Ada][ada]                        | `YY`/`YYYY`       | 83, 95, 2012
[ALGOL][algol]                    | `YY`              | 58, 60, 68
[C][c]                            | `YY`              | 89, 99, 11
[C++][cpp]                        | `YY`              | 98, 03, 11, 14, 17
[Fortran][fortran]                | `YY`/`YYYY`       | 66, 77, 90, 95, 2003, 2008
[ECMAScript][js] (aka JavaScript) | `YYYY`            | 2015, 2020
[Python manylinux][manylinux]     | `YYYY`            | 2010 ("backwards compatible to")


[ada]: https://en.wikipedia.org/wiki/Ada_(programming_language)
[algol]: https://en.wikipedia.org/wiki/ALGOL_60
[c]: https://en.wikipedia.org/wiki/C_(programming_language)
[cpp]: https://en.wikipedia.org/wiki/C%2B%2B
[fortran]: https://en.wikipedia.org/wiki/Fortran
[manylinux]: https://www.python.org/dev/peps/pep-0571/
[js]: https://en.wikipedia.org/wiki/ECMAScript#Versions

# Libraries

CalVer software libraries allow developers to evaluate their software
freshness with just a glance at the dependency list.

Project                         | CalVer Format       | Examples
------------------------------- | ------------------- | ---------------
[Boltons][boltons]              | `YY.MINOR.MICRO`    | 17.2.0
[Twisted][twisted]              | `YY.MM.MICRO`       | 16.1.1
[certifi][certifi]              | `YYYY.MM.DD`        | 2016.2.28
[Teradata][teradata]            | `YY.MM.MINOR.MICRO` | 15.10.0.16
[pytz][pytz]                    | `YYYY.MM`           | 2016.4
[attrs][attrs]                  | `YY.MINOR.MICRO`    | 17.4.0
[pip][pip]                      | `YY.MINOR.MICRO`    | 18.0 - 19.0.3

[boltons]: http://boltons.readthedocs.io/en/latest/
[twisted]: /overview.html#twisted
[certifi]: https://pypi.python.org/pypi/certifi
[teradata]: /overview.html#teradata
[pytz]: /overview.html#pytz
[attrs]: https://github.com/python-attrs/attrs
[pip]: https://pip.pypa.io/en/stable/news/

# Utilities

System administrators appreciate a tool with a proper version.

Project                         | CalVer Format       | Examples
------------------------------- | ------------------- | ---------------
[pip][pip] ([details][pipdeet]) | `YY.MINOR.MICRO`    | 19.2.3
[youtube-dl][youtube-dl]        | `YYYY.0M.0D.MICRO`  | 2016.06.19.1
[fusefs-ntfs][fsfntfs]          | `YYYY.MM.DD_MICRO`  | 2016.2.22_1
[black][black]                  | `YY.MM.MICRO`       | 18.3a0

[youtube-dl]: /overview.html#youtube-dl
[fsfntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[pip]: https://pypi.org/project/pip/#history
[black]: https://github.com/ambv/black
[pipdeet]: https://groups.google.com/forum/#!topic/pypa-dev/AKsd2D_F4cM

# Other

If you know of a CalVer usage that does not fit into these categories,
please [submit it here][issues].
