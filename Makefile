.PHONY: test lint black build publish

default: lint

test:
	poetry run coverage run -m pytest

lint: pyright black

pyright:
	poetry run pyright --verbose

black:
	poetry run black --check --diff --color .

build:
	poetry build

publish:
	poetry publish