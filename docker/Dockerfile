FROM python:3-alpine

WORKDIR /usr/src/app

RUN pip install --user --no-warn-script-location pipenv

COPY . .

RUN python -m pipenv lock --requirements > requirements.txt

ENV PORT=8003

RUN python -m pip install -r requirements.txt

EXPOSE 8003

CMD ["sh", "./gunicorn_start.sh"]
