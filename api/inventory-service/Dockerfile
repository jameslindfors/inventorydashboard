# syntax=docker/dockerfile:1
FROM python:3.8.14-alpine3.16 as builder

RUN apk add gcc python3-dev musl-dev

WORKDIR /src

COPY ./requirements.txt requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

ENV FASTAPI_APP main.py
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT prod
ENV PYTHONPATH=/src

COPY . ./src

EXPOSE 8080

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]