provider "aws" {
  region = "ap-south-1"
}

resource "aws_s3_bucket" "monitoring_logs" {
  bucket = "rahul-monitoring-logs"
  acl    = "private"
}
