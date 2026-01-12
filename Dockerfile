FROM python:3.13-slim

WORKDIR /usr/geoalchemy-main

ENV PYTHONUNBUFFERED=1 \
    TZ="Europe/Moscow"

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libgl1 \
    libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install poetry==2.0.1 --no-cache-dir --root-user-action=ignore

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-cache --only main --no-root

COPY . .
