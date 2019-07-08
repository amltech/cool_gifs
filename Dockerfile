FROM python:3.7-alpine
#ARG UID
#ARG GID
#ENV GID=$GID
#ENV UID=$UID
RUN addgroup -g 1000 -S appuser && \
  adduser -u 1000 -S appuser -G appuser

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev zlib-dev jpeg-dev \
  && pip install psycopg2 Pillow==6.0 \
  && apk del build-deps


RUN pip install --upgrade pip
RUN pip install pipenv

COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --system --dev

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

RUN mkdir -p /usr/src/app/media/images/
RUN mkdir /usr/src/app/static/

RUN chown -R  appuser:appuser /usr/src/app

USER appuser
ENTRYPOINT [ "/usr/src/app/entrypoint.sh"]
