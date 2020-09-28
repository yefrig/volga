.PHONY: test lint black build publish

default: black lint

test:
	poetry run pytest

lint: ## check style with flake8
	flake8 volga tests

black:
	black .

build:
	poetry build

publish:
	poetry publish