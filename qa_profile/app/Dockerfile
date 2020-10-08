FROM python:3.8-slim-buster

WORKDIR /svc
COPY hello /svc/hello

RUN addgroup --system app && adduser --system app && adduser app app
RUN chown -R app:app /svc

USER app

ENTRYPOINT ["./hello"]
