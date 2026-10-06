FROM node:22-bookworm-slim AS node

FROM python:3.12-slim-bookworm

COPY --from=node /usr/local/ /usr/local/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/