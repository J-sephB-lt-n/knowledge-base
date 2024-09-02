---
created:
  - 2024-08-18T22:48
modified: 2024-08-20 21:27
tags:
  - security
  - iam
  - identity
  - access
  - roles
  - gcp
  - aws
  - cloud
  - google-cloud
type:
  - note
status:
  - in-progress
---
# IAM in Google Cloud

| Entity     | Description                                                                                                                                                                                   | Example(s)                                                                                                            |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Principal  | - An identity that can access a resource. <br>- Principals are granted access to resources.                                                                                                   | - A google user account (e.g. joe@gmail.com)<br>- A service account (e.g. bot@my-gcp-project.iam.gserviceaccount.com) |
| Role       | A collection of permissions                                                                                                                                                                   | `roles/compute.admin`<br>`roles/storage.objectViewer`                                                                 |
| Permission | - Defines access to a specific operation that can be performed on a resource<br>- Principals are not granted permissions directly, but rather roles (which are groups of related permissions) | `compute.disks.resize`<br>`storage.objects.list`                                                                      |
# IAM in AWS

| Entity | Description                                                                                                                                                                            | Example(s)                                                                                                                                                          |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User   | - An identity requiring long-term access to AWS resources.<br>- Must authenticate with AWS before they are given access to resources                                                   |                                                                                                                                                                     |
| Group  | - A collection of IAM users.<br>- This is used to make it easier to provide the same access to a large number of users without having to specify permissions for each user separately. | - Database admins<br>- Testers                                                                                                                                      |
| Role   | - A collection of permissions<br>- In contrast to users, roles provide temporary access                                                                                                |                                                                                                                                                                     |
| Policy | - A document specifying a list of allow/deny permissions to specific AWS resources<br>- Policies are attached to an "identity" (a user, group or role)                                 | ```json<br>{"Sid": "AllowGetObject",<br>      "Action": "s3:GetObject",<br>      "Effect": "Allow",<br>      "Resource": "arn:aws:s3:::my-bucket/*"<br>}<br>```<br> |
## References
* https://www.freecodecamp.org/news/aws-iam-explained/
## Related
* Links to other notes which are directly related go here