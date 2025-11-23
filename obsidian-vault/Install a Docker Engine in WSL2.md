---
created:
  - 2025-11-20T11:32
modified: 2025-11-20 12:11
tags:
  - docker
  - docker-desktop
  - wsl
  - wsl2
  - linux
  - windows
  - os
  - subsystem
  - vm
  - dx
  - dev
  - software-development
type:
  - note
status:
  - in-progress
---
You don't have to use Docker Desktop. You can run the docker engine yourself in WSL2:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl

# Creates `/etc/apt/keyrings` with mode `0755` (rwxr-xr-x). Common for storing repo keys
sudo install -m 0755 -d /etc/apt/keyrings

# Downloads Docker’s GPG key directly from https://download.docker.com
#  saves it in the keyrings directory
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc

# make it world-readable
sudo chmod a+r /etc/apt/keyrings/docker.asc

# add Docker's apt repo to the apt install sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null 

# update apt package registry
sudo apt-get update

# install docker packages:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# add `docker` user group (might complain about already existing)
sudo addgroup docker

# add yourself to the `docker` user group
sudo usermod -aG docker $USER

# add this:
#    [boot]
#    systemd=true
# into /etc/wsl.conf 
sudo vim /etc/wsl.conf    # make this change manually

echo 'you must restart WSL for changes to take effect'

############
# OPTIONAL #
############
# change nameserver to 1.1.1.1 (cloudflare) or 8.8.8.8 (google) in /etc/resolv.conf:
sudo vim /etc/resolv.conf

# to /etc/wsl.conf add:
# [network]
# generateResolvConf = false
# # (this makes /etc/resolv.conf not auto-generate on WSL start)
sudo vim /etc/wsl.conf

# check that it works #  
docker run hello world
```

## References
* https://daniel.es/blog/how-to-install-docker-in-wsl-without-docker-desktop/
## Related
* Links to other notes which are directly related go here