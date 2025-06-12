# Computer Networks: LAN, WAN, PAN, MAN

## Introduction

Computer networks are collections of interconnected devices that can communicate and share resources. Think of networks like different types of road systems - from small neighborhood streets to international highways, each serving different purposes and covering different distances.

## Types of Computer Networks

### LAN (Local Area Network)

* **Definition**: A network confined to a small geographical area, typically within a single building or campus.
* **Characteristics**:
  * High data transfer rates (typically 100 Mbps to 10 Gbps)
  * Low latency (delay)
  * Limited geographical coverage (usually within 1km)
  * Typically owned and managed by a single organization

* **Real-world Example**: 
  * Your home Wi-Fi network connecting your laptop, smartphone, and smart TV
  * Office network connecting computers, printers, and servers
  * School computer lab network

* **Practical Command**:
  ```bash
  # View your LAN IP address and interface details
  ip a
  # or on older systems
  ifconfig
  
  # See connected devices on your LAN (requires arp-scan to be installed)
  sudo arp-scan --localnet
  ```

### WAN (Wide Area Network)

* **Definition**: A network that spans a large geographical area, often connecting multiple LANs across cities, countries, or continents.
* **Characteristics**:
  * Lower data rates compared to LANs (typically from 1.5 Mbps to 1 Gbps)
  * Higher latency
  * Covers large geographical areas
  * Often uses leased telecommunication lines

* **Real-world Example**: 
  * The Internet - the largest WAN in the world
  * A company network connecting branch offices across different cities
  * JioFiber's network infrastructure connecting homes across India

* **Practical Command**:
  ```bash
  # Test connectivity to a remote server on a WAN (like the internet)
  ping 8.8.8.8
  
  # Trace the route to a remote server, showing all network hops
  traceroute google.com
  ```

### PAN (Personal Area Network)

* **Definition**: A very small network for personal use, typically within a range of 10 meters.
* **Characteristics**:
  * Very limited range (typically up to 10 meters)
  * Connects personal devices
  * Often uses wireless technologies like Bluetooth or NFC

* **Real-world Example**: 
  * Bluetooth connection between your smartphone and wireless earbuds
  * Connecting your laptop to a mobile hotspot
  * Smartwatch connected to your phone

* **Practical Command**:
  ```bash
  # List Bluetooth devices on Linux
  bluetoothctl devices
  
  # Check if Bluetooth is enabled
  bluetoothctl show
  ```

### MAN (Metropolitan Area Network)

* **Definition**: A network spanning a city or large campus, larger than a LAN but smaller than a WAN.
* **Characteristics**:
  * Coverage area typically within 50km
  * Data rates between those of LANs and WANs
  * Often used by municipal governments or large organizations

* **Real-world Example**: 
  * City-wide Wi-Fi networks
  * University campus networks connecting multiple buildings
  * Cable TV networks covering a city

* **Practical Command**:
  ```bash
  # Check connectivity to a MAN resource
  ping campus-server.university.edu
  
  # View routing information that might include MAN routes
  ip route
  ```

## Comparison Table

| Network Type | Geographic Scope | Speed | Latency | Example |
|--------------|------------------|-------|---------|----------|
| PAN | Within reach of a person (10m) | 1-3 Mbps (Bluetooth) | Very Low | Phone to wireless earbuds |
| LAN | Building/Campus (1km) | 100 Mbps - 10 Gbps | Low | Office network |
| MAN | City (50km) | 10 Mbps - 1 Gbps | Medium | University campus network |
| WAN | Country/Global (1000+ km) | 1.5 Mbps - 1 Gbps | High | The Internet |

## Simple Network Diagram

```
PAN                LAN                  MAN                  WAN
<10m               <1km                 <50km                >50km
┌─────┐           ┌─────────┐         ┌───────────┐       ┌───────────┐
│     │ Bluetooth │         │         │           │       │           │
│  📱 ├───────────┤   🏠    │ Fiber   │    🏙️     │       │    🌎     │
│     │           │ Router  ├─────────┤  ISP Node ├───────┤  Internet │
└─────┘           └─────────┘         └───────────┘       └───────────┘
  │                   │                                          │
┌─────┐           ┌─────────┐                              ┌───────────┐
│     │           │         │                              │           │
│ 🎧  │           │   💻    │                              │  Remote   │
│     │           │         │                              │  Server   │
└─────┘           └─────────┘                              └───────────┘
```

## Summary

* Networks are classified by their geographical coverage and purpose, from personal (PAN) to global (WAN) scales.
* LANs provide high-speed connectivity within limited areas like homes and offices.
* WANs connect distant networks together, with the Internet being the largest example.

## FAQ

### Q: What's the difference between Wi-Fi and a LAN?
**A:** Wi-Fi is a technology that can be used to create a LAN. A LAN refers to the network itself (the connected devices), while Wi-Fi is just one method (wireless) to connect those devices. A LAN can also use wired connections like Ethernet.

### Q: Can a device be part of multiple networks simultaneously?
**A:** Yes! Your smartphone might be connected to your wireless earbuds via Bluetooth (PAN) while also connected to your home Wi-Fi (LAN) which connects to the Internet (WAN).

### Q: Why is my LAN connection faster than my internet connection?
**A:** Your LAN operates within your control and uses short-distance, high-bandwidth connections. Your internet connection depends on your ISP's infrastructure and must travel much greater distances, resulting in lower speeds.

### Q: What determines the speed of a network?
**A:** Network speed depends on several factors: the technology used (Ethernet, Wi-Fi standard, fiber optic), the quality of hardware (routers, switches), the number of connected devices sharing bandwidth, and physical limitations like distance and interference.

### Q: How do these different networks connect to each other?
**A:** Networks connect through special devices called gateways. For example, your home router acts as a gateway between your LAN and your ISP's WAN. These gateways handle the translation between different network protocols and addressing schemes.