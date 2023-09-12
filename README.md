# Navigation

## [`04 <- `](https://github.com/liquidcarbon/FastAPI-Slowly/tree/04)**`05`**[` -> 06`](https://github.com/liquidcarbon/FastAPI-Slowly/tree/06)


# 05. Add API version to response

```bash
a@SNAVVV:~/code/FastAPI-Slowly$ git checkout -b 05
Switched to a new branch '05'
a@SNAVVV:~/code/FastAPI-Slowly$ touch fastapi_slowly/version.py
a@SNAVVV:~/code/FastAPI-Slowly$ python -c 'from fastapi_slowly.version import get_version; print(get_version())'
0.4.0
a@SNAVVV:~/code/FastAPI-Slowly$ poetry version minor
Bumping version from 0.4.0 to 0.5.0
a@SNAVVV:~/code/FastAPI-Slowly$ python -c 'from fastapi_slowly.version import get_version; print(get_version())'
0.5.0
a@SNAVVV:~/code/FastAPI-Slowly$ git status
On branch 05
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md
        modified:   fastapi_slowly/api.py
        modified:   image.png
        modified:   pyproject.toml

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        fastapi_slowly/version.py
```

![Step 05 - respond with version](image.png)

---

## [`04 <- `](https://github.com/liquidcarbon/FastAPI-Slowly/tree/04)**`05`**[` -> 06`](https://github.com/liquidcarbon/FastAPI-Slowly/tree/06)
