---
created:
  - 2026-04-14T13:37
modified: 2026-04-14 16:04
tags:
  - python
  - app
  - dev
  - software
  - software-development
  - distribution
  - package-management
  - pip
  - pypi
  - repository
  - install
type:
  - note
status:
  - in-progress
---
## Project Layout

`uv init` sets up the project structure:

```
.
├── README.md
├── pyproject.toml
└── src
    └── your_app_name
        ├── __init__.py
        └── py.typed     # only created when using `uv init --lib`
```

`uv init --package` and `uv init --lib` are only very slightly different:

| Aspect                                        | --package | --lib |
| --------------------------------------------- | --------- | ----- |
| src/ layout                                   | ✅         | ✅     |
| adds build system to `pyproject.toml`         | ✅         | ✅     |
| includes `py.typed`                           |           | ✅     |
| includes a CLI entrypoint in `pyproject.toml` | ✅         |       |


## References
* https://docs.astral.sh/uv/reference/cli/#uv-init
## Related
* Links to other notes which are directly related go here