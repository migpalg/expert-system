FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install --user pipenv

COPY Pipfile ./
COPY Pipfile.lock ./

COPY expert expert

ENV FLASK_APP='expert'
ENV FLASK_ENV=development
ENV FLASK_RUN_PORT=5000

RUN python -m pipenv install

EXPOSE 5000

CMD [ "python", "-m", "pipenv", "run", "flask", "run"]
