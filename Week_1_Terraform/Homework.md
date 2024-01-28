## Module 1 Homework

## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.


## Answered

```bash
# Refresh service-account's auth-token for this session
gcloud auth application-default login

# Initialize state file (.tfstate)
terraform init

# Check changes to new infra plan
terraform plan -var="project=<your-gcp-project-id>"
```

```bash
# Create new infra
terraform apply -var="project=<your-gcp-project-id>"
```

#### The output

```bash
Armut@Armut-PC MINGW64 ~/Desktop/ZoomCamp-GCP
$ terraform apply -var="project=evident-beacon-412117"
google_bigquery_dataset.demo_dataset: Refreshing state... [id=projects/evident-beacon-412117/datasets/demo_dataset]
google_storage_bucket.demo-bucket: Refreshing state... [id=evident-beacon-412117-terra-bucket]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  ~ update in-place

Terraform will perform the following actions:

  # google_storage_bucket.demo-bucket will be updated in-place
  ~ resource "google_storage_bucket" "demo-bucket" {
        id                          = "evident-beacon-412117-terra-bucket"
        name                        = "evident-beacon-412117-terra-bucket"
        # (14 unchanged attributes hidden)

      ~ lifecycle_rule {
          - action {
              - type = "Delete" -> null
            }
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          - condition {
              - age                        = 3 -> null
              - days_since_custom_time     = 0 -> null
              - days_since_noncurrent_time = 0 -> null
              - matches_prefix             = [] -> null
              - matches_storage_class      = [] -> null
              - matches_suffix             = [] -> null
              - num_newer_versions         = 0 -> null
              - with_state                 = "ANY" -> null
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
      - lifecycle_rule {
          - action {
              - type = "AbortIncompleteMultipartUpload" -> null
            }
          - condition {
              - age                        = 1 -> null
              - days_since_custom_time     = 0 -> null
              - days_since_noncurrent_time = 0 -> null
              - matches_prefix             = [] -> null
              - matches_storage_class      = [] -> null
              - matches_suffix             = [] -> null
              - num_newer_versions         = 0 -> null
              - with_state                 = "ANY" -> null
            }
        }
    }

Plan: 0 to add, 1 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_storage_bucket.demo-bucket: Modifying... [id=evident-beacon-412117-terra-bucket]
google_storage_bucket.demo-bucket: Modifications complete after 0s [id=evident-beacon-412117-terra-bucket]

Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

```

```bash
# Delete infra after your work, to avoid costs on any running services
terraform destroy
```

### Here the homework solution

After updating the main.tf and variable.tf files run:

```
terraform apply
```

#### Here the output

````bash
Armut@Armut-PC MINGW64 ~/Desktop/ZoomCamp-GCP
$ terraform apply

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.demo_dataset will be created
  + resource "google_bigquery_dataset" "demo_dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "demo_dataset"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "EU"
      + max_time_travel_hours      = (known after apply)
      + project                    = "evident-beacon-412117"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_storage_bucket.demo-bucket will be created
  + resource "google_storage_bucket" "demo-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "EU"
      + name                        = "evident-beacon-412117-terra-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.demo_dataset: Creating...
google_storage_bucket.demo-bucket: Creating...
google_storage_bucket.demo-bucket: Creation complete after 2s [id=evident-beacon-412117-terra-bucket]
google_bigquery_dataset.demo_dataset: Creation complete after 2s [id=projects/evident-beacon-412117/datasets/demo_dataset]

```
