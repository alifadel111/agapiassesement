output "ecr_url" {
  value = aws_ecr_repository.repo.repository_url
}

output "pipeline_url" {
  value = "https://console.aws.amazon.com/codesuite/codepipeline/pipelines/${aws_codepipeline.pipeline.name}/view"
}
