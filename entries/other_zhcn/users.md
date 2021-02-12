---
title: CalVer Users (中文)
entry_root: users_zhcn
special: true
publish_date: May 30, 2020
orig_publish_date: March 29, 2018
---

日历版本化由来已久，在所有领域都可以找到 CalVer 用户。
这个不断增长的、从未完成的项目名称清单
和示例版本是 [开放的][issues]。

[issues]: https://github.com/mahmoud/calver/issues

[TOC]

关于标记与用例的更多详细信息，
见 [CalVer概述][overview]。

[overview]: /overview-zhcn.html

# 产品

从小到大，从闭源到开源，很多产品将日期加入到品牌中
都获得了收益。

产品                            | CalVer 格式         | 例子
------------------------------- | ------------------ | ---------------
[Ubuntu][ubuntu]                | `YY.0M`            | 4.10 - 17.04
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

# 标准

程序设计语言标准通常以年份命名
（`YY`/`YYYY`），包括一些日历化版本最古老的
著名用法。

产品                              | CalVer 格式        | 例子
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

# 库

CalVer 软件库允许开发人员只需要看依赖列表一眼
就可以评估他们软件的新旧程度。

产品                            | CalVer 格式          | 例子
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

# 实用工具

系统管理员喜欢具有合适版本的工具。

产品                            | CalVer 格式          | 例子
------------------------------- | ------------------- | ---------------
[pip][pip] ([details][pipdeet]) | `YYYY.MINOR.MICRO`  | 19.2.3
[youtube-dl][youtube-dl]        | `YYYY.0M.0D.MICRO`  | 2016.06.19.1
[fusefs-ntfs][fsfntfs]          | `YYYY.MM.DD_MICRO`  | 2016.2.22_1
[black][black]                  | `YY.MM.MICRO`       | 18.3a0

[youtube-dl]: /overview.html#youtube-dl
[fsfntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[pip]: https://pypi.org/project/pip/#history
[black]: https://github.com/ambv/black
[pipdeet]: https://groups.google.com/forum/#!topic/pypa-dev/AKsd2D_F4cM

# 其他

如果您知道 CalVer 用法不适合这些类别，
请 [在此处提交问题][issues]。
