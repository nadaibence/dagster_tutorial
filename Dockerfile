FROM python:3.8

RUN mkdir /app
WORKDIR /app

RUN pip install dagster dagit dagster-postgres

COPY ./app/requirements.txt requirements.txt
RUN pip install -r requirements.txt

EXPOSE 3000