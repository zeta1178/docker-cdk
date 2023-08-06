#!/bin/bash
unset AWS_ACCESS_KEY_ID
unset AWS_SECRET_ACCESS_KEY
unset AWS_SESSION_TOKEN
#ASSUME_ROLE_ARN="arn:aws:iam::992690408789:role/aws-reserved/sso.amazonaws.com/AWSReservedSSO_AdministratorAccess_8773fea6ec8d21df"
#TEMP_ROLE=$(aws sts assume-role --role-arn $ASSUME_ROLE_ARN --role-session-name role)
#rm -f $PWD/role.txt
#aws sts assume-role --role-arn "arn:aws:iam::992690408789:role/CrossAccountAccessCodeCommitAccessRoleForAWSProServ" --role-session-name "amtrak" | tee $PWD/role.txt
#TEMP_ROLE=$(aws sts get-caller-identity | tee $PWD/role.txt)
#export TEMP_ROLE

# ASSUME_ROLE_ARN="arn:aws:iam::$account_id:role/Secretassumerole"
# TEMP_ROLE=$(aws sts assume-role --role-arn $ASSUME_ROLE_ARN --role-session-name test)
# export TEMP_ROLE
# export AWS_ACCESS_KEY_ID=$(echo "${TEMP_ROLE}" | jq -r '.Credentials.AccessKeyId')
# export AWS_SECRET_ACCESS_KEY=$(echo "${TEMP_ROLE}" | jq -r '.Credentials.SecretAccessKey')
# export AWS_SESSION_TOKEN=$(echo "${TEMP_ROLE}" | jq -r '.Credentials.SessionToken')


#source $PWD/test.env
# export mike3=hotdog

#export mike3=$(cat $PWD/test.env | grep -e "mike3")
#export AWS_ACCESS_KEY_ID=$(cat $PWD/.env.docker | grep -e "AWS_ACCESS_KEY_ID")

#export AWS_SECRET_ACCESS_KEY=$(cat $PWD/.env.docker.AWS_SECRET_ACCESS_KEY)
#export AWS_SESSION_TOKEN=$(cat $PWD/.env.docker.AWS_SESSION_TOKEN)

#export AWS_SESSION_TOKEN=$(cat $PWD/role.txt  | jq -r '.UserId')
#echo $(cat $PWD/role.txt  | jq -r '.UserId')
#export mike3=$(cat $PWD/role.txt  | jq -r '.UserId')
#export mike3="hotdog"

#aws sts assume-role --role-arn arn:aws:iam::992690408789:role/aws-reserved/sso.amazonaws.com/AWSReservedSSO_AdministratorAccess_8773fea6ec8d21df --role-session-name role

export $(aws-export-credentials --env)
#eval $(aws-export-credentials --env-export)
