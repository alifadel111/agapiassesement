<<<<<<< HEAD
# Uptime Monitoring System (DevOps Assessment)

This project is a complete uptime monitoring system  for a DevOps assessment task.  

It checks the availability of predefined websites, stores the results in AWS S3, and exposes an API to query uptime statistics.
---

## Application Logic

- The application sends HTTP GET requests to each configured URL.
- A website is considered **UP** only if the response returns status code **200**.
- Any non-200 response (including 301, 404, 503, or timeout exceptions) is considered **DOWN**.
- The check retries up to 3 times per site before determining the final status.
- Each result is timestamped and stored as a JSON object in AWS S3.

Example stored result:

json
{
  "timestamp": "2025-04-11T10:30:00Z",
  "url": "https://google.com",
  "status_code": 200,
  "status": "UP"
}


A full CI/CD pipeline is integrated using GitHub + AWS CodePipeline + CodeBuild + ECR + ECS + Fargate + ALB


## Features

- Website monitoring with retry logic
- Stores results as JSON in AWS S3
- FastAPI-based API to query uptime over the last 24h
- Dockerized with multi-stage builds
- CI/CD pipeline from GitHub to ECS via Terraform
- ECS service behind a load balancer (ALB)

---
## project arch

GitHub Repo (agapiassesement)
     |
     | (Webhook Trigger)
     v
AWS CodePipeline
     |
     |----> Source Stage (from GitHub)
     |
     |----> CodeBuild (builds Docker image, pushes to ECR)
     |
     |----> (Optional future) Deploy stage
     |
     v
Amazon ECR (holds built images)
     |
     v
ECS Cluster (Fargate)
     |
     |--- Task Definition (uptime-container)
     |
     v
ALB (Load Balancer) → port 80
     |
     v
FastAPI App → responds on `/uptime/<website>`
     |
     v
Reads uptime data from:
     |
     v
Amazon S3 Bucket (stores uptime JSON results)
=======
# instruction to run 
To run the project locally:
first clone the repository using `git clone https://github.com/alifadel111/agapiassesement.git` 
go into the folder with `cd agapiassesement`.
Then create a virtual environment using `python -m venv venv` and activate it with `source venv/bin/activate` (or `venv\Scripts\activate` on Windows).
After that, install the dependencies by running `pip install -r requirements.txt`.

Before running the app, make sure you have valid AWS credentials configured,since all results are uploaded directly to an S3 bucket (local file storage is not used but can be added as a result file). 
Set the credentials using `export AWS_ACCESS_KEY_ID=your_key`, `export AWS_SECRET_ACCESS_KEY=your_secret`,
 and `export AWS_DEFAULT_REGION=us-east-1`.

Then run the app with `python run.py`.
 This will start the uptime monitor and the FastAPI server on port 8000. You can test it by visiting `http://localhost:8000/uptime/google.com` or using curl.

If you prefer to use Docker, build the image with `docker build -t uptime-monitor .` and run it with `docker run -p 8000:8000 uptime-monitor`.

To deploy the full infrastructure to AWS,
go to the terraform directory using `cd terraform`,
initialize Terraform with `terraform init`,
and apply it with `terraform apply`.
This will provision all required AWS services including CodePipeline, CodeBuild, ECR, ECS Fargate, IAM roles, and the S3 bucket. The CI/CD pipeline will automatically build and deploy the app whenever changes are pushed to the main branch.
