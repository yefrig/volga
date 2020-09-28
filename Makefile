.PHONY: lint black build

default: black lint

lint: ## check style with flake8
	flake8 volga tests

black:
	black .

build:
	poetry build

publish:
	poetry publish