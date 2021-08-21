main:
	sh ./scripts/run.sh

init:
	pipenv install

init-dev:
	pipenv install --development

install-pipenv:
	python -m pip install --user pipenv
