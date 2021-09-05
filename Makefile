main:
	docker-compose -f docker-compose.dev.yml up --build

init:
	pipenv install

init-dev:
	pipenv install --development

install-pipenv:
	python -m pip install --user pipenv

deploy-docker:
	docker-compose up -d --build

build-docker-image:
	docker build -t expert-system-api:$(tag) -f docker/Dockerfile .
