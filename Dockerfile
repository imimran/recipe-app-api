FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir /app
RUN mkdir /build
COPY ./app /app
WORKDIR /app

RUN adduser -D user
USER user




