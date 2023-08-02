

# Dockerfile to run aws cdk commands
# References
# - AWS CLI https://levelup.gitconnected.com/how-to-create-a-simple-docker-image-with-aws-cli-and-serverless-installed-d1cc2901946
FROM alpine:3.16.2

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY 
ARG AWS_SESSION_TOKEN

# Install packages
RUN apk update && apk add --update --no-cache \
    git \
    bash \
    curl \
    openssh \
    python3 \
    py3-pip \
    py-cryptography \
    wget \
    curl \
    nodejs \
    npm
RUN apk --no-cache add --virtual builds-deps build-base python3
# Update NPM
RUN npm config set unsafe-perm true
RUN npm update -g
# Upgrade pip install cli
RUN pip install --upgrade pip && \
    pip install --upgrade awscli
# Install cdk
RUN npm install -g aws-cdk 

#WORKDIR root/
#RUN mkdir -p .aws/sso/cache
#COPY ./config/config .aws/config
#COPY ./config/credentials .aws/credentials

WORKDIR /home/app
COPY ./app /home/app
RUN pip install -r requirements.txt
RUN cdk deploy --all --require-approval never

ENTRYPOINT []