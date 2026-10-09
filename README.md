# CalVer

<img height=300 align=right
src="https://raw.githubusercontent.com/mahmoud/calver/master/uploads/caltree_med.png">

CalVer is a project versioning convention based on calendar dates of
project releases, instead of arbitrary numbers. There are
[many benefits][designing_a_version] to this approach, and
[multiple variations][calver_overview] to custom fit all projects,
from [Ubuntu][ubuntu] to [Twisted][twisted] to [PyCharm][pycharm] to
[C][c] itself and [more][calver_users].

Adopting CalVer with a coding agent? Point it at
[`skills/calver-adoption`](skills/calver-adoption/SKILL.md), a skill
that detects the current version, picks a scheme, writes the docs
paragraph, and cuts the first release.

[ubuntu]: http://calver.org/overview.html#ubuntu
[twisted]: http://calver.org/overview.html#twisted
[pycharm]: http://calver.org/overview.html#other-notable-projects
[c]: http://calver.org/users.html#languages-and-standards

[designing_a_version]: http://sedimental.org/designing_a_version.html
[calver_overview]: http://calver.org/overview.html
[calver_users]: http://calver.org/users.html

## Contributing

If you have questions, comments, issues, or enhancements, please feel
free to [open an issue][issue].

calver.org is generated with [Chert][chert] and [Python][python]. So,
if you would like to submit a pull request directly, `pip install
chert` and `chert serve` from within the repo directory to get a
live-updating preview of what your change will look like.

[issue]: https://github.com/mahmoud/calver/issues

[chert]: https://github.com/mahmoud/chert
[python]: http://python.org
