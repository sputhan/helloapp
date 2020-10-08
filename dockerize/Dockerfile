FROM ubuntu:latest

# set working directory
ARG ADDR
WORKDIR /svc
COPY hello /svc/hello

RUN addgroup --system app && adduser --system app && adduser app app
RUN chown -R app:app /svc

USER app

ENTRYPOINT ["./hello"]