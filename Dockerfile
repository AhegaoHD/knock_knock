FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

RUN mkdir code
WORKDIR code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
