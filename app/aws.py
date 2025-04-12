import boto3
import json
import uuid
from datetime import datetime, timezone

s3 = boto3.client("s3")
bucket_name = "uptime-monitor-results"

def upload_result_to_s3(result: dict):
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    domain = result['url'].replace("https://", "").replace("http://", "").split("/")[0]
    filename = f"{domain}/{timestamp}-{uuid.uuid4().hex}.json"

    s3.put_object(
        Bucket=bucket_name,
        Key=filename,
        Body=json.dumps(result),
        ContentType="application/json"
    )
    print(f"✅ Uploaded to S3: {filename}")

def get_results_for_website(website: str):
    domain = website.replace("https://", "").replace("http://", "").split("/")[0]
    results = []
    objects = s3.list_objects_v2(Bucket=bucket_name, Prefix=f"{domain}/")

    if "Contents" in objects:
        for obj in objects["Contents"]:
            key = obj["Key"]
            response = s3.get_object(Bucket=bucket_name, Key=key)
            content = response["Body"].read().decode("utf-8")
            result = json.loads(content)
            results.append(result)

    return results
