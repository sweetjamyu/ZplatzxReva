import boto3
import urllib.parse
def enumerate_bucket_path(bucket_name, job_number):
    # Specify the region
    region = 'us-east-1'

    # Create the S3 client with the specified region
    s3 = boto3.client('s3', region_name=region)

    path = f"revajobs/{job_number}/new/"
    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=path)

    # Construct the URL prefix
    url_prefix = f"https://{bucket_name}.s3.{region}.amazonaws.com/"

    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                # Append the URL prefix to the object key
                object_key = obj['Key']
                full_url = url_prefix + urllib.parse.quote(object_key)
                print(full_url)

if __name__ == "__main__":
    # Get job number from input
    job_number = input("Enter job number: ")

    # Hardcoded bucket name
    bucket_name = "vizalu"

    enumerate_bucket_path(bucket_name, job_number)