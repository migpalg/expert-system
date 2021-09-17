FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY expert expert
COPY data data
COPY scripts/gunicorn_start.sh scripts/gunicorn_start.sh

ENV PORT=8003

EXPOSE 8003

CMD ["sh", "./scripts/gunicorn_start.sh"]
