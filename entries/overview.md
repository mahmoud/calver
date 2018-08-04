---
title: Calendar Versioning
entry_root: overview
publish_date: May 1, 2017
orig_publish_dat: March 25, 2016
---

*CalVer is a software versioning convention that is based on your
project's release calendar, instead of arbitrary numbers.*

**Software versioning gets better with time.**

For engineers, versioning allows us to specify precise dependencies
within ever-expanding software ecosystems. For marketers, the version
is the dynamic part of a project's brand. For all of us, software
versioning lets us reference the past while also upgrading to the
future.

<!-- Developers who do not design their versioning scheme to match
their project are leaving valuable communication capital on the
table. -->

Different software projects use different systems for versioning, but
some common practices have emerged. Point-separated numbers e.g.,
*3.1.4*, are all but given. Another common versioning pattern
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

* **Major** - The first number in the version. 2 and 3 are Python's famous
  major versions. The major segment is the most common calendar-based component.
* **Minor** - The second number in the version. 7 is the most popular
  minor version of Python 2.
* **Micro** - The third and usually final number in the version. Sometimes
  referred to as the "patch" segment.
* **Modifier** - An optional text tag, such as "dev", "alpha", "beta",
  "rc1", and so on.

The vast majority of modern software versions are composed of two or
three numeric segments, plus the optional modifier. Convention
suggests that four-numeric-segment versions are discouraged.

[designing_a_version]: http://sedimental.org/designing_a_version.html

As seen in the [case studies](#case_studies) below, projects have
found more than one useful way to leverage dates in their
versions. Rather than choose a single scheme, CalVer introduces
standard terminology for developers, based on current practices and
conventions.

* **`YYYY`** - Full year - 2006, 2016, 2106
* **`YY`** - Short year - 6, 16, 106
* **`0Y`** - Zero-padded year - 06, 16, 106
* **`MM`** - Short month - 1, 2 ... 11, 12
* **`0M`** - Zero-padded month - 01, 02 ... 11, 12
* **`DD`** - Short day - 1, 2 ... 30, 31
* **`0D`** - Zero-padded day - 01, 02 ... 30, 31

Note that traditional, incremented version numbers are 0-based,
whereas date segments are 1-based, and the short and zero-padded years
are relative to the year 2000.

The [Gregorian calendar][gregorian] is assumed, as is the convention
of [UTC][utc]. Technically any calendar can be used, provided projects
state which one.

[gregorian]: https://en.wikipedia.org/wiki/Gregorian_calendar
[utc]: https://en.wikipedia.org/wiki/Coordinated_Universal_Time

# Case studies

CalVer has quite a few users. These are projects selected for their
notability and variety of use cases.

## Ubuntu

<img src="https://img.shields.io/badge/calver-YY.0M.MICRO-22bfda.svg" />

**[Ubuntu][ubuntu]**, one of the most prominent Linux-based operating
systems available, uses a three-segment CalVer scheme, with a short
year and zero-padded month. It has done so
[from the very start][ubuntu_releases], in October 2004, making 4.10
the first general release of Ubuntu.

Even a simple operating system involves many, many parts, making it
difficult to communicate much meaning with an arbitrary number. By
dating the software release, the calendar-based version is much more
than an arbitrary number, communicating useful information that is
rooted in simple fact.

Ubuntu derives additional benefit from its CalVer scheme, by
integrating it with their support schedule. Ubuntu currently has
five-year support periods for their long-term support (LTS) releases,
and only 9 months for non-LTS releases. Thanks to CalVer and
elementary arithmetic, any user can easily determine whether their
version is still supported. The current LTS release at the time of
writing, 16.04, will be supported until April 2021.

[ubuntu]: http://www.ubuntu.com/
[ubuntu_releases]: https://en.wikipedia.org/wiki/List_of_Ubuntu_releases

## Twisted

<img src="https://img.shields.io/badge/calver-YY.MM.MICRO-22bfda.svg" />

**[Twisted][twisted]**, the venerated Python networking and
asynchronous execution framework, uses a three-segment CalVer scheme,
with a short year in the major version slot, release number of that year
in the minor slot, and the micro slot being the bugfix release number.

First released in 2002 and still actively developed today, Twisted is
a [mature][twisted_wp] library that has grown to match its large
scope. It features everything from an IRC client to an HTTP server to
a slew of utilities for concurrent programming. Like an operating
system, Twisted has a lot of parts, making SemVer a poor fit due to
the individual parts deprecating and breaking compatibility individually.

The non-deprecated parts of Twisted are backwards-compatible between
each successive version, and breaking changes are done on a time basis,
where one year must pass and two releases issued between the release
deprecating the functionality and the removal of the functionality.

Its versioning scheme has spread to related projects, including
[Klein][klein], [Treq][treq], and even one of Twisted's dependencies,
[PyOpenSSL][pyopenssl].

[twisted]: https://twistedmatrix.com
[twisted_wp]: https://en.wikipedia.org/wiki/Twisted_%28software%29
[klein]: https://github.com/twisted/klein
[treq]: https://github.com/twisted/treq
[pyopenssl]: https://github.com/pyca/pyopenssl

## youtube_dl

<img src="https://img.shields.io/badge/calver-YYYY.0M.0D-22bfda.svg" />

**[youtube_dl][youtube_dl]**, the understated ally of Internet
media archivists everywhere, uses a three-segment CalVer scheme,
including full year, zero-padded month, and zero-padded day. The
version is almost completely calendar-driven, except for a micro
segment that is added in some technical contexts.

Despite the name, youtube_dl's scope is expansive. It supports
extracting audio and video from a long, ever-expanding list of
sites. Consider the rapid release cycle of supported services, and it
becomes clear why the project has adopted CalVer to such a great
degree.

[youtube_dl]: https://rg3.github.io/youtube-dl/

## pytz

<img src="https://img.shields.io/badge/calver-YYYY.MM-22bfda.svg" />

**[pytz][pytz]** is the Python translation of the
[IANA/Olson timezone database][iana_tz], the database behind accurate
times for all of computerdom.  pytz uses a two-segment CalVer scheme,
including full year and short month.

While Python has a history of "batteries-included" architecture, and
the datetime module frequently mentions timezones, the core Python
runtime does not include timezone information. This is because
timezone updates do not follow a fixed schedule, and are subject to
politics and legislative whim. Calendar versioning offers a
date-stamped snapshot of an otherwise chaotic system.

[pytz]: https://pypi.python.org/pypi/pytz
[iana_tz]: https://www.iana.org/time-zones

## Teradata

<img src="https://img.shields.io/badge/calver-YY.MM.MINOR.MICRO-22bfda.svg" />

The **[Teradata UDA client][teradata_uda]** provides [next-generation
access][uda_blog] to [Teradata][teradata]'s data warehousing technologies.

Teradata's usage is notable not for the prominence of the technology
or company, but because there have been multiple releases in 2016
which were versioned as `15.10`. This may seem breaking at first, but
the meaning and utility is clear.

The library maintainers have crafted a resourceful hybrid of
[semantic versioning][semver] and calendar versioning. The **YY.MM**
part of the version are used as a combined SemVer major version. That
is, for new releases, the API of the library remains the same as it
did in October 2015. Dependent code written since then is safe to
upgrade.  We will see the year and month segments update next time
there is a breaking API change.

[teradata]: http://www.teradata.com/
[teradata_uda]: https://pypi.python.org/pypi/teradata
[uda_blog]: https://developer.teradata.com/tools/reference/teradata-python-module
[semver]: http://semver.org/

## Other notable projects

* [boltons][boltons] - **`YY.MINOR.MICRO`** - A broad library of
  utilities supplementing the Python standard library.
* [PyCharm][pycharm] - **`YYYY.MINOR.MICRO`** - A leading Python IDE.
* [OpenSCAD][openscad] - **`YYYY.0M`** - The premiere open-source
  offering for solid 3D CAD modelling.
* [fusefs-ntfs][fusefs-ntfs] - **`YYYY.MM.DD_MICRO`** - One of the
  earliest and most cross-compatible NTFS access layers for Unix
  systems.
* [certifi][certifi] - **`YYYY.MM.DD`** - certifi is a wrapper around
  Mozilla's certificate authority bundle, used for secure Internet
  communication. Similar to [pytz](#pytz), certificate updates do not
  follow a fixed schedule, but timely, dateable updates are critical
  to security.
<!-- * Windows 95, 98, and 2000 - While Ubuntu is undoubtedly the
better operating sytem exemplar, Windows did serve to demonstrate the
branding success of CalVer. Windows 95 simply had a better ring to it
than Windows 3.1.1. -->

[boltons]: http://boltons.readthedocs.io/en/latest/
[pycharm]: https://www.jetbrains.com/pycharm/download/
[fusefs-ntfs]: http://www.freshports.org/sysutils/fusefs-ntfs
[openscad]: http://www.openscad.org/
[certifi]: https://pypi.python.org/pypi/certifi

See the [Users page][users] for a growing list of CalVer users.

[users]: /users.html

# When to use CalVer

If both you and someone you don't know use your project seriously,
then use a serious version. Your project is released, and it needs a
nonzero major version. Luckily, the decision on whether to use CalVer
for that version is easier than ever:

* Is your project large or all-encompassing?
    * Large systems and frameworks, like [Ubuntu](#ubuntu) and [Twisted](#twisted).
    * Amorphous sets of utilities, like [Boltons](#other_notable_projects).
* Is your project time-sensitive in any way? Do other external changes
  drive new project releases?
    * Business requirements, such as [Ubuntu](#ubuntu)'s focus on support schedules.
    * Security updates, such as [certifi](#other_notable_projects)'s need to update certificates.
    * Political shifts, such as [pytz](#pytz)'s handling of timezone changes.

If you answered yes to any of these questions, CalVer's semantics make
it a strong choice for your project.
