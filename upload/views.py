from rest_framework.views import APIView
from rest_framework.response import Response
import os
import boto3

s3 = boto3.client('s3', aws_access_key_id="YOUR_ACCESS_ID",
                  aws_secret_access_key="YOUR_AWS_SECRET_CODE",
                  region_name="us-east-1")

path = "PATH/OF/THE/FOLDER"
data = {}


class Upload(APIView):

    def get(self, request):
        # Display the list of images from the folder.
        img_list = os.listdir(path)
        i = 1
        for img in img_list:
            data[i] = img
            i += 1
        return Response(data)

    def post(self, request):
        # Upload the files on s3 bucket using boto3 from post method.
        for key in request.data:
            file_name = request.data[key]
            file = path + file_name
            s3.upload_file(file, "YOUR_S3_BUCKET_NAME", file_name)
            response = [{"message": "File uploaded"}]
            return Response(response)

