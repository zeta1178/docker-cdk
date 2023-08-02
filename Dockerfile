# Dockerfile to run aws cdk commands
# References
# - AWS CLI https://levelup.gitconnected.com/how-to-create-a-simple-docker-image-with-aws-cli-and-serverless-installed-d1cc2901946
FROM alpine:3.16.2

ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY 
ARG AWS_SESSION_TOKEN

#WORKDIR root/
#RUN mkdir -p .aws/sso/cache
#COPY ./config/config .aws/config
#COPY ./config/credentials .aws/credentials

WORKDIR /home/app
COPY ./app /home/app

RUN echo $AWS_ACCESS_KEY_ID
RUN echo $AWS_SECRET_ACCESS_KEY
RUN echo $AWS_SESSION_TOKEN

ENTRYPOINT []