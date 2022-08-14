FROM python:3.8.12-alpine3.14

RUN apk add --no-cache postgresql-libs \
  && apk add --no-cache --virtual .build-deps curl gcc g++ musl-dev postgresql-dev libffi-dev openldap-dev

RUN mkdir -p /app && chown -R nobody.nobody /app 

WORKDIR /app

ARG IREDAPD_VERSION=5.1

RUN curl -L https://github.com/iredmail/iRedAPD/archive/refs/tags/${IREDAPD_VERSION}.tar.gz | tar -xz --strip-components=1 \
  && pip install -r requirements.txt --no-cache-dir \
  && apk --purge del .build-deps

COPY config/settings.py /app/settings.py

EXPOSE 7777

CMD ["python3", "/app/iredapd.py", "--foreground"]
