# Iniciando projeto

Instalação do python já realizada python3.8 ou superior

```bash
pip install Django=3.0.7
```

ps: avaliar se não haverá conflitos entre os pacotes

## Iniciar VENV

```bash
python3 -m venv .venv
```

Ativar venv

```bash
source .venv/bin/activate
```

Instalar django

```bash
pip install django
```

## Iniciar setup django

```bash
django-admin startproject setup .
```

Alterando timezone.

setup/settings.py

```bash
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

## Criando um APP

```bash
python manage.py startapp transactions # nome do seu app
```

## Rest Framework Configuration

Instalação

```bash
pip install djangorestframework
pip install markdown
```

## Adicionar Framework em Apps

```python
# setup/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```
