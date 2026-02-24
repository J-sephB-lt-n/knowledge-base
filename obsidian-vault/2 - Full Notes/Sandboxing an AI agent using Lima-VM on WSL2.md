---
created:
  - 2026-02-10T22:51
modified: 2026-02-19 21:21
tags:
  - ai
  - ai-dev
  - ai-agent
  - ai-coding
  - sandbox
  - software-architecture
  - security
  - container
  - isolate
  - isolated
type:
  - note
status:
  - in-progress
---
This is a guide for running an AI-agent in a secure local VM with read/write access to only 1 specified local folder.

I added this line to `~/.ssh/config`:
```bash
Include ~/.lima/*/ssh.config
```

## Sort out KVM
(got most of this information from https://serverfault.com/questions/1043441/how-to-run-kvm-nested-in-wsl2-or-vmware)

```bash
sudo usermod -a -G kvm ${USER}
```

I added this to `/etc/wsl.conf`:
(I am INTEL not AMD - run `lscpu` and check your `Vendor ID`)
```bash
[boot]
command = "modprobe kvm_intel && while [ ! -e /dev/kvm ]; do sleep 0.1; done && chown root:kvm /dev/kvm && chmod 660 /dev/kvm"
```

Check if nested virtualization is enabled:
(this should return 'Y'. If not, enable it in `%USERPROFILE%\\.wslconfig` on windows)
```bash
cat /sys/module/kvm_intel/parameters/nested
```

Need to restart WSL for this to take effect:
```powershell
wsl.exe --shutdown
```

## Setup QEMU

```bash
# from inside WSL2 #
sudo apt update
sudo apt install -y qemu-system-x86 qemu-utils
```
## Run the VM

```bash
# lima VM #  
limactl create --name agentvm --vm-type=qemu --containerd=system 
limactl start agentvm
limactl start agentvm --mount-only .:w # read/write access to only current folder
limactl stop agentvm
limactl stop --force agentvm
limactl delete agentvm
```
## References
* https://www.innoq.com/en/blog/2025/12/dev-sandbox/
* https://blaxel.ai/blog/sandbox-management-for-ai-coding-agents
* https://github.com/restyler/awesome-sandbox
* https://github.com/lima-vm/lima
* https://lima-vm.io/docs
* https://github.com/kata-containers/kata-containers
* https://serverfault.com/questions/1043441/how-to-run-kvm-nested-in-wsl2-or-vmware
## Related
* Links to other notes which are directly related go here