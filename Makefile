# App
run-server:
	@python manage.py runserver

# Test
test:
	@python manage.py test

# Lint
APPS= transactions

clean:
	@find . -name "*.pyc" | xargs rm -rf
	@find . -name "*.pyo" | xargs rm -rf
	@find . -name "*.log" | xargs rm -rf
	@find . -name "__pycache__" -type d | xargs rm -rf
	@find . -name ".pytest_cache" -type d | xargs rm -rf
	@rm -f .coverage
	@rm -rf htmlcov/
	@rm -f coverage.xml
	@rm -f *.log


flake8:
	@flake8 --show-source ./transactions

deadfixtures:  ## Checks dead fixtures
	@pytest --dead-fixtures ./transactions

check-python-import:
	isort $(APPS) --check-only --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

fix-python-import:
	isort $(APPS) --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=88 -l 79

black:
	black $(APPS) --line-length 79 -t py37 --skip-string-normalization

black-check:
	black $(APPS) --line-length 79 -t py37 --skip-string-normalization --check

lint: clean fix-python-import black flake8

check-lint: check-python-import black-check flake8

# Persistencia

create-migrations: ## Create migrations
	@python manage.py makemigrations

migrate-tables:
	@python manage.py migrate


# Infraestrutura

docker-build:  ## Builds the docker environment
	docker-compose build db

docker-up:  ## Start docker containers in daemon mode
	docker-compose up -d

docker-down:  ## Stop docker containers
	docker-compose down
