# Stock AWS SMS

### Purpose
To create stock update alert through AWS SNS service

### Documentation
Download: https://www.terraform.io/downloads.html
Official Docs: https://www.terraform.io/

### Secrets
Running module or standalone terraform files requires a secrets.tf (or any name) file to be located in that folder (e.g. /dev_environment, /standalone/s3, etc.).
File should have with the following structure:
variable "access_key" {
    default = "placeholder_access_key"
}

variable "secret_key" {
    default = "placeholder_secret_key"
}