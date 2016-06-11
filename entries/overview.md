---
title: Calendar Versioning
publish_date: March 25, 2016
---

Software versioning is important.

Without versioning, we would not be able to discuss software's past or
plan software's future. For engineers, versioning allows us to specify
precise dependencies within ever-expanding software ecosystems. For
marketers, the version is the dynamic part of the project's brand. For
all of us, software versioning lets us reference the past while
upgrading to the future.

<!-- Developers who do not design their versioning scheme to match
their project are leaving valuable communication capital on the
table. -->

Different software projects use different systems for versioning, but
some common practices have emerged. Numeric, decimal point separation,
e.g., 3.1.4, is all but assumed. Another common versioning pattern to
emerge involves incorporating a time-based element, usually part of
the release date, into the version.

This date-based approach has come to be called Calendar Versioning, or
CalVer for short.

# Schemes

There are multiple CalVer schemes, long used by projects big and
small. Rather than selecting a single scheme as CalVer, it's important
to recognize the practicality of each and choose the scheme on a
per-project basis.

* **Major** - The first number in the version. 2 and 3 are Python's famous
  major versions. In calendar versioning, this is most commonly the
  year.
* **Minor** - The second number in the version. 7 is the most popular
  Python minor version.
* **Micro** - The third and usually final number in the version. Sometimes
  referred to as "patch".
* **Modifier** - An optional text tag, such as "dev", "alpha", "beta",
  "rc1", and so on.

The vast majority of modern software versions are composed of two or
three numeric segments, plus the optional modifier. Convention
suggests that four-numeric-segment versions are discouraged.

As seen in the list of real-world examples below, projects have found
more than one useful way to use dates in their versions. Rather than
choose a single scheme, CalVer introduces standard terminology for
users, based on researching current practice.

* YYYY - Full year (four-digit)
* YY - Short year (two-digit)
* MM - Short month (e.g., 1, 2, 3 ... 10, 11, 12)
* 0M - Zero-padded month (e.g., 01, 02, 03 ... 10, 11, 12)
* DD - Short day
* 0D - Zero-padded day

Note that traditional, incremented version numbers are 0-based, but
these date segments are 1-based.

The Gregorian calendar is assumed, as is the convention of
UTC. Technically any calendar can be used, provided projects state
which one.

# Case studies

## Ubuntu

**`YY.0M.MICRO`** - [Link](http://www.ubuntu.com)

Three-segment, short year, zero-padded month.

## Twisted

**`YY.MINOR.MICRO`** - [Link](https://twistedmatrix.com)

Three-segment, short year.

## youtube_dl

**`YYYY.0M.0D`** - [Link](https://rg3.github.io/youtube-dl/)

Three-segment, full year, zero-padded month, zero-padded day. In some
contexts the version adds a fourth segment for MICRO.

## pytz

**`YYYY.MM`** - [Link]()

## certifi

**`YYYY.MM.DD`** - [Link]()

## Teradata

**YY.MM.MINOR.MICRO** - [Link](https://pypi.python.org/pypi/teradata)

Notable because there have been multiple releases in 2016 which were
versioned as *15.10.\**. This may seem breaking at first, but the
meaning and utility is clear.

In effect, the library has crafted a resourceful hybrid of semantic
versioning and calendar versioning. The **YY.MM** part of the version
are used as a combined SemVer major version. That is, for new
releases, the API of the library remains the same as it did in October
2015. Dependent code written since then is safe to upgrade.  We will
see the year and month segments update next time there is a breaking
API change.


## Other notable projects

* [fusefs-ntfs]() - **YYYY.MM.DD_MICRO**
* [OpenSCAD]() - **YYYY.0M** - Two-segment. Full year, zero-padded month.

# When to use CalVer

For those seeking straight answers to the version design question, the
wait is over. In the end the decision is the project developer's, but
here are the questions to be asking:

* Is your project large or all-encompassing?
    * Large frameworks, like Twisted.
    * Amorphous sets of utilities, like Boltons.
* Is your project time-sensitive in any way? Are external changes a
  primary driver of new project releases?
    * Business requirements, such as Ubuntu's focus on support schedules.
    * Security updates, such as certifi's need to update certificates.
    * Political shifts, such as pytz's handling of timezone changes.

If you answered yes to any of these questions, CalVer's semantics may
make it a strong choice for your project.
