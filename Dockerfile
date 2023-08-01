ARG ALPINE_VERSION=3.16
FROM python:3.10-alpine${ALPINE_VERSION} as builder

ARG AWS_CLI_VERSION=2.11.11
RUN apk add --no-cache git unzip groff build-base libffi-dev cmake
RUN git clone --single-branch --depth 1 -b ${AWS_CLI_VERSION} https://github.com/aws/aws-cli.git

WORKDIR aws-cli
RUN ./configure --with-install-type=portable-exe --with-download-deps
RUN make
RUN make install

# reduce image size: remove autocomplete and examples
RUN rm -rf \
    /usr/local/lib/aws-cli/aws_completer \
    /usr/local/lib/aws-cli/awscli/data/ac.index \
    /usr/local/lib/aws-cli/awscli/examples
RUN find /usr/local/lib/aws-cli/awscli/data -name completions-1*.json -delete
RUN find /usr/local/lib/aws-cli/awscli/botocore/data -name examples-1.json -delete
RUN (cd /usr/local/lib/aws-cli; for a in *.so*; do test -f /lib/$a && rm $a; done)

# Dockerfile to run aws cdk commands
# References
# - AWS CLI https://levelup.gitconnected.com/how-to-create-a-simple-docker-image-with-aws-cli-and-serverless-installed-d1cc2901946
FROM alpine:${ALPINE_VERSION}
COPY --from=builder /usr/local/lib/aws-cli/ /usr/local/lib/aws-cli/
RUN ln -s /usr/local/lib/aws-cli/aws /usr/local/bin/aws
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
# Upgrade pip
RUN pip install --upgrade pip
# Install cdk
RUN npm install -g aws-cdk
RUN cdk --version 

WORKDIR root/
RUN mkdir .aws/sso/cache
COPY ./config/config .aws/config
#COPY ./config/credentials .aws/credentials
COPY ./config/sso/cache/botocore-client-id-us-east-1.json .aws/sso/cache/botocore-client-id-us-east-1.json
COPY ./config/sso/cache/21502f4a281fa759740478902f86d074f0f4af62.json .aws/sso/cache/21502f4a281fa759740478902f86d074f0f4af62.json
#RUN aws sso login

WORKDIR /home/app
COPY ./app /home/app
RUN pip install -r requirements.txt
RUN cdk ls

ENTRYPOINT []