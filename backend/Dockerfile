FROM python:3.9.0

ENV PYTHONBUFFERED 1

RUN mkdir /django

WORKDIR /django

ADD requirements.txt /django/

RUN apt-get update && apt-get install -y python3-opencv

RUN pip install opencv-python

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


ADD . /django/

RUN python manage.py collectstatic --noinput
