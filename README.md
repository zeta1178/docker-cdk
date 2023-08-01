# docker-cdk
docker-cdk


Build Docker
Now we are ready to bring up container and run commands

In your /docker folder

Start docker container in the background

```
#sso login
pip install aws-export-credentials
aws sso login
aws-export-credentials --profile Admin-MikeCruz --env > .env.docker

docker builder prune (removes images cache)
docker build --progress=plain --no-cache . (verbose building)

#local docker run
docker run --env-file .env.docker -dit aws-cdk bash
docker exec -ti magical_euclid bash


docker compose up -d
```
Docker container commands
SSH into your docker container

```
docker compose run -dit aws-cdk /bin/bash
```
Check CDK is installed (it should result in some cdk help)

```
cdk
```

Go to directory

```
cd /home/app
```

Create CDK files
Initialize a cdk project (python)

```
cdk init sample-app --language python
cdk ls
#test awscli
aws s3 ls --profile Admin-MikeCruz
```

Locally you will have a folder with app files ready for creating AWS infrastructure with python CDK.

It should look like below minus the cdk-workshop folder
