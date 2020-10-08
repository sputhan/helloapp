# Dockerize the service and run

Dockerfile can be found in folder dockerize.
Execute the steps from repo root folder to build docker image and run service

    $ cd dockerize
    $ docker build -t hello .
    $ docker run --rm -p 8080:8081 hello :8081

Queries can be run in another terminal for eg

    $ curl localhost:8080/sheena


# Run service in kubernetes cluster

Firstly Push docker image to docker registry

    $ docker login
    $ docker image tag hello sheenaxyz/hellosvc:1.0
    $ docker push sheenaxyz/hellosvc:1.0

Create deployment.yaml and service.yaml. From repo root:

    $ cd kubernetize
    $ kubectl create -f deployment.yaml
    $ kubectl create -f service.yaml

The service shall be up and accessible now. To queries against the service

    curl $(minikube ip):30036/sheena


# Write a client - Devops profile

to demo: first dockerize and run the service so that the service is accessed like this:

    $ curl localhost:8080/sheena

Then to run client, required packages are in devops_profile/requirements.txt:

    $ cd devops_profile
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ export ADDR=localhost:8080
    $ python3 devops_cli.py sheena

This shall print the service response

# qa profile

Go to folder qa and run

    $ docker-compose up

This shall bring up the service and run the tests

