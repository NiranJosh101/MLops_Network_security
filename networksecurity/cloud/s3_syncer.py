import os

class S3Sync:
    # Post to bucket
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url}"
        os.system(command)


    # Get from bucket
    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder}"
        os.system(command)