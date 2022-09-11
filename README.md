[![PyPI Version](https://img.shields.io/pypi/v/monkeytale.svg?style=for-the-badge)](https://pypi.org/project/monkeytale)
[![Release Date](https://img.shields.io/github/release-date/MLAOPDX/monkeytale?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/releases)
[![License](https://img.shields.io/github/license/MLAOPDX/monkeytale.svg?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/blob/main/LICENSE)

[![Issues](https://img.shields.io/github/issues/MLAOPDX/monkeytale.svg?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/MLAOPDX/monkeytale?style=for-the-badge)](https://github.com/MLAOPDX/monkeytale/pulls)
[![Code Quality Alerts](https://img.shields.io/lgtm/alerts/github/MLAOPDX/monkeytale?style=for-the-badge)](https://lgtm.com/projects/g/MLAOPDX/monkeytale/alerts/?mode=list)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/github/MLAOPDX/monkeytale?style=for-the-badge)](https://lgtm.com/projects/g/MLAOPDX/monkeytale/context:python)

# Monkeytale

> "The book is a program." from [Pollen](https://docs.racket-lang.org/pollen/big-picture.html) by Matthew Butterick

Monkeytale is a markup language for documenting and composing a story world and its novels. I am building this language to improve insight into my own writing and to learn more about software development.

Monkeytale plugins will use the structured writing content to generate things like Word documents for editor submissions and Vellum imports. I also intend to create plugins that generate visualizations like these.

```mermaid
flowchart TB
    BEGIN[/"Begin Manuscript Title"\]
    END[\"End Manuscript Title"/]

    subgraph PoV1 ["<b>@Protagonist"</b>]
        SN2(["<b><u>The waves crumbled into a hiss</u></b>\n#PermiflangeCoast\n\nA scene outline wrapped at a decent length\nas not to stretch the  Scene box too wide."])
        SN3([SceneName])
        SN8([SceneName])
    end

    subgraph PoV2 ["<b>@Antagonist</b>"]
        SN4([<b><u>After the full moon shatters</u></b>\n#WoodedLands])
        SN6([SceneName])
    end

    BEGIN ====> SN2
    
    SN2 ==narrative\norder==> SN3 ==> SN4 ==> SN6 ==> SN8

    SN8 ====> END
    
    SN2 -.non-narrative\nrelation.-> SN6
    SN8 -.-> SN3
```

## Design Principles

- The book is a program.
- Document for others to use.
- Simplicity ensures durability.

### The Book Is A Program
Monkeytale lives where I write, in [Workflowy](https://workflowy.com), a multi-platform outliner. Monkeytale will process OPML exports of Workflowy content.

### Document for others to use.
Monkeytale only collects information about the writing, so that plugins can report on the information collected. Those plugins can compose, visualize, opine, or even rewrite your work.

### Simplicity ensures durability.
Monkeytale requires only the installation of git, has minimal configuration, and maximum extensibility. This makes changing Monkeytale functionality both more difficult and powerful.

## 
4. Generate ToDoTree configuration in .vscode/settings.json to help navigate story structure
5. Generate import file(s) for Aeon Timeline software to help visualize a story world

## Dismissed Functionality
- Advice on how to improve or correct the writing
- Typography and formatting, other than emphasis/thought (italics)
- Tables of content and indexing
- Goal tracking

## Design Decisions
- [Workflowy](https://workflowy.com) as writing platform. The content used by Monkeytale will need to meet certain structural requirements, a template of which is [shared from Workflowy](https://workflowy.com/s/world-template-dupli/3Tj4vp9gsIXYGZaT).
- [Python 3](https://www.python.org/) will be the programming language for Monkeytale and any plugins that folks might want to build
- [Github Repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) as the [quick start template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).
- [Github Actions](https://github.com/features/actions) as execution platform, so nothing will have to be installed on the user's system other than [Github Desktop](https://desktop.github.com/).

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
