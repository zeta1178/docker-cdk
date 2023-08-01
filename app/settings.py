import os
from dotenv import load_dotenv

# Get the path to the directory this file is in
BASEDIR = os.path.abspath(os.path.dirname(__file__))
# Load environment variables
load_dotenv(os.path.join(BASEDIR, '.env'))
CDK_DEPLOY_ACCOUNT = os.getenv('CDK_DEPLOY_ACCOUNT')
CDK_DEFAULT_ACCOUNT = os.getenv('CDK_DEFAULT_ACCOUNT')