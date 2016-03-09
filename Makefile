.PHONY: tests devinstall cleanpyc
APP=src/
COV=banter
OPTS=


help:
	@echo "tests - run tests"
	@echo "devinstall - install all packages required for development"
	@echo "cleanpyc - cleanup pyc files"

tests:
	py.test ${OPTS} ${APP}


devinstall:
	pip install --upgrade pip setuptools wheel
	pip install -e .
	pip install -r resources/requirements-develop.txt


cleanpyc:
	find . -name "*.py[co]" -delete