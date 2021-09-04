# 🤖 Expert System

This is an university practice to implement an expert system, this is made in top of `Python 3` and uses `pipenv` as environment and dependency manager.

## 💡 Getting started

Make sure that you've already installed the latest `Python 3` version, then install `pipenv` witn the following command:

```bash
python -m pip install --user pipenv
```

### 📦 Installing packages

To install project packages run the following command

```
python -m pipenv install --development
```

That will create a virtual environment and install all the dependencies listed int the `Pipfile`
s

## 🚀 Deployment

### 🐋 Docker

To deploy this application using docker, just run this `docker-compose` command:

```bash
docker-compose up -d --build
```

This will create the required container to make the application work.

### 📦 Heroku

TODO: Implement Heroku deployment
