# Dockerize the service and run

After writing Dockerfile

    docker build -t hello .
    docker run --rm -p 8080:8081 hello :8081

# in another terminal run queries

curl localhost:8080/sheena


# Run service in kubernetes cluster

To Push docker image to docker registry

    docker login
    docker build -t sheenaxyz/hellosvc:1.0 .
    docker push sheenaxyz/hellosvc:1.0

Create deployment.yaml and service.yaml

    kubectl create -f deployment.yaml
    kubectl create -f service.yaml

# Run queries against the service

    curl $(minikube ip):30036/sheena


# Write a client
# Devops profile

devops_cli.py

# qa profile

Go to folder qa and run

    docker-compose up


