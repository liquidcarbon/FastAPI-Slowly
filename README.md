# Navigation

## [`02 <- `](https://github.com/liquidcarbon/FastAPI-Slowly/tree/02)**`03`**[` -> 04`](https://github.com/liquidcarbon/FastAPI-Slowly/tree/04)


# 03. Start app with gunicorn

```bash
a@SNAVVV:~/code/FastAPI-Slowly$ git checkout -b 03
Switched to a new branch '03'
a@SNAVVV:~/code/FastAPI-Slowly$ mkdir fastapi_slowly
a@SNAVVV:~/code/FastAPI-Slowly$ touch fastapi_slowly/api.py
a@SNAVVV:~/code/FastAPI-Slowly$ touch gunicorn.conf.py
a@SNAVVV:~/code/FastAPI-Slowly$ DIR=/home/a/code/FastAPI-Slowly/; poetry run --directory $DIR gunicorn fastapi_slowly.api:app --reload -D
```

![Step 03 - gunicorn](image.png)

---

## [`02 <- `](https://github.com/liquidcarbon/FastAPI-Slowly/tree/02)**`03`**[` -> 04`](https://github.com/liquidcarbon/FastAPI-Slowly/tree/04)
