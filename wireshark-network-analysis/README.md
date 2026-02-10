# Wireshark Network Traffic Analysis

## Project Overview

This project presents basic network traffic analysis performed using Wireshark.
The goal was to understand how network communication works in practice, identify common protocols, and interpret packet-level data during real network activity.

Packet analysis (packet sniffing) is the process of capturing and inspecting network packets to understand communication between devices and detect potential issues or suspicious behaviour.

---

## Tools Used

* Wireshark
* Windows OS
* Wi-Fi network interface

---

## Key Concepts Demonstrated

* Packet capture
* TCP communication
* TLS/HTTPS encrypted traffic
* HTTP communication
* TCP three-way handshake
* Packet headers and flags
* Capture vs Display filters
* Stream analysis

---

## Screenshots & Explanation

### 1. TLS Encrypted Payload

`wireshark_tls_payload.png`

Captured HTTPS traffic.
The payload appears unreadable because it is protected by TLS encryption. Wireshark can capture packets but cannot decrypt HTTPS without session keys.

---

### 2. Capture Filters

`capture_filters.png`

Capture filters limit what traffic Wireshark records before starting the capture.
They reduce noise and improve performance.

Examples:

* `tcp`
* `udp`
* `port 53`
* `host 192.168.x.x`

---

### 3. Display Filters

`display_filters.png`

Display filters are used after capture to show specific packets.

Examples:

* `tcp`
* `http`
* `ip.addr == 192.168.0.1`
* `tcp.port == 443`

---

### 4. TCP Traffic

`tcp_traffic.png`

Shows active TCP communication between hosts including sequence and acknowledgement numbers.

---

### 5. Single TCP Stream

`single_tcp_stream.png`

Filtering by `tcp.stream eq 0` isolates a single conversation between client and server.

---

### 6. TCP Stream Graph

`tcp_stream_graph.png`

Graphical visualization of TCP sequence numbers over time.
Used to analyse throughput, retransmissions and connection stability.

---

### 7. Packet Details

`packet_details.png`

Detailed packet inspection showing:

* IP header
* TCP header
* Flags (ACK, SYN, FIN)
* Sequence and acknowledgement numbers

---

### 8. HTTPS Handshake

`https_handshake.png`

Shows TLS handshake and connection termination (FIN/ACK).
Indicates secure communication over port 443.

---

## What I Learned

* How TCP connections are established (3-way handshake)
* Difference between HTTP and HTTPS
* Why encrypted traffic cannot be read by packet sniffers
* How to analyse individual sessions
* How to use filters efficiently
* How network protocols operate at packet level

---

## Conclusion

Wireshark is a powerful packet analyser used for troubleshooting, network monitoring, and cybersecurity investigations.
Through this project I gained practical experience analysing real network traffic and interpreting protocol behaviour.

This project demonstrates foundational skills useful for Network+, Security+, and junior SOC analyst roles.

