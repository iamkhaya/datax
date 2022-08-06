
checkfiles = datax/ tests/ setup.py
devenv = PYTHONPATH=.


help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    up          Updates dev/test dependencies"
	@echo  "    deps        Ensure dev/test dependencies are installed"
	@echo  "    lint	Reports all linter violations"
	@echo  "    test	Runs all tests"
	@echo  "    ci		Runs linter and tests"

up:
	pip install pip
	pip install --upgrade setuptools wheel
	pip install -q pip-tools
	pip-compile -U --no-emit-index-url --no-emit-trusted-host requirements.in
	pip-compile -U --no-emit-index-url --no-emit-trusted-host tests/requirements.in

deps:
	@pip install pip
	@pip install --upgrade setuptools wheel

	@pip install -q pip-tools
	@pip-sync requirements.txt tests/requirements.txt
	@pip install --no-cache-dir -qe  .

isort:
	isort datax tests

lint:
	flake8 $(checkfiles)
	pylint $(checkfiles)
	mypy $(checkfiles)
	python setup.py check -mr

style:
	isort $(checkfiles)
	black $(checkfiles)

test:
	pytest --disable-warnings --cov=datax --cov-report term tests

ci: deps lint test
