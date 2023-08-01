import json
import boto3 
from datetime import datetime

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    acm = boto3.client('acm') 
    response = json.loads(json.dumps(acm.list_certificates(), default=str))
    # return(response['CertificateSummaryList']) 
    cert_output=response['CertificateSummaryList']
    cert_arn_list=[cert['CertificateArn'][(cert['CertificateArn'].find('/')+1):] for cert in cert_output]
    cert_arn_dmn_dict={cert['CertificateArn'][(cert['CertificateArn'].find('/')+1):]:cert['DomainName'] for cert in cert_output }
    cert_arn_exp_dict={cert['CertificateArn'][(cert['CertificateArn'].find('/')+1):]:str(datetime.strptime(cert['NotAfter'][:cert['NotAfter'].find(' ')],'%Y-%m-%d')) for cert in cert_output }
    cert_arn_diff_dict={cert['CertificateArn'][(cert['CertificateArn'].find('/')+1):]:((datetime.strptime(cert['NotAfter'][:cert['NotAfter'].find(' ')],'%Y-%m-%d'))-(datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d'))).days for cert in cert_output }
    cert_arn_exp_dict_list=[{'cert_arn': arn, 'cert_dmn': cert_arn_dmn_dict[arn], 'cert_exp': cert_arn_exp_dict[arn] ,'cert_diff': cert_arn_diff_dict[arn]} for arn in cert_arn_list]
    cert_dict={'certs': cert_arn_exp_dict_list}
    # return(cert_dict)
    
    cert_table = dynamodb.Table('cert_tracker')
    for cert in cert_dict['certs']: 
        response=cert_table.put_item(
                              Item={
                                  'arn': cert['cert_arn'],
                                  'certificate_domain': cert['cert_dmn'],
                                  'certificate_expiry': cert['cert_exp'],
                                  'certificate_daysleft': cert['cert_diff'] 
                              }
                              )