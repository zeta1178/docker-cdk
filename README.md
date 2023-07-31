# docker-cdk
docker-cdk


Build Docker
Now we are ready to bring up container and run commands

In your /docker folder

Start docker container in the background

```
docker compose up -d
```
Docker container commands
SSH into your docker container

```
docker compose run -it --rm aws-cdk /bin/bash
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
```

Locally you will have a folder with app files ready for creating AWS infrastructure with python CDK.

It should look like below minus the cdk-workshop folder
