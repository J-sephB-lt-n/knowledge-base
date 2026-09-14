---
created:
  - 2026-02-18T10:57
modified: 2026-07-08 13:08
tags:
  - rclone
  - sharepoint
  - microsoft
  - auth
  - files
  - download
  - graph-explorer
  - microsoft-graph-explorer
  - token
  - access-token
type:
  - note
status:
  - completed
---
This note explains how to programmatically list and download files from a microsoft sharepoint folder (and it's nested subfolders) without requiring you to have microsoft admin access.
It uses [rclone](https://github.com/rclone/rclone) and a temporary access token from [microsoft Graph Explorer](https://developer.microsoft.com/en-us/graph/graph-explorer) .   

This guide assumes that you are using ubuntu linux.
# rclone Setup Guide

```bash
brew install rclone # or apt install rclone
```

Get a temporary access token from https://developer.microsoft.com/en-us/graph/graph-explorer

Get the your `site_id` by running:
```http
GET https://graph.microsoft.com/v1.0/sites/{{YOUR_SHAREPOINT_TENANT_DOMAIN}}:/sites/{{YOUR_SITE_NAME}}
Authorization: Bearer {{ TEMP_GRAPH_EXPLORER_ACCESS_TOKEN }}
```

I used [bruno](https://github.com/usebruno/bruno) for this (and all other HTTPS requests in this guide).

Get `directory_id`s for your site:
```http
GET https://graph.microsoft.com/v1.0/sites/{{YOUR_SITE_ID_FROM_PREVIOUS_STEP}}/drives
Authorization: Bearer {{ TEMP_GRAPH_EXPLORER_ACCESS_TOKEN }}
```

Decode your TEMP_GRAPH_EXPLORER_ACCESS_TOKEN (it's a JWT) to get the expiry date of the token. It's a long integer (unix epoch timestamp) in there with key `exp`. 
(I have a bash alias `decode_jwt` but you can also use https://jwt.ms/).

Convert the unix epoch format expiry date to a ISO 8601 (RFC 3339) string (you need this format for your `rclone.conf`): 
```bash
# this is the command on ubuntu (macos unix differs) #
# don't put in '@1771483940' - put in your own "exp" value #
date -u -d @1771483940 +"%Y-%m-%dT%H:%M:%SZ"
```

In `~/.config/rclone/rclone.conf`:
```toml
[temp-sharepoint-access]
type = onedrive
provider = sharepoint
token = {"access_token":"TEMP_GRAPH_EXPLORER_ACCESS_TOKEN_HERE","token_type":"Bearer","refresh_token":"","expiry":"2026-02-19T06:52:20Z"}
drive_id = b!...   # your drive ID from prior step
drive_type = documentLibrary
```

- All entries in `rclone.conf` must be a single line (e.g. you can't indent your JSON)
- Set the "expiry" in `token` here to your ISO 8601 date (from the prior step)

If you have not been given access to the root folder of your sharepoint but only a subfolder within it, you will need to do this:
```http
GET https://graph.microsoft.com/v1.0/drives/{{YOUR_DRIVE_ID}}/root:/path/to/lowest%20folder/you/have/access/to:/children?top=5
Authorization: Bearer {{ TEMP_GRAPH_EXPLORER_ACCESS_TOKEN }}
```

Then, from that response body, find the `parentReference > id` (it's a long string with uppercase digits and numbers like 3HB48X43B6G7F8S9A0W2Z4).
Then, add this parent reference ID to your `~/.config/rclone/rclone.conf`:
```toml
[temp-sharepoint-access]
... # the other stuff shown earlier
root_folder_id = 3HB48X43B6G7F8S9A0W2Z4 # with your actual parent_ref_id
```

# rclone Usage Guide

List all filepaths matching a specific pattern:
(e.g. this is listing all .PDF files with filename "X1234{{any-text-here}}.pdf" in any folder)
```bash
rclone lsf temp-sharepoint-access: --recursive --files-only --fast-list --include '**/X1234*.pdf' > files_to_download.txt
```

or if you need regex (much slower):
```bash
rclone lsf temp-sharepoint-access: --recursive --files-only --fast-list | grep -E ".*/X1234[^\/]*\.pdf$" > files_to_download.txt 
```

To search only within a subfolder use:
```bash
rclone lsf "temp-sharepoint-access:Path/To/Subfolder" ...
```

Download the files you've identified:
```bash
rclone copy temp-sharepoint-access: ./input_files/ \
  --files-from files_to_download.txt
```

For OR logic, you can use multiple `--include` flags, but when you get into the tens or hundreds of them, rather use `--filter-from` 

## References
* https://github.com/rclone/rclone
* https://developer.microsoft.com/en-us/graph/graph-explorer
## Related
* Links to other notes which are directly related go here