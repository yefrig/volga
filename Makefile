.PHONY: test lint black build publish

default: lint

test:
	poetry run coverage run -m pytest

lint: mypy black flake8 pylint

mypy:
	poetry run mypy --strict volga tests

black:
	poetry run black --check .

flake8:
	poetry run flake8 volga tests 

pylint:
	poetry run pylint volga tests

build:
	poetry build

publish:
	poetry publish