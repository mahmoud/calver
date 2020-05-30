---
title: 日历化版本 / Calendar Versioning
special: true
entry_root: overview_zhcn
publish_date: May 30, 2020
orig_publish_date: March 25, 2016
---

*CalVer 不是基于任意数字，而是基于项目发布日期
的版本控制约定*

**版本随着时间的推移会变得更好。**

对于维护者，版本使我们在不断扩大的生态系统中
可以指定精确的依赖关系。对于卖家和推广者来说，
项目的版本是一个品牌的活力部分。对我们所有人来说，
版本使我们在升级到将来时可以参考过去。

不同的项目使用不同的系统命名版本，但是常见的
实践已经浮现出来。例如，以点分隔的数字（例如，
*3.1.4*）就是全部。另一种常见的版本模式
包含一个基于时间的元素，通常是发布日期的一部分。

这种基于日期的方法被称为 “日历化版本”（Calendar Versioning），
或者简称 **CalVer**。

[TOC]

# 方案

有多种日历化版本方案，长期被各种大小项目
使用。与其宣布某个方案为 CalVer，更重要的是
要认识到每个方案的可行性并
[设计一个适合项目的方案][designing_a_version]。首先，
版本的各部分：

* **主要** - 版本中的第一个数字。2 和 3 是 Python 的著名
  主要版本。主要部分是基于日历的最常见组件。
* **次要** - 版本中的第二个数字。7 是 Python 的最受欢迎的
  次要版本。
* **微小** - 版本中的第三个且通常是最终数字。有时
  称为 “补丁” 部分。
* **修饰符** - 可选的文本标记，例如 “dev”、“alpha”、“beta”、
  “rc1”，依此类推。

绝大多数现代版本标识符是由两个或
三个数字段组成，以及可选的修饰符。通常
建议不要使用四个数字段的版本。

[designing_a_version]: http://sedimental.org/designing_a_version.html

如下面的 [样例学习](#样例学习) 所示，项目
发现了不止一种有用的方法在版本中使用
日期。 作为对比，CalVer 并未像 “语义化版本” 那样选择单一方案，
而是引入了开发人员的
标准术语：

* **`YYYY`** - 年份全称 - 2006、2016、2106
* **`YY`** - 年份缩写 - 6、16、106
* **`0Y`** - 以零填充的年份 - 06、16、106
* **`MM`** - 月份缩写 - 1、2 ... 11、12
* **`0M`** - 以零填充的月份 - 01、02 ... 11、12
* **`WW`** - 星期（自年初开始）- 1、2、33、52
* **`0W`** - 以零填充的星期 - 01、02、33、52
* **`DD`** - 日 - 1、2 ... 30、31
* **`0D`** - 以零填充的日 - 01、02 ... 30、31

请注意，传统的递增版本号是从 0 开始，
而日期段是从 1 开始的，且年份缩写和以零填充的年份
是相对于 2000 年。还请注意，星期的使用
通常与月/日互斥。

假定采用 [格里高利历][gregorian]，
[UTC][utc] 的惯例也是如此。从技术上讲可以使用任何日历，
只要提供的项目声明使用哪一个。

[gregorian]: https://zh.wikipedia.org/wiki/%E6%A0%BC%E9%87%8C%E6%9B%86
[utc]: https://zh.wikipedia.org/wiki/%E5%8D%8F%E8%B0%83%E4%B8%96%E7%95%8C%E6%97%B6

# 样例学习

CalVer 有很多用户。考虑到知名度和使用案例的多样性
选择以下项目。

## Ubuntu

<img src="https://img.shields.io/badge/calver-YY.0M.MICRO-22bfda.svg" />

**[Ubuntu][ubuntu]**，最杰出的基于 Linux 可用的
操作系统之一，使用三段式 CalVer 方案，包含
年份和以零填充的月份。它
[从一开始][ubuntu_releases] 就这样做了，在 2004 年 10 月，将 4.10
作为 Ubuntu 第一个普通版本。

即使是一个简单的操作系统，也会涉及到很多很多部分，使它
很难用一个任意数字传达太多含义。通过
约定项目发布日期，基于日历的版本要比
一个任意数字更好，基于简单的事实可以
传达有用的信息。

通过 CalVer 方案与 Ubuntu 的支持周期结合，
Ubuntu 从中获取了额外的好处。Ubuntu 目前为
长期支持（LTS）版本提供五年支持，
为非 LTS 版本只提供 9 个月支持。感谢 CalVer 和
基本算术，任何用户都可以轻松确定他们使用的版本是否
仍受支持。在写下这段文字时当前的 LTS 版本
是 16.04，将会支持到 2021 年 4 月。

[ubuntu]: http://www.ubuntu.com/
[ubuntu_releases]: https://zh.wikipedia.org/wiki/Ubuntu%E5%8F%91%E8%A1%8C%E7%89%88%E5%88%97%E8%A1%A8

## Twisted

<img src="https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg" />

**[Twisted][twisted]**，受人尊敬的 Python 网络和
异步执行框架，使用三段式 CalVer 方案，
在主要版本部分使用年份缩写，在次要版本部分使用
该年份的发行序号，而微小版本部分为错误修正版本号。

2002 年首次发布，至今仍在积极开发中，Twisted 是
一个已经成长为大范围的 [成熟的][twisted_wp] 库。
它具有从 IRC 客户端到 HTTP 服务器到
用于并发编程的一系列实用工具的所有功能。就像一个
操作系统，Twisted 有很多部分组成，而 SemVer 支持
个别的部分单独废弃与打破兼容性，因而并不适合。

在每一个连续的版本之间 Twisted 的非废弃部分都是
向后兼容的，并且要求打破兼容性修改按照基于时间的计划：
必须经过一年的时间并且在标记废弃功能与删除功能之间
要间隔两个发布版本。

Twisted 的版本方案已扩展到相关项目，包括：
[Klein][klein]、[Treq][treq]，甚至是 Twisted 的一个依赖库，
[PyOpenSSL][pyopenssl]。

[twisted]: https://twistedmatrix.com
[twisted_wp]: https://en.wikipedia.org/wiki/Twisted_%28software%29
[klein]: https://github.com/twisted/klein
[treq]: https://github.com/twisted/treq
[pyopenssl]: https://github.com/pyca/pyopenssl

## youtube_dl

<img src="https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg" />

**[youtube_dl][youtube_dl]**，是各地的互联网媒体档案员的盟友，
使用三段式的 CalVer 方案，
包括年份全称、以零填充的月、以零填充的日。
除了由于某些技术背景下添加的一个微小版本部分，
这个版本几乎完全由日历驱动。

尽管有这个名字，但 youtube_dl 的使用范围很广。它支持
从很多网站中提取音频和视频，并且这一长串网站列表
还在不断扩大。考虑到支持服务的
快速发布周期，它清楚地说明了
为什么该项目如此深度的使用 CalVer。

[youtube_dl]: https://rg3.github.io/youtube-dl/

## pytz

<img src="https://img.shields.io/badge/calver-YYYY.MINOR-22bfda.svg" />

**[pytz][pytz]** 是 [IANA/Olson timezone database][iana_tz]
 的 Python 实现，是所有计算机精确时间背后的数据库。
pytz 使用两段式 CalVer 方案，
包括年份全称和次要版本。

虽然 Python 有 “内置电池” 架构的历史（指包含大量有用的依赖库），
日期时间模块经常会提到时区，Python 核心
运行时并不包括时区信息。这是因为
时区更新没有固定的时间表，并受制于
政治和立法上的奇思妙想。日历版本为这个用其他方法会混乱的系统
提供了日期标记的快照。

[pytz]: https://pypi.python.org/pypi/pytz
[iana_tz]: https://www.iana.org/time-zones

## Teradata

<img src="https://img.shields.io/badge/calver-YY.MM.MINOR.MICRO-22bfda.svg" />

**[Teradata UDA client][teradata_uda]** 提供了[下一代
访问][uda_blog] [Teradata][teradata] 的数据仓库技术。

Teradata 的使用并非以技术或公司的突出而著称，
而是由于在 2016 年发布了多个版本号为 `15.10`
 的版本。这可能在最初看来似乎是破坏性的，但是
意义和作用是显而易见的。

库的维护者们精心打造了一个资源丰富的混合型的
[语义化版本][semver] 和日历化版本。**YY.MM**
版本部分被用作组合的 SemVer 主要版本。这
意味着新版本库的 API 仍然与 2015 年 10 月的
相同。此后编写的依赖代码是可以
安全升级的。我们会在下一次破坏性的 API 变化时看到
年份与月份部分的更新。

[teradata]: http://www.teradata.com/
[teradata_uda]: https://pypi.python.org/pypi/teradata
[uda_blog]: https://developer.teradata.com/tools/reference/teradata-python-module
[semver]: https://semver.org/lang/zh-CN/

## 其他值得注意的项目

* [Unity][unity] - **`YYYY.MINOR.MICRO`** - 跨平台的游戏引擎。
* [pip][pip] - **`YY.MINOR.MICRO`** - Python 官方软件包管理器。
* [PyCharm][pycharm] - **`YYYY.MINOR.MICRO`** - 一个领先的 Python IDE。
* [OpenSCAD][openscad] - **`YYYY.0M`** - 提供实体三维 CAD 建模的
  领先开源软件。
* [fusefs-ntfs][fusefs-ntfs] - **`YYYY.MM.DD_MICRO`** - 为 Unix
  提供最早且最兼容的 NTFS 访问层
  之一。
* [certifi][certifi] - **`YYYY.MM.DD`** - certifi 是一个
  Mozilla 证书授权包的封装，用于保护互联网
  通信。与 [pytz](#pytz) 类似，证书更新没有
  固定的时间表，但及时的、有日期的更新对于安全是
  至关重要的。
* [boltons][boltons] - **`YY.MINOR.MICRO`** - 一个含有许多实用程序的库，
  是对 Python 标准库的补充。

[unity]: https://unity3d.com/unity/whats-new/
[pycharm]: https://www.jetbrains.com/pycharm/download/
[fusefs-ntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[openscad]: http://www.openscad.org/
[certifi]: https://pypi.python.org/pypi/certifi
[boltons]: http://boltons.readthedocs.io/en/latest/
[pip]: https://pip.pypa.io/en/stable/news/


参见 [用户页面][users] ([中文](/users_zhcn.html)) 以获取越来越多的 CalVer 用户列表。

[users]: /users.html

# 何时使用 CalVer

如果你和你不认识的人都严肃地使用你的项目，那么
使用一个严肃的版本。幸运的是，为那个版本决定是否使用 CalVer
比以往任何时候都要容易。

* 你的项目是否具有较大或不断变化的范围？
    * 大型系统和框架，如 [Ubuntu](#ubuntu) 和 [Twisted](#twisted)。
    * 无定形的实用程序集，比如 [Boltons](#其他值得注意的项目)。
* 你的项目是否对时间敏感？是否有其他的外部变化
  驱动项目新版本的发布？
    * 业务需求，例如 [Ubuntu](#ubuntu) 对支持计划的支持。
    * 安全更新，例如 [certifi](#其他值得注意的项目) 对证书更新的需求。
    * 政治变化，例如 [pytz](#pytz) 对时区变化的处理。

如果你对这些问题中的任何一个回答是肯定的，CalVer 的语义就会使
它成为你项目的有力选择。
