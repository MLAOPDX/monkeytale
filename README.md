# Monkeytale
[![PyPI Version](https://img.shields.io/pypi/v/monkeytale.svg?style=for-the-badge)](https://pypi.org/project/monkeytale)
[![License](https://img.shields.io/github/license/MLAOPDX/monkeytale.svg?style=for-the-badge)](/LICENSE.md)

[![Issues](https://img.shields.io/github/issues/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../issues)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/github/MLAOPDX/monkeytale?style=for-the-badge)](https://lgtm.com/projects/g/MLAOPDX/monkeytale/context:python)

> "The book is a program." - from [Pollen](https://docs.racket-lang.org/pollen/big-picture.html) by Matthew Butterick

Monkeytale is a markup language for documenting and composing a story world and its novels. I am building this language to improve insight into my own writing.

## Design Principles

To stay honest in the application of these principles, here's a useful bit to keep in mind:

> Special cases aren't special enough to break the rules, although practicality beats purity. - from [The Zen of Python](https://peps.python.org/pep-0020/) by Tim Peters

- **The book is a program.**</br>Monkeytale lives within your manuscript, within your notes, where you work.
- **Don't opine. Document.**</br>Monkeytale does not give advice on how to improve your writing. It's job is to collects information about your writing, so you can decide if and where work is needed.
- **Keeping it simple makes it durable.**</br>Monkeytale has a minimal syntax, no configuration, and uses flat text files.

## Planned Functionality

### Monkeytale
This will be the true Monkeytale functionality, the result of which is exposed to the plugins, for them to generate different outputs.
- Compose multiple narratives by (re-)using story components
- Derive story structure from story components and their content
- Provide plugin mount point for generation of documents from story structure extracted by Monkeytale
- Execute from continuous integration server

### Plugin
The intent is that anyone could write a plugin and make it available through PyPI and Monkeytale could make use of it. How to tell Monkeytale which plugins to use without configuration will be a challenge.

- Navigate to any named story component
- Generate Markdown of each manuscript
- Generate flow chart of scenes across PoV characters for each manuscript
- Generate Markdown for all characters

## Dismissed Functionality
- Advice on how to improve or correct the writing
- Typography and formatting, other than emphasis (italics)
- Tables of content and indexing
- Project management and goal tracking (maybe when hard writing deadlines ever become a reality for me)

## Design Decisions
- [Python 3](https://www.python.org/) will be the programming language for Monkeytale and the hooks for any plugins that folks might want to build
- [Github Actions](https://github.com/features/actions) using Linux as execution platform
- [Github Repo Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) as the delivery system.
- Use .@ as the file extension to indicate Monkeytale files.
- Single global namespace

## My environment of choice
- [Visual Studio Code](https://code.visualstudio.com/) (VSCode) will be the text editor of choice
- [GruntFuggly's ToDoTree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) extension for VS Code will be used to support navigation. Will need a plugin that updates ToDoTree configuration as needed.
- [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) extension for Markdown and Mermaid diagram display and conversion to docx using [PanDoc](https://pandoc.org/) and PDF using Safari.

## Development Progress

[![Last commit](https://img.shields.io/github/last-commit/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../commits/master)
[![Commit activity](https://img.shields.io/github/commit-activity/m/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../commits/master)
[![https://img.shields.io/pypi/pyversions/monkeytale?style=for-the-badge](https://img.shields.io/pypi/pyversions/monkeytale?style=for-the-badge)](https://pypi.org/project/monkeytale)
[![GitHub top language](https://img.shields.io/github/languages/top/MLAOPDX/monkeytale.svg?style=for-the-badge)](../../)

[![PyPI Downloads](https://img.shields.io/pypi/dm/monkeytale.svg?style=for-the-badge)](https://pypistats.org/packages/licensecheck)
[![PyPI Total Downloads](https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=total%20downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fmonkeytale)](https://pepy.tech/project/monkeytale)

Monkeytale is developed in spare time and uses [Semantic Versioning](https://semver.org/) and [Semantic Release](https://pypi.org/project/python-semantic-release/) to track its, equally spare, progress.

As per Semantic Versioning: "Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable."

Check the [change log](https://github.com/MLAOPDX/monkeytale/blob/main/CHANGELOG.md) for the latest updates.
