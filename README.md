[![PyPI Version](https://img.shields.io/pypi/v/monkeytale.svg?style=for-the-badge)](https://pypi.org/project/monkeytale)
[![Release Date](https://img.shields.io/github/release-date/MLAOPDX/monkeytale?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/releases)
[![License](https://img.shields.io/github/license/MLAOPDX/monkeytale.svg?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/blob/main/LICENSE)

[![Issues](https://img.shields.io/github/issues/MLAOPDX/monkeytale.svg?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/MLAOPDX/monkeytale?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/pulls)
[![Code Quality Alerts](https://img.shields.io/lgtm/alerts/github/MLAOPDX/monkeytale?style=for-the-badge)](https://lgtm.com/projects/g/MLAOPDX/monkeytale/alerts/?mode=list)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/github/MLAOPDX/monkeytale?style=for-the-badge)](https://lgtm.com/projects/g/MLAOPDX/monkeytale/context:python)

# Monkeytale

> "The book is a program." --- [Pollen](https://docs.racket-lang.org/pollen/big-picture.html) by Matthew Butterick

Monkeytale is a markup language for documenting and composing a story world and its novels. I am building it to improve insight into my own writing and to learn more about software development.

Plugins will use Monkeytale's structured writing content to generate things like Word documents for editor submissions or scene flows like this:

```mermaid
flowchart TB
    BEGIN[/"<b>MANUSCRIPT TITLE</b>"\]
    END[\"<b>MANUSCRIPT TITLE</b>"/]

    subgraph PoV1 ["<b>@Protagonist"</b>]
        SN2(["<b><u>The crumbling wave</u></b>\n#PermiflangeCoast\n\nA scene outline wrapped at a decent length\nas not to stretch the Scene box too wide."])
        SN3([<b><u>SceneName</u></b>])
        SN8([<b><u>SceneName</u></b>])
    end

    subgraph PoV2 ["<b>@Antagonist</b>"]
        SN4([<b><u>After the full moon sinks</u></b>\n#WoodedLands])
        SN6([<b><u>SceneName</u></b>])
    end

    BEGIN ====> SN2
    
    SN2 =="narrative\norder\n(time gap?)"==> SN3 ==> SN4 ==> SN6 ==> SN8

    SN8 ====> END
    
    SN2 -."non-narrative relation\nlike foreshadow".-> SN6
    SN8 -."flashback".-> SN3
```

## Design Principles

- Derive as much as possible from the text itself before adding in syntax.
- Document what is written, let plugins report on the structure and content, and then gather the results.
- Set up and forget.

## Decisions

Monkeytale syntax lives in [Workflowy](https://workflowy.com), a multi-platform outliner. An OPML export of Workflowy content will be given to the Monkeytale parser, which in turn will pass the generated structure and content on to each installed plugin.

- Monkeytale needs to work without installing any software on the user's system other than a browser, which is assumed to be already present.
- [Workflowy](https://workflowy.com) as writing platform. Workflowy supports multi-platform, offline editing.
- [Github](https://github.com) as the store for exported OPML and the associated Monkeytale plugin outputs. Github supports multi-platform offline storage to read or backup the Monkeytale plugin output.
- [Github Actions](https://github.com/features/actions) as execution platform, so nothing will have to be installed on the user's system other than [Github Desktop](https://desktop.github.com/). There is no offline alternative to refresh the Monkeytale plugin output.
- [Github Repo Templates](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) as the [quick start template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
- [Python 3](https://www.python.org/) as the programming language for Monkeytale and any plugins that folks might want to build.

## Development

[![GitHub top language](https://img.shields.io/github/languages/top/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../)
[![https://img.shields.io/pypi/pyversions/monkeytale?style=for-the-badge](https://img.shields.io/pypi/pyversions/monkeytale?style=for-the-badge)](https://pypi.org/project/monkeytale)
[![Last commit](https://img.shields.io/github/last-commit/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../commits/master)
[![Commit activity](https://img.shields.io/github/commit-activity/m/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../commits/master)
[![PyPI Downloads](https://img.shields.io/pypi/dm/monkeytale.svg?style=for-the-badge)](https://pypistats.org/packages/licensecheck)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fmonkeytale)](https://pepy.tech/project/monkeytale)

Monkeytale is developed in my spare time and uses [Semantic Versioning](https://semver.org/) and [Semantic Release](https://pypi.org/project/python-semantic-release/) to track its, equally spare, progress.

As per Semantic Versioning: "Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable."

Check the [change log](https://github.com/MLAOPDX/monkeytale/blob/main/CHANGELOG.md) for the latest updates.
