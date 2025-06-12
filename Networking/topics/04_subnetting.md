# Subnetting: Explained Simply with Examples

## Introduction

Subnetting is the practice of dividing a network into smaller, more manageable sub-networks called subnets. Think of it like dividing a large piece of land into smaller plots - each plot has its own address range but is part of the same overall property.

## Why Subnet?

* **Improved Network Performance**: Reduces broadcast traffic by containing it within smaller networks
* **Enhanced Security**: Allows for network segmentation and access control between subnets
* **Efficient Address Allocation**: Makes better use of available IP addresses
* **Simplified Management**: Easier to manage smaller, logical network segments
* **Reduced Network Congestion**: Localizes traffic within appropriate subnets

## Subnet Mask Basics

A subnet mask determines which portion of an IP address refers to the network and which portion refers to hosts.

* **Format**: Like an IP address, written as four decimal numbers separated by periods
  * Example: `255.255.255.0`
* **Binary Representation**: A series of 1s followed by 0s
  * 1s represent the network portion
  * 0s represent the host portion
* **CIDR Notation**: Written as a suffix with a forward slash
  * Example: `/24` (equivalent to 255.255.255.0)

### Common Subnet Masks

| CIDR Notation | Subnet Mask | # of Usable Hosts | Binary Representation |
|--------------|-------------|-------------------|------------------------|
| /24 | 255.255.255.0 | 254 | 11111111.11111111.11111111.00000000 |
| /25 | 255.255.255.128 | 126 | 11111111.11111111.11111111.10000000 |
| /26 | 255.255.255.192 | 62 | 11111111.11111111.11111111.11000000 |
| /27 | 255.255.255.224 | 30 | 11111111.11111111.11111111.11100000 |
| /28 | 255.255.255.240 | 14 | 11111111.11111111.11111111.11110000 |
| /29 | 255.255.255.248 | 6 | 11111111.11111111.11111111.11111000 |
| /30 | 255.255.255.252 | 2 | 11111111.11111111.11111111.11111100 |
| /31 | 255.255.255.254 | 0* | 11111111.11111111.11111111.11111110 |
| /32 | 255.255.255.255 | 1 | 11111111.11111111.11111111.11111111 |

*Note: /31 is a special case used for point-to-point links (RFC 3021)

## Subnetting Analogy: The Apartment Building

Think of an IP network like an apartment building:

* The **network address** is like the building's street address (e.g., 192.168.1.0)
* The **subnet mask** determines how many floors and apartments are in the building
* Each **subnet** is like a floor in the building
* Each **host address** is like an individual apartment
* The **broadcast address** is like the building's intercom system that reaches everyone

When you subnet, you're essentially deciding how to divide your building into floors and how many apartments to put on each floor.

## Subnetting Step by Step

### Step 1: Determine Your Requirements

* How many subnets do you need?
* How many hosts per subnet do you need?

### Step 2: Calculate the Appropriate Subnet Mask

* For number of subnets: 2^n ≥ number of required subnets (where n is the number of bits borrowed)
* For hosts per subnet: 2^m - 2 ≥ number of required hosts (where m is the number of host bits)

### Step 3: Calculate the Subnet Addresses

* Network address of first subnet = Original network address
* Network address of next subnet = Previous subnet + subnet increment

### Step 4: Calculate Host Range for Each Subnet

* First usable host = Network address + 1
* Last usable host = Broadcast address - 1
* Broadcast address = Next subnet - 1 (or all host bits set to 1)

## Practical Example 1: Dividing a /24 Network into Four Equal Subnets

Let's subnet 192.168.1.0/24 into four equal subnets:

1. **Determine bits needed for subnets**:
   * We need 4 subnets, so we need 2 bits (2^2 = 4)
   * We'll borrow 2 bits from the host portion
   * New subnet mask: /26 (255.255.255.192)

2. **Calculate subnet increment**:
   * Increment = 256 - 192 = 64

3. **Calculate the subnets**:

| Subnet | Network Address | First Usable | Last Usable | Broadcast |
|--------|----------------|-------------|------------|------------|
| 1 | 192.168.1.0/26 | 192.168.1.1 | 192.168.1.62 | 192.168.1.63 |
| 2 | 192.168.1.64/26 | 192.168.1.65 | 192.168.1.126 | 192.168.1.127 |
| 3 | 192.168.1.128/26 | 192.168.1.129 | 192.168.1.190 | 192.168.1.191 |
| 4 | 192.168.1.192/26 | 192.168.1.193 | 192.168.1.254 | 192.168.1.255 |

* **Practical Command**:
  ```bash
  # View your current subnet mask
  ip addr show | grep inet
  
  # Calculate subnet information for a given network
  ipcalc 192.168.1.0/26
  ```

## Practical Example 2: Creating Subnets of Different Sizes (VLSM)

Variable Length Subnet Masking (VLSM) allows creating subnets of different sizes. Let's subnet 172.16.0.0/16 for different departments:

* **Department A**: Needs 4000 hosts
* **Department B**: Needs 500 hosts
* **Department C**: Needs 100 hosts
* **Department D**: Needs 2 hosts (point-to-point link)

1. **Sort requirements from largest to smallest**:
   * Dept A: 4000 hosts → needs 12 host bits (2^12 = 4096) → /20 mask
   * Dept B: 500 hosts → needs 9 host bits (2^9 = 512) → /23 mask
   * Dept C: 100 hosts → needs 7 host bits (2^7 = 128) → /25 mask
   * Dept D: 2 hosts → needs 2 host bits (2^2 = 4) → /30 mask

2. **Assign subnets**:

| Department | Requirement | Subnet | Mask | Usable Hosts |
|-----------|------------|--------|------|-------------|
| A | 4000 hosts | 172.16.0.0 | /20 (255.255.240.0) | 4094 |
| B | 500 hosts | 172.16.16.0 | /23 (255.255.254.0) | 510 |
| C | 100 hosts | 172.16.18.0 | /25 (255.255.255.128) | 126 |
| D | 2 hosts | 172.16.18.128 | /30 (255.255.255.252) | 2 |

## Subnetting Shortcuts

### The "Power of 2" Method

* Each CIDR increment doubles or halves the network size
* /24 has 256 addresses, /25 has 128, /26 has 64, etc.

### The "256 Minus Subnet Mask Octet" Method

To find the subnet increment in any octet:
1. Identify the octet where the subnet mask is not 255 or 0
2. Subtract that octet's value from 256

Example: For subnet mask 255.255.255.192 (/26)
* Last octet is 192
* 256 - 192 = 64 (subnet increment)

### Binary Method for Quick Calculations

```
Subnet Mask: /27 (255.255.255.224)
Binary:      11100000 (last octet)
Value:       128 64 32 16 8 4 2 1
Sum:         224

Subnet increment: 32 (the rightmost 1-bit value)
Subnets: 0, 32, 64, 96, 128, 160, 192, 224
```

## Practical Subnetting Diagram

```
Original Network: 192.168.1.0/24
Subnetted into four /26 networks:

┌───────────────────────────────────────────────────────────┐
│                    192.168.1.0/24                         │
│                                                           │
│  ┌─────────────────┐ ┌─────────────────┐                  │
│  │ 192.168.1.0/26  │ │ 192.168.1.64/26 │                  │
│  │                 │ │                 │                  │
│  │ Hosts: 1-62     │ │ Hosts: 65-126   │                  │
│  │ Broadcast: 63   │ │ Broadcast: 127  │                  │
│  └─────────────────┘ └─────────────────┘                  │
│                                                           │
│  ┌─────────────────┐ ┌─────────────────┐                  │
│  │ 192.168.1.128/26│ │ 192.168.1.192/26│                  │
│  │                 │ │                 │                  │
│  │ Hosts: 129-190  │ │ Hosts: 193-254  │                  │
│  │ Broadcast: 191  │ │ Broadcast: 255  │                  │
│  └─────────────────┘ └─────────────────┘                  │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

## Real-World Subnetting Example: Corporate Network

A company wants to divide its 10.0.0.0/16 network for different departments:

* **Engineering**: Largest department, needs 8000 addresses
* **Sales & Marketing**: Medium size, needs 2000 addresses
* **Finance**: Small department, needs 500 addresses
* **Management**: Very small, needs 30 addresses
* **Server Farm**: Needs 100 addresses with strict isolation
* **Guest Network**: Needs 250 addresses with limited access

### Solution

| Department | Subnet | Mask | Usable Hosts |
|-----------|--------|------|-------------|
| Engineering | 10.0.0.0 | /19 (255.255.224.0) | 8,190 |
| Sales & Marketing | 10.0.32.0 | /21 (255.255.248.0) | 2,046 |
| Finance | 10.0.40.0 | /23 (255.255.254.0) | 510 |
| Management | 10.0.42.0 | /27 (255.255.255.224) | 30 |
| Server Farm | 10.0.42.32 | /25 (255.255.255.128) | 126 |
| Guest Network | 10.0.42.160 | /24 (255.255.255.0) | 254 |

## Summary

* Subnetting divides networks into smaller, manageable segments for better performance and security.
* The subnet mask determines which part of an IP address identifies the network and which part identifies hosts.
* VLSM allows for efficient use of IP space by creating different-sized subnets based on actual needs.

## FAQ

### Q: How do I calculate how many subnets I can create?
**A:** The formula is 2^n, where n is the number of bits borrowed from the host portion. For example, if you borrow 3 bits, you can create 2^3 = 8 subnets.

### Q: How do I calculate how many hosts I can have per subnet?
**A:** The formula is 2^m - 2, where m is the number of host bits (the 0s in the subnet mask). We subtract 2 because each subnet reserves one address for the network ID and one for the broadcast address. For example, a /24 subnet has 8 host bits, so it can have 2^8 - 2 = 254 usable host addresses.

### Q: Why is the first address in a subnet reserved?
**A:** The first address (all host bits set to 0) is the network identifier. It represents the subnet itself rather than any individual host. For example, 192.168.1.0 in a 192.168.1.0/24 network.

### Q: Why is the last address in a subnet reserved?
**A:** The last address (all host bits set to 1) is the broadcast address. It's used to send data to all hosts in that subnet simultaneously. For example, 192.168.1.255 in a 192.168.1.0/24 network.

### Q: How do I determine which subnet an IP address belongs to?
**A:** Apply the subnet mask to the IP address using a bitwise AND operation. The result is the network address. For example, 192.168.1.57 with a mask of 255.255.255.192 (/26) belongs to the 192.168.1.0/26 subnet because 192.168.1.57 AND 255.255.255.192 = 192.168.1.0.