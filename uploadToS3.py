import argparse
import boto3
import os

def main():
    parser = argparse.ArgumentParser(description='Upload a file to S3 with metadata.')
    parser.add_argument('file_path', help='Path to the file you want to upload')
    parser.add_argument('--bucket', required=True, help='S3 bucket name (default: alma-web-uros)')
    parser.add_argument('--key', help='S3 object key (optional, defaults to filename)')

    args = parser.parse_args()
    print(args)
    file_path = args.file_path
    bucket_name = args.bucket or 'alma-web-uros'
    key = args.key or os.path.basename(file_path)

    # Get file metadata
    metadata = {
        'author': 'Uros Skrt',
        'organization': 'Almamater'
    }

    # Upload to S3
    s3 = boto3.client('s3')
    s3.upload_file(
        Filename=file_path,
        Bucket=bucket_name,
        Key=key,
        ExtraArgs={
            'Metadata': metadata
        }
    )

    print(f"Uploaded {file_path} to s3://{bucket_name}/{key}")

if __name__ == '__main__':
    main()