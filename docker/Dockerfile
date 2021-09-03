FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install --user --no-warn-script-location pipenv

COPY . .

ENV PORT=8003

RUN python -m pipenv install

EXPOSE 8003

CMD ["python", "-m", "pipenv", "run", "sh", "./gunicorn_start.sh"]
