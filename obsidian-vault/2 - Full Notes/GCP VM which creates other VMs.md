---
created:
  - 2024-09-02T13:54
modified: 2024-09-02 14:12
tags:
  - gcp
  - vm
  - virtual-machine
  - compute-engine
  - iam
  - service-account
  - create
  - creates
  - instance
  - cloud
  - google-cloud
type:
  - note
status:
  - completed
---
These are almost certainly not the minimum permissions required, but the follow works:

Add the following roles to the service account used by the VM doing the creating:
1. Compute Admin
2. Artifact Registry Reader
3. Service Account User
4. Storage Object Viewer

Set explicit access for the following API (in the Compute Engine _Create Instance_ step):
1. Compute Engine read/write

Run this on the creator VM in order to create a new VM:

```bash
pip install google-auth requests
```

```python
import google.auth
import google.auth.transport.requests
import requests

credentials, gcp_project_id = google.auth.default()
credentials.refresh(auth_req)  # refresh token

request = requests.post(
    url="https://compute.googleapis.com/compute/v1/projects/your-gcp-project-id/zones/europe-west2-c/instances",
    headers={"Authorization": f"Bearer {credentials.token}"},
    json={
	    # get this from the Compute Engine 'Create Instance' <equivalent cost> section under "REST"
    }
)
print(request)
print(request.text)
```
## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here