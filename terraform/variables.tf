variable "region" {
  default = "us-east-1"
}

variable "project_name" {
  default = "ali"
}

variable "github_owner" {
  default = "alifadel111"
}

variable "github_repo" {
  default = "agapiassesement"
}

variable "github_branch" {
  default = "main"
}

variable "github_oauth_token" {
  description = "GitHub personal access token"
  type        = string
  sensitive   = true
}
