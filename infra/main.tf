provider "aws" {
  region = "us-east-1"
}

resource "aws_secretsmanager_secret" "api_key" {
  name        = "api_key"
  description = "API key for secure service"
}

resource "aws_secretsmanager_secret_version" "api_key_value" {
  secret_id     = aws_secretsmanager_secret.api_key.id
  secret_string = "initial-secret"
}

resource "aws_cloudwatch_event_rule" "rotate_schedule" {
  name        = "rotate-secrets-schedule"
  schedule_expression = "rate(30 days)"
}