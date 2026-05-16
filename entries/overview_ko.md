---
title: 캘린더 버전 관리 / Calendar Versioning
special: true
entry_root: overview_ko
publish_date: May 2, 2026
orig_publish_date: March 25, 2016
---

_CalVer는 어떤 임의의 숫자 대신, 프로젝트의 릴리스 날짜를 기반으로 하는 버전 관리 컨벤션입니다._

**버전 관리는 시간이 쌓일수록 더 가치 있어집니다.**

메인테이너들에게 있어 버전 관리는 끊임없이 확장되는 생태계 안에서 의존성 버전을 정확히 지정할 수 있게 해줍니다. 마케터나 홍보 담당자에게 프로젝트 버전은 프로젝트가 계속 움직이고 있다는 신호입니다. 모두에게 버전 관리는 미래로 업그레이드하면서도 과거를 참조할 수 있게 해줍니다.

프로젝트마다 다른 버전 관리 시스템을 사용하지만, 몇 가지 공통된 관행이 자리잡았습니다. 예를 들어, 점으로 구분된 숫자(예: _3.1.4_)는 사실상 표준입니다. 또 다른 일반적인 버전 패턴은 보통 릴리스 날짜의 일부를 시간 기반 요소로 포함합니다.

이러한 날짜 기반 접근 방식을 캘린더 버전 관리(Calendar Versioning), 줄여서 **CalVer**라고 부릅니다.

[TOC]

# 스킴

크고 작은 프로젝트들이 오래전부터 사용해온 다양한 캘린더 버전 관리 스킴이 있습니다. 하나의 스킴만을 CalVer로 선언하는 것보다, 각각의 실용성을 인정하고 프로젝트에 맞게 [스킴을 설계][designing_a_version]하는 것이 중요합니다. 먼저 버전의 구성 요소를 살펴보겠습니다:

- **Major** - 버전의 첫 번째 숫자. 2와 3은 Python의 유명한 메이저 버전입니다. 메이저 세그먼트는 캘린더 기반 구성 요소로 가장 많이 사용됩니다.
- **Minor** - 버전의 두 번째 숫자. 7은 Python의 가장 인기 있는 마이너 버전입니다.
- **Micro** - 세 번째이자 보통 마지막 숫자. "패치" 세그먼트라고도 불립니다.
- **Modifier** - "dev", "alpha", "beta", "rc1" 등과 같은 선택적 텍스트 태그.

현대의 대부분의 버전 식별자는 두 개 또는 세 개의 숫자 세그먼트와 선택적 수정자로 구성됩니다. 관례상 네 개의 숫자 세그먼트 버전은 권장되지 않습니다.

[designing_a_version]: http://sedimental.org/designing_a_version.html

아래 [사례](#case_studies)에서 볼 수 있듯이, 프로젝트들은 버전에 날짜를 활용하는 다양한 방법을 발견했습니다. CalVer는 하나의 스킴을 선택하는 대신, "시맨틱" 버전에 더해 개발자를 위한 표준 용어를 도입합니다:

- **`YYYY`** - 네 자리 연도 - 2006, 2016, 2106
- **`YY`** - 앞자리 0을 붙이지 않은 축약 연도 - 6, 16, 106
- **`0Y`** - 앞자리 0을 붙인 축약 연도 - 06, 16, 106
- **`MM`** - 앞자리 0을 붙이지 않은 월 - 1, 2 ... 11, 12
- **`0M`** - 앞자리 0을 붙인 월 - 01, 02 ... 11, 12
- **`WW`** - 앞자리 0을 붙이지 않은 주차 - 1, 2, 33, 52
- **`0W`** - 앞자리 0을 붙인 주차 - 01, 02, 33, 52
- **`DD`** - 앞자리 0을 붙이지 않은 일자 - 1, 2 ... 30, 31
- **`0D`** - 앞자리 0을 붙인 일자 - 01, 02 ... 30, 31

전통적인 증분 버전 번호는 0부터 시작하는 반면, 날짜 세그먼트는 1부터 시작하며, 축약 연도와 0으로 채워진 연도는 2000년 기준 상대값입니다. 주(week) 사용은 일반적으로 월/일과 상호 배타적입니다.

[그레고리력][gregorian]과 [UTC][utc] 관례를 기본으로 사용합니다. 기술적으로는 어떤 달력도 사용할 수 있으며, 프로젝트에서 어떤 달력을 사용하는지 명시하면 됩니다.

[gregorian]: https://en.wikipedia.org/wiki/Gregorian_calendar
[utc]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time

# 사례

CalVer를 사용하는 프로젝트는 꽤 많습니다. 여기서는 주목할 만하고 다양한 사용 사례를 가진 프로젝트들을 선정했습니다.

## Ubuntu

<img src="https://img.shields.io/badge/calver-YY.0M.MICRO-22bfda.svg" />

가장 널리 알려진 Linux 기반 운영 체제 중 하나인 **[Ubuntu][ubuntu]**는 축약 연도와 0으로 채워진 월을 사용하는 세 세그먼트 CalVer 스킴을 사용합니다. 2004년 10월 [처음 시작][ubuntu_releases]부터 그래왔으며, 4.10이 Ubuntu의 첫 번째 일반 릴리스였습니다.

운영 체제 하나만 해도 수많은 구성 요소가 포함되어 있어, 임의의 숫자로 많은 의미를 전달하기가 어렵습니다. 프로젝트 릴리스에 날짜를 붙임으로써, 캘린더 기반 버전은 단순한 임의의 숫자 그 이상이 되어 릴리스 시점이라는 명확하고 유용한 정보를 담게 됩니다.

Ubuntu는 CalVer 스킴을 지원 일정과 통합하여 추가적인 이점을 얻습니다. Ubuntu는 현재 장기 지원(LTS) 릴리스에 5년 지원 기간을 제공하고, LTS가 아닌 릴리스에는 9개월만 지원합니다. CalVer와 간단한 산술 덕분에, 어떤 사용자든 자신의 버전이 아직 지원되는지 쉽게 확인할 수 있습니다. 작성 시점 기준 현재 LTS 릴리스인 16.04는 2021년 4월까지 지원됩니다.

[ubuntu]: http://www.ubuntu.com/
[ubuntu_releases]: https://en.wikipedia.org/wiki/List_of_Ubuntu_releases

## Twisted

<img src="https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg" />

Python 네트워킹과 비동기 실행을 대표하는 프레임워크인 **[Twisted][twisted]**는 세 세그먼트 CalVer 스킴을 사용합니다. 메이저 버전 슬롯에는 축약 연도, 마이너 버전 슬롯에는 축약 월, 세 번째이자 마지막 슬롯에는 마이크로/패치 버전이 들어갑니다.

2002년에 처음 릴리스되어 오늘날에도 활발히 개발 중인 Twisted는 방대한 범위에 걸맞게 성장한 [성숙한][twisted_wp] 라이브러리입니다. IRC 클라이언트부터 HTTP 서버, 동시 프로그래밍을 위한 다양한 유틸리티까지 모든 것을 갖추고 있습니다. 운영 체제처럼 Twisted도 구성 요소가 많아서, 각 구성 요소마다 하위 호환성 유지 정책이 다르기 때문에 SemVer(시맨틱 버전 관리)를 일괄 적용하기 어렵습니다.

Twisted의 지원 중단 예정이 아닌 각 버전 간에 하위 호환성이 유지되며, 호환성을 깨는 변경은 시간 기반으로 이루어집니다. 기능을 폐기하는 릴리스와 해당 기능을 제거하는 릴리스 사이에 1년이 경과하고 두 번의 릴리스가 발행되어야 합니다.

이 버전 관리 스킴은 [Klein][klein], [Treq][treq], 그리고 Twisted의 의존성 중 하나인 [PyOpenSSL][pyopenssl] 등 관련 프로젝트로 퍼져 나갔습니다.

[twisted]: https://twistedmatrix.com
[twisted_wp]: https://en.wikipedia.org/wiki/Twisted_%28software%29
[klein]: https://github.com/twisted/klein
[treq]: https://github.com/twisted/treq
[pyopenssl]: https://github.com/pyca/pyopenssl

## youtube-dl

<img src="https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg" />

인터넷 미디어를 보관하는 사람들에게 오래 사랑받아 온 도구 **[youtube-dl][youtube-dl]**은 전체 연도, 0으로 채워진 월, 0으로 채워진 일자로 구성된 세 세그먼트 CalVer 스킴을 사용합니다. 일부 기술적 맥락에서 마이크로 세그먼트가 추가되는 경우를 제외하면, 버전은 거의 날짜 정보만으로 구성됩니다.

이름과 달리 youtube-dl의 범위는 광범위합니다. 계속 늘어나는 사이트 목록에서 오디오와 비디오를 추출하는 것을 지원합니다. 지원되는 서비스의 빠른 릴리스 주기를 고려하면, 이 프로젝트가 CalVer를 이 정도로 적극적으로 채택한 이유가 명확해집니다.

[youtube-dl]: https://youtube-dl.org/

## IANA/Olson 시간대 데이터베이스

<img src="https://img.shields.io/badge/calver-YYYYa..z-22bfda.svg" />

[IANA/Olson 시간대 데이터베이스][iana_tz]는 전 세계 대표 지역들의 현지 시간 역사를 담고 있으며, 시간대나 일광 절약 시간제를 다루는 사실상 모든 운영 체제, 데이터베이스, 웹사이트 등의 단일 진실 공급원(source of truth)입니다.

정치적 기구가 시간대 경계, UTC 오프셋, 일광 절약 규칙에 가하는 변경 사항을 반영하기 위해 주기적으로 업데이트됩니다. 이러한 변경이 고정된 일정이 아닌 정치적·입법적 결정을 따르기 때문에, 데이터베이스는 네 자리 연도 뒤에 소문자(a부터 z, 그 다음 za부터 zz, 그 다음 zza부터 zzz 순)를 붙여 [버전 관리][tz_version]합니다. 캘린더 버전 관리는 혼란스러운 시스템에 날짜 기반 스냅샷을 제공합니다.

[iana_tz]: https://www.iana.org/time-zones
[tz_version]: https://data.iana.org/time-zones/tz-link.html

## Teradata

<img src="https://img.shields.io/badge/calver-YY.MM.MINOR.MICRO-22bfda.svg" />

**[Teradata UDA 클라이언트][teradata_uda]**는 [Teradata][teradata]의 데이터 웨어하우징 기술에 대한 [차세대 접근][uda_blog]을 제공합니다.

Teradata의 사용 사례는 기술이나 회사의 명성 때문이 아니라, 2016년에 `15.10`으로 버전이 매겨진 여러 릴리스가 있었기 때문에 주목할 만합니다. 처음에는 이상해 보일 수 있지만, 의미와 유용성은 명확합니다.

라이브러리 메인테이너들은 [시맨틱 버전 관리][semver]와 CalVer를 영리하게 절충하여 사용하고 있습니다. 버전의 **YY.MM** 부분은 결합된 SemVer 메이저 버전으로 사용됩니다. 즉, 새 릴리스에서 라이브러리의 API는 2015년 10월과 동일하게 유지됩니다. 그 이후로 작성된 의존 코드는 안전하게 업그레이드할 수 있습니다. 다음 번 API 호환성을 깨는 변경이 있을 때 연도와 월 세그먼트가 업데이트됩니다.

[teradata]: http://www.teradata.com/
[teradata_uda]: https://pypi.python.org/pypi/teradata
[uda_blog]: https://developer.teradata.com/tools/reference/teradata-python-module
[semver]: http://semver.org/

## 기타 주목할 만한 프로젝트

- [boltons][boltons] - **`YY.MINOR.MICRO`** - Python 표준 라이브러리를 보완하는 광범위한 유틸리티 라이브러리.
- [certifi][certifi] - **`YYYY.MM.DD`** - 보안 인터넷 통신에 사용되는 Mozilla의 인증 기관 번들 래퍼. [IANA 시간대 데이터베이스](#iana-olson-시간대-데이터베이스)와 유사하게, 인증서 업데이트는 고정된 일정을 따르지 않지만 시의적절하고 날짜를 기반으로 한 업데이트가 보안에 필수적입니다.
- [fusefs-ntfs][fusefs-ntfs] - **`YYYY.MM.DD_MICRO`** - Unix 시스템을 위한 가장 초기이자 가장 호환성 높은 NTFS 접근 레이어 중 하나.
- [LibreOffice][libreoffice] - **`YY.MM`** - 강력한 무료 오피스 스위트로, OpenOffice.org의 후계자.
- [OpenSCAD][openscad] - **`YYYY.0M`** - 솔리드 3D CAD 모델링을 위한 최고의 오픈 소스 도구.
- [pip][pip] - **`YY.MINOR.MICRO`** - Python 공식 패키지 관리자.
- [PyCharm][pycharm] - **`YYYY.MINOR.MICRO`** - 선도적인 Python IDE.
- [Stripe API][stripe] - **`YYYY-MM-DD`** - API 중심 결제 처리 플랫폼.
- [Unity][unity] - **`YYYY.MINOR.MICRO`** - 크로스 플랫폼 게임 엔진.

[boltons]: https://boltons.readthedocs.io/en/latest/
[certifi]: https://pypi.python.org/pypi/certifi
[fusefs-ntfs]: https://www.freshports.org/sysutils/fusefs-ntfs
[libreoffice]: https://www.libreoffice.org/
[openscad]: https://openscad.org/
[pip]: https://pip.pypa.io/en/stable/news/
[pycharm]: https://www.jetbrains.com/pycharm/download/
[stripe]: https://stripe.com/blog/api-versioning
[unity]: https://unity3d.com/unity/whats-new/

CalVer 사용자들의 늘어나는 목록은 [사용자 페이지][users]를 참조하세요.

[users]: /users.html

# CalVer를 사용해야 할 때

당신이 알지 못하는 사람들도 당신의 프로젝트를 진지하게 사용한다면, 진지한 버전을 사용하세요. CalVer 사용 여부를 결정하는 것은 그 어느 때보다 쉽습니다:

- 프로젝트의 범위가 크거나 지속적으로 변경됩니까?
  - [Ubuntu](#ubuntu)와 [Twisted](#twisted)와 같은 대규모 시스템 및 프레임워크.
  - [Boltons](#기타-주목할-만한-프로젝트)와 같이 범위가 불분명한 유틸리티 모음.
- 프로젝트가 어떤 식으로든 시간에 민감합니까? 외부의 변화가 새 릴리스를 유도합니까?
  - [Ubuntu](#ubuntu)의 지원 일정에 대한 비즈니스 요구 사항.
  - [certifi](#기타-주목할-만한-프로젝트)의 인증서 업데이트 필요성과 같은 보안 업데이트.
  - [IANA 데이터베이스](#iana-olson-시간대-데이터베이스)의 시간대 변경 처리와 같은 정치적 변화.

이 중 하나라도 해당된다면, CalVer의 시맨틱이 프로젝트에 강력한 선택이 될 것입니다.
