# cloud_services.py

import boto3
from botocore.exceptions import NoCredentialsError

class CloudServices:
    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload_to_s3(self, file_name, bucket):
        try:
            self.s3.upload_file(file_name, bucket, file_name)
            return {"status": "success", "message": "Upload Successful"}
        except FileNotFoundError:
            return {"status": "error", "message": "The file was not found"}
        except NoCredentialsError:
            return {"status": "error", "message": "Credentials not available"}

    def download_from_s3(self, file_name, bucket):
        try:
            self.s3.download_file(bucket, file_name, file_name)
            return {"status": "success", "message": "Download Successful"}
        except NoCredentialsError:
            return {"status": "error", "message": "Credentials not available"}

cloud_services = CloudServices()

def use(data):
    action = data['action']
    file_name = data['file_name']
    bucket = data['bucket']

    if action == 'upload':
        return cloud_services.upload_to_s3(file_name, bucket)
    elif action == 'download':
        return cloud_services.download_from_s3(file_name, bucket)
    else:
        return {"status": "error", "message": "Invalid action"}
