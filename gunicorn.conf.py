# ./gunicorn.conf.py

# launch like so:
# DIR=/path/to/this/repo/
# poetry run --directory $DIR gunicorn fastapi_slowly.api:app --reload -D
#
# to terminate the daemonized process enabled by the -D option, use `pkill gunicorn`


import signal
import os

bind = "0.0.0.0:7890"
worker_class = "uvicorn.workers.UvicornWorker"
workers = 1

capture_output = True
errorlog = "gunicorn.log"
loglevel = "debug"
timeout = 300


def worker_int(worker):
    os.kill(worker.pid, signal.SIGINT)
