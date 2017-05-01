---
title: CalVer Users
entry_root: users
---

Calendar versioning has a long history, and CalVer users can be found
in all areas of software development. This ever-growing,
never-complete list of project names and example versions is
[open to expansion][issues].

[issues]: https://github.com/mahmoud/calver/issues

[TOC]

For more details about the notation and for more detailed use cases,
see the [CalVer overview][overview].

[overview]: /overview.html

# Products

From small to large, closed and open, many products have all profitted
from incorporating calendar dates into their brands.

Project                         | CalVer Format      | Examples
------------------------------- | ------------------ | ---------------
[Ubuntu][ubuntu]                | `YY.0M`            | 4.10 - 17.04
[NixOS][nixos_releases]         | `YY.0M`            | 13.10 - 17.03
[Microsoft Windows][ms_win]     | `YY`/`YYYY`        | 95, 98, 2000
[OpenSCAD][openscad]            | `YYYY.0M`          | 2015.03
[JetBrains PyCharm][pycharm]    | `YYYY.MINOR.MICRO` | 2017.1.2

[ubuntu]: /overview.html#ubuntu
[ms_win]: https://en.wikipedia.org/wiki/Microsoft_Windows
[openscad]: https://en.wikipedia.org/wiki/OpenSCAD
[pycharm]: https://en.wikipedia.org/wiki/PyCharm

# Standards

Programming language standards are conventionally named for their year
(`YY`/`YYYY`), and comprise some of the oldest notable usages of
calendar versioning.

Project                         | CalVer Format     | Examples
------------------------------- | ----------------- | ---------------
[Ada][ada]                      | `YY`/`YYYY`       | 83, 95, 2012
[ALGOL][algol]                  | `YY`              | 58, 60, 68
[C][c]                          | `YY`              | 89, 99, 11
[C++][cpp]                      | `YY`              | 98, 03, 11, 14, 17
[Fortran][fortran]              | `YY`/`YYYY`       | 66, 77, 90, 95, 2003, 2008

[ada]: https://en.wikipedia.org/wiki/Ada_(programming_language)
[algol]: https://en.wikipedia.org/wiki/ALGOL_60
[c]: https://en.wikipedia.org/wiki/C_(programming_language)
[cpp]: https://en.wikipedia.org/wiki/C%2B%2B
[fortran]: https://en.wikipedia.org/wiki/Fortran

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

[boltons]: http://boltons.readthedocs.io/en/latest/
[twisted]: /overview.html#twisted
[certifi]: https://pypi.python.org/pypi/certifi
[teradata]: /overview.html#teradata
[pytz]: /overview.html#pytz

# Utilities

System administrators appreciate a tool with a proper version.

Project                         | CalVer Format       | Examples
------------------------------- | ------------------- | ---------------
[youtube_dl][youtube_dl]        | `YYYY.0M.0D.MICRO`  | 2016.06.19.1
[fusefs-ntfs][fsfntfs]          | `YYYY.MM.DD_MICRO`  | 2016.2.22_1

[youtube_dl]: /overview.html#youtube_dl
[fsfntfs]: http://www.freshports.org/sysutils/fusefs-ntfs

# Other

If you know of a CalVer usage that does not fit into these categories,
please [submit it here][issues].
