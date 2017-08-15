import os

S3_LOCATION =  os.environ.get('S3_LOCATION')
S3_KEY =  os.environ.get('AWS_ACCESS_KEY_ID')
S3_SECRET =os.environ.get('AWS_SECRET_ACCESS_KEY') 
S3_UPLOAD_DIRECTORY = ''
S3_BUCKET =  os.environ.get('S3_BKT')

SECRET_KEY = "FLASK_SECRET_KEY"
DEBUG = True
PORT = 5002
