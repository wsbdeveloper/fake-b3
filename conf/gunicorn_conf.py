import os

command = "/.venv/bin/gunicorn"
pythonpath = os.getenv("SINGED_PATH", "")
bind = "localhost:8000"
workers = 2
