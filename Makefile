.PHONY: test lint black build publish

default: black lint

test:
	poetry run pytest

black:
	poetry run black --check .

lint:
	poetry run flake8 volga tests

build:
	poetry build

publish:
	poetry publish