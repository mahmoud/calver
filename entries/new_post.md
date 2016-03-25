---
title: A New Post
publish_date: May 6th, 2015
tags:
  - meta
  - reference
---

This is a brand new post just waiting to be filled out by a willing
author. Features abound, so in addition to staving off slate
blankness, this post acts as a quick-start reference.

<!-- HTML comments are the preferred comment syntax for markdown -->
<!-- Note that the title of the post is conventionally prepended as an h1-level heading by the theme -->

[TOC]

This entry is probably a bit on the short side for a table of
contents, but Chert makes it easy to add one like the one above.
Simply include `[TOC]` in your entry, wherever you'd like the Contents
to appear. Also note that regardless of whether a table of contents is
generated, headings always link to themselves, making anchor retrieval
and navigation even more convenient.

# Definition lists and footnotes

Chert supports all the standard Markdown features, plus tables of
contents, footnotes[^note], and definition lists:

Python
:   A constricting snake belonging to the family [Pythonidae][pythonidae].
:   A high-level, multi-purpose programming language, used to generate this site.

Chert
:   [A sedimentary rock][chert_rock] historically used to start fires.
:   An open-source static site generator, used to generate this site.

[^note]: Footnotes can be great for citations or when you're tired of
using parentheses. They are automatically placed at the bottom of the
entry.

# Headings
Chert supports heading levels galore, with all headings anchor linked
to themselves. Five levels of headings to keep your content company.
## Subheading 2
### Subheading 3
#### Subheading 4
##### Subheading 5

# Code highlighting

Finally, it's time for that very special and very ubiquitous code snippet,
with highlighting provided by [pygments][pygments]:

<!-- python is actually the default for code highlighting -->

```python hl_lines="1"
# line highlighting is also supported
def greet(name):
    print('Hello, %s!' % name)

# Prints the greeting to sys.stdout
greet('world')
```

**Hello, world!** And enjoy using Chert!

[pythonidae]: https://en.wikipedia.org/wiki/Pythonidae
[chert_rock]: https://en.wikipedia.org/wiki/Chert
[pygments]: http://pygments.org/
