import crontab
import os
import boto3
from datetime import datetime

# define s3 bucket and target directory
s3_bucket_name = 'cilbucket'
target_directory = '/home/ec2-user/backups3objects/'

# Create a Boto3 S3 client
s3_client = boto3.client('s3')

# List objects in the S3 bucket


def my_s3_backup():
    try:
        # Create the local backup directory if it doesn't exist
        os.makedirs(target_directory, exist_ok=True)

        # List objects in the S3 bucket
        objects = s3_client.list_objects_v2(Bucket=s3_bucket_name)

        # Copy S3 objects to the local backup directory
        for obj in objects.get('Contents', []):
            key = obj['Key']
            local_path = os.path.join(target_directory, key)
            s3_client.download_file(s3_bucket_name, key, local_path)
        print(f"Backup completed at {datetime.now()}")

    except Exception as e:
        print(f"Error: {str(e)}")


# Create a cron job to run this python script at 5 pm daily

crontab.CronTab().new(command='/usr/bin/python /path/to/file/copy-s3-objects.py',
                      hour='17', minute='0')
# Write the cron jobs to the crontab file
crontab.CronTab().write()
