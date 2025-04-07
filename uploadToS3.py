import argparse
import boto3
import mimetypes
import os

def main():
    parser = argparse.ArgumentParser(description='Upload a file to S3 with metadata.')
    parser.add_argument('file_path', help='Path to the file you want to upload')
    parser.add_argument('--bucket', help='S3 bucket name (default: alma-web-uros)')
    parser.add_argument('--key', help='S3 object key (optional, defaults to filename)')

    args = parser.parse_args()
    file_path = args.file_path
    bucket_name = args.bucket or 'alma-web-uros'
    # Dobi končnico iz izvorne datoteke
    source_ext = os.path.splitext(file_path)[1]
    if args.key:
        key_root, key_ext = os.path.splitext(args.key)
        # Če key nima končnice ali ima napačno, popravi
        if key_ext.lower() != source_ext.lower():
            key = f"{key_root}{source_ext}"
        else:
            key = args.key
    else:
        key = os.path.basename(file_path)

    # Get file metadata
    mime_type, _ = mimetypes.guess_type(file_path)
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
            'Metadata': metadata,
            'ContentType': mime_type or 'application/octet-stream'
        }
    )

    print(f"Uploaded {file_path} to s3://{bucket_name}/{key}")

if __name__ == '__main__':
    main()