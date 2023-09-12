# Navigation

## [`01 <- `](https://github.com/liquidcarbon/FastAPI-Slowly/tree/01)**`02`**[` -> 03`](https://github.com/liquidcarbon/FastAPI-Slowly/tree/03)

# 02. Poetry setup

```bash
a@SNAVVV:~/code/FastAPI-Slowly$ git checkout -b 02
a@SNAVVV:~/code/FastAPI-Slowly$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [fastapi-slowly]:
Version [0.1.0]:
Description []:  Code-along for creating data apps with FastAPI and friends.
Author [liquidcarbon <akscrps@gmail.com>, n to skip]:
License []:
Compatible Python versions [^3.11]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "fastapi-slowly"
version = "0.1.0"
description = "Code-along for creating data apps with FastAPI and friends."
authors = ["liquidcarbon <akscrps@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes
a@SNAVVV:~/code/FastAPI-Slowly$
a@SNAVVV:~/code/FastAPI-Slowly$
a@SNAVVV:~/code/FastAPI-Slowly$ poetry add fastapi uvicorn gunicorn
Creating virtualenv fastapi-slowly-OYpz3Sn0-py3.11 in /home/a/.cache/pypoetry/virtualenvs
Using version ^0.103.1 for fastapi
Using version ^0.23.2 for uvicorn
Using version ^21.2.0 for gunicorn

Updating dependencies
Resolving dependencies... (0.6s)

Package operations: 14 installs, 0 updates, 0 removals

  • Installing idna (3.4)
  • Installing sniffio (1.3.0)
  • Installing typing-extensions (4.7.1)
  • Installing annotated-types (0.5.0)
  • Installing anyio (3.7.1)
  • Installing pydantic-core (2.6.3)
  • Installing click (8.1.7)
  • Installing h11 (0.14.0)
  • Installing packaging (23.1)
  • Installing pydantic (2.3.0)
  • Installing starlette (0.27.0)
  • Installing fastapi (0.103.1)
  • Installing gunicorn (21.2.0)
  • Installing uvicorn (0.23.2)

Writing lock file
a@SNAVVV:~/code/FastAPI-Slowly$
a@SNAVVV:~/code/FastAPI-Slowly$
a@SNAVVV:~/code/FastAPI-Slowly$ git status
On branch 02
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        poetry.lock
        pyproject.toml

no changes added to commit (use "git add" and/or "git commit -a")
a@SNAVVV:~/code/FastAPI-Slowly$ poetry version minor
Bumping version from 0.1.0 to 0.2.0
a@SNAVVV:~/code/FastAPI-Slowly$ git add .
a@SNAVVV:~/code/FastAPI-Slowly$ git commit -m "poetry add fastapi uvicorn gunicorn"
[02 cc6c02a] poetry add fastapi uvicorn gunicorn
 3 files changed, 357 insertions(+), 28 deletions(-)
 rewrite README.md (97%)
 create mode 100644 poetry.lock
 create mode 100644 pyproject.toml
a@SNAVVV:~/code/FastAPI-Slowly$ git push -u origin 02
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 8.69 KiB | 8.69 MiB/s, done.
Total 5 (delta 1), reused 0 (delta 0)
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
remote:
remote: Create a pull request for '02' on GitHub by visiting:
remote:      https://github.com/liquidcarbon/FastAPI-Slowly/pull/new/02
remote:
To https://github.com/liquidcarbon/FastAPI-Slowly.git
 * [new branch]      02 -> 02
Branch '02' set up to track remote branch '02' from 'origin'.
```

---

## [`01 <- `](https://github.com/liquidcarbon/FastAPI-Slowly/tree/01)**`02`**[` -> 03`](https://github.com/liquidcarbon/FastAPI-Slowly/tree/03)