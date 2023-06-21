.ONESHELL:
default: help
PHONY: install check test setup-env install-pre-commit-hook bootstrap help
ENVIRONMENT ?= dev


install:
	ENVIRONMENT="{$(ENVIRONMENT) | tr -d \'[:blank:]\'}";\
	if [[ "${ENVIRONMENT}" ]]; then
		python -m pip install .[$(ENVIRONMENT)];\
	else
		python -m pip install .;\
	fi

check:
	bash -c 'pre-commit run --all-files';\


test:
	PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$${PYTHONPATH}:$${PWD}" pytest resume.py --import-mode=importlib --cov=resume.py;\


setup-env:
	cp .env.example .env;\
	direnv allow;\


install-pre-commit-hook:
	pre-commit install;\


bootstrap: setup-env install install-pre-commit-hook


shell:
	PYTHONPATH="$${PYTHONPATH}:$${PWD}" bpython;\


help:
	@echo "    help:"
	@echo "        Show this help."
	@echo "    install:"
	@echo "        Install requirements."
	@echo "    check:"
	@echo "        Perform some code checks."
	@echo "    test:"
	@echo "        Run tests."
	@echo "    setup-env:"
	@echo "        Copy example environment config for development and setup virtualenv."
	@echo "    install-pre-commit-hook:"
	@echo "        Setup pre commit hook."
	@echo "    bootstrap:"
	@echo "        Bootstrap project."
	@echo "    shell:"
	@echo "        Open python REPL with loaded application."
