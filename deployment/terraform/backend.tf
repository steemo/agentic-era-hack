terraform {
  backend "gcs" {
    bucket = "qwiklabs-gcp-00-e1b69de533fa-terraform-state"
    prefix = "agentic-era-hack/prod"
  }
}
