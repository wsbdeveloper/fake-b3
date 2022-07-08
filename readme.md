## Run server admin.

```bash
django-admin runserver --pythonpath=. --settings="singed.settings"
```

## Gunicorn

```bash
gunicorn -c conf/gunicorn_conf.py ms_singed.wsgi
```
