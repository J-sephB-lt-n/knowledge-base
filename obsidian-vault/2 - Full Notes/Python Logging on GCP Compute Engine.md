---
created:
  - 2024-09-03T23:21
modified: 2024-09-04 11:46
tags:
  - gcp
  - google-cloud
  - python
  - compute-engine
  - vm
  - virtual-machine
type:
  - note
status:
  - in-progress
---
I was struggling to get the native python logging to appear properly in Cloud Logging (from a Docker container running on the VM). Here is what fixed it for me:

```python
import logging 

import google.cloud.logging # pip install google-cloud-logging

gcp_logging_client = google.cloud.logging.Client()
gcp_logging_handler = google.cloud.logging.handlers.CloudLoggingHandler(
    gcp_logging_client
)
gcp_logging_handler.setFormatter(
    logging.Formatter(
        f"%(name)s - %(levelname)s - %(message)s"
    )
)
logger = logging.getLogger(__name__)
logger.addHandler(gcp_logging_handler)
logger.setLevel(logging.INFO)

logger.info("Started process")
```
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here