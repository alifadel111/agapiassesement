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
