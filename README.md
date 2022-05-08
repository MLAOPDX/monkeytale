# Monkeytale v0.2.0

> "The book is a program." - [Matthew Butterick](https://docs.racket-lang.org/pollen/big-picture.html)

Monkeytale is a markup language for composing, documenting, and visualizing a novel from flat files. I am building it to meet my needs and, thus, it will be opinionated to a fault.

## Design Principles
- All information lives within the writing
- World and story structure are independent of file and folder structure
- Only flat text files
- Simple and consistent syntax
- No configuration

## Planned Functionality
- Compose one or multiple narratives from story components
- Navigate to any named story component
- Execute from continuous integration server
- Derive story structure knowledge from story components and their content
- Provide plugin mount point for generation of documents from Monkeytale story components
  - Word documents for editor-ready manuscripts and import into [Vellum](https://vellum.pub/)
  - Comma-separated files for import into [Aeon](https://timeline.app/)

## Dismissed Functionality
- Advice on how to improve or correct the writing
- Typography and formatting, other than emphasis (italics)
- Tables of content and indexing
- Stuff other folks have done better (e.g. VS Code, ToDoTree, Vellum, Aeon)

## Development Progress
Monkeytale is developed in spare time and uses [Semantic Versioning](https://semver.org/) and [Semantic Release](https://pypi.org/project/python-semantic-release/) to track its, equally spare, progress.

As per Semantic Versioning: "Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable."

Check the [change log](https://github.com/MLAOPDX/monkeytale/blob/main/CHANGELOG.md) for the latest updates.

## Decisions
- [Python 3](https://www.python.org/) will be the programming language
- [Visual Studio Code](https://code.visualstudio.com/) (VSCode) will be the text editor of choice
- [GruntFuggly's ToDoTree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree) extension for VS Code will be used to support navigation
- [Github Actions](https://github.com/features/actions) as execution platform
- Use .@ as the file extension to indicate Monkeytale files
