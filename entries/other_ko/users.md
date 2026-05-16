---
title: CalVer 사용자
entry_root: users
special: true
publish_date: March 29, 2018
---

캘린더 버전 관리는 긴 역사를 가지고 있으며, CalVer 사용자는 모든 분야에서 찾을 수 있습니다. 계속 늘어나고 있는 이 프로젝트 이름과 버전 예시 목록은 [확장에 열려][issues] 있습니다.

[issues]: https://github.com/mahmoud/calver/issues

[TOC]

표기법과 더 자세한 사용 사례에 대한 내용은 [CalVer 개요][overview]를 참조하세요.

[overview]: /overview_ko.html

# 애플리케이션

크고 작은, 폐쇄적이고 개방적인 많은 시스템과 애플리케이션이 캘린더 날짜를 버전에 통합하고 있습니다.

프로젝트                          | CalVer 형식         | 예시
--------------------------------- | ------------------- | ---------------
[Ubuntu][ubuntu]                  | `YY.0M`             | 4.10 - 20.04
[NixOS][nixos_releases]           | `YY.0M`             | 13.10 - 17.03
[Microsoft Windows][ms_win]       | `YY`/`YYYY`         | 95, 98, 2000
[OpenSCAD][openscad]              | `YYYY.0M`           | 2015.03
[JetBrains PyCharm][pycharm]      | `YYYY.MINOR.MICRO`  | 2017.1.2
[ArchLinux][archlinux]            | `YYYY.0M.0D`        | 2018.03.01
[Unity][unity]                    | `YYYY.MINOR.MICRO`  | 2019.2.2
[Slack for Mobile][slack]         | `YY.0M.MICRO`       | 19.08.10
[CockroachDB][cockroachdb]        | `YY.MINOR.MICRO`    | 19.1.0
[Dgraph][dgraph]                  | `YY.0M.MICRO`       | 20.03.0, 20.03.1-beta.Jun15
[Spring Cloud][spring_cloud]      | `YYYY.MINOR.MICRO`  | 2020.0.0-RC2
[Tesla Firmware][tesla_fw]        | `YYYY.WW.MICRO`     | 2020.12.10
[KDE Apps][kde_apps]              | `YY.0M.MICRO`       | 20.12.0
[Consensys Quorum][quorum]        | `YY.MM.MICRO`       | 20.10.0
[Home Assistant][ha]              | `YYYY.MM.MICRO`     | 20.12.1

[ubuntu]: /overview_ko.html#ubuntu
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

# 표준

프로그래밍 언어 표준은 관례적으로 연도(`YY`/`YYYY`)로 명명되며, 캘린더 버전 관리의 가장 오래된 주목할 만한 사례 중 일부를 포함합니다.

프로젝트                            | CalVer 형식        | 예시
----------------------------------- | ------------------ | ---------------
[Ada][ada]                          | `YY`/`YYYY`        | 83, 95, 2012
[ALGOL][algol]                      | `YY`               | 58, 60, 68
[C][c]                              | `YY`               | 89, 99, 11
[C++][cpp]                          | `YY`               | 98, 03, 11, 14, 17
[Fortran][fortran]                  | `YY`/`YYYY`        | 66, 77, 90, 95, 2003, 2008
[ECMAScript][js] (JavaScript)       | `YYYY`             | 2015, 2020
[Python manylinux][manylinux]       | `YYYY`             | 2010 ("이 버전까지 하위 호환")

[ada]: https://en.wikipedia.org/wiki/Ada_(programming_language)
[algol]: https://en.wikipedia.org/wiki/ALGOL_60
[c]: https://en.wikipedia.org/wiki/C_(programming_language)
[cpp]: https://en.wikipedia.org/wiki/C%2B%2B
[fortran]: https://en.wikipedia.org/wiki/Fortran
[manylinux]: https://www.python.org/dev/peps/pep-0571/
[js]: https://en.wikipedia.org/wiki/ECMAScript#Versions

# 라이브러리

CalVer 소프트웨어 라이브러리는 개발자가 의존성 목록만 봐도 소프트웨어의 최신성을 평가할 수 있게 해줍니다.

프로젝트                          | CalVer 형식          | 예시
--------------------------------- | -------------------- | ---------------
[Boltons][boltons]                | `YY.MINOR.MICRO`     | 17.2.0
[Twisted][twisted]                | `YY.MM.MICRO`        | 16.1.1
[certifi][certifi]                | `YYYY.MM.DD`         | 2016.2.28
[Teradata][teradata]              | `YY.MM.MINOR.MICRO`  | 15.10.0.16
[pytz][pytz]                      | `YYYY.MM`            | 2016.4
[attrs][attrs]                    | `YY.MINOR.MICRO`     | 17.4.0

[boltons]: http://boltons.readthedocs.io/en/latest/
[twisted]: /overview_ko.html#twisted
[certifi]: https://pypi.python.org/pypi/certifi
[teradata]: /overview_ko.html#teradata
[pytz]: /overview_ko.html#pytz
[attrs]: https://github.com/python-attrs/attrs

# 유틸리티

시스템 관리자는 제대로 된 버전이 있는 도구를 선호합니다.

프로젝트                              | CalVer 형식          | 예시
------------------------------------- | -------------------- | ---------------
[pip][pip] ([상세][pipdeet])           | `YY.MINOR.MICRO`     | 19.2.3
[youtube-dl][youtube-dl]              | `YYYY.0M.0D.MICRO`   | 2016.06.19.1
[fusefs-ntfs][fsfntfs]                | `YYYY.MM.DD_MICRO`   | 2016.2.22_1
[black][black]                        | `YY.MM.MICRO`        | 18.3a0

[youtube-dl]: /overview_ko.html#youtube-dl
[fsfntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[pip]: https://pypi.org/project/pip/#history
[black]: https://github.com/ambv/black
[pipdeet]: https://groups.google.com/forum/#!topic/pypa-dev/AKsd2D_F4cM

# 기타

이 카테고리에 맞지 않는 CalVer 사용 사례를 알고 계시면, [여기에 제출][issues]해 주세요.
