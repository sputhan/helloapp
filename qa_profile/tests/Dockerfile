FROM python:3.8-slim-buster

RUN \
 apt-get update &&\
 apt-get install netcat -y

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt --no-cache-dir

# set working directory
WORKDIR /tests


RUN addgroup --system app && adduser --system testuser && adduser testuser app
RUN chown -R testuser:app /tests


COPY . /tests
RUN chown -R testuser:app /tests/entrypoint.sh
RUN chmod +x /tests/entrypoint.sh
USER testuser
