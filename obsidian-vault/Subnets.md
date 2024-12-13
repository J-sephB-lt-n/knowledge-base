---
created:
  - 2024-12-11T20:01
modified: 2024-12-12 20:58
tags:
  - network
  - ip
  - ip-address
  - subnet
  - ipv4
type:
  - note
status:
  - in-progress
---
An _IP network_ is a pool of devices connected by a network, where each device is identified in the network using it's IP address. e.g. the internet is an _IP network_. [Internet Protocol (IP) is a set of rules and procedures that govern how devices identify themselves and exchange data with other devices on a network](https://gcore.com/learning/what-is-a-subnet-how-subnetting-works/).

An _IP network_ can be partitioned into smaller (non-overlapping) subnetworks (i.e. _subnets_), each _subnet_ with it's own IP address range.  

## IPv4

An IPv4 address is a 32-bit number, meaning a number which is represented by 32 binary digits. e.g. 10011000011001100101010111001100 is a 32-bit number.

An IP address is divided into four 8-bit numbers (called _octets_). 

For example, the IP address 
```
192.168.1.20
``` 
in binary is 
```
11000000.10101000.00000001.00010100
```

## IPv4 Subnets
A _subnet_ mask is a 32-bit number which is used to subdivide the IP network (pool of IP addresses) into a _network_ portion and a _host_ portion. 

Example: 
The _netmask_ `255.255.252.0` in binary is `11111111.11111111.11111100.00000000` 
Applying this _netmask_ to the IP address `192.168.1.20` (`11000000.10101000.00000001.00010100`)
divides the IP address into a _network_ portion and a _host_ portion: 
```
IP Addr: 1 1 0 0 0 0 0 0 . 1 0 1 0 1 0 0 0 . 0 0 0 0 0 0 0 1 . 0 0 0 1 0 1 0 0
NETMASK: 1 1 1 1 1 1 1 1 . 1 1 1 1 1 1 1 1 . 1 1 1 1 1 1 0 0 . 0 0 0 0 0 0 0 0
Network: _ _ _ _ _ _ _ _   _ _ _ _ _ _ _ _   _ _ _ _ _ _  
Host:                                                    _ _   _ _ _ _ _ _ _ _
```

All devices within the subnet have the same _network_ values, but each connected device has a unique _host_ value. The are 2 reserved IP addresses in the subnet - the _network_ and _broadcast_ IP addresses.

Network: `11000000.10101000.00000000.00000000` (192.168.0.0)
Broadcast: `11000000.10101000.00000011.11111111` (192.168.3.255)
Host range (min): `11000000.10101000.00000000.00000001` (192.168.0.1)
Host range (max):  `11000000.10101000.00000011.11111110` (192.168.3.254)

In [CIDR notation](https://www.cbtnuggets.com/blog/technology/networking/proper-cidr), the subnet of the IP address 192.168.1.20 would usually be notated 192.168.0.0/22 (i.e. just showing the _network_ portion of the IP address). The _/22_ is the number of bits in the _network_ portion. 

Therefore, the number of available IP addresses in a /22 subnet is $(2^{32-22})=1024$ (noting that 2 of them cannot be assigned to individual hosts, but are reserved for "_network_" and "_broadcast_" addresses, so 1022 are actually assignable). In general (aside from the exception /31), number of IP addresses available in a $/n$ subnet is $2^{32-n}$ 

There is something called a "wildcard", which is just the inverse of the subnet mask.
## References
* https://www.freecodecamp.org/news/subnet-cheat-sheet-24-subnet-mask-30-26-27-29-and-other-ip-address-cidr-network-references.
* https://www.cbtnuggets.com/blog/technology/networking/networking-basics-what-is-ipv4-subnetting
* [Online Subnet Calculator](https://jodies.de/ipcalc)
## Related
* Links to other notes which are directly related go here