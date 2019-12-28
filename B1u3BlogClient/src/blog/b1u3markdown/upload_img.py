import json
import boto3

bucket_name = 'blog.b1u3'
s3 = boto3.resource('s3')

s3.Bucket(bucket_name).upload_file('./fruit_orange.png', 'sample3.png', ExtraArgs={'ACL': 'public-read'})
