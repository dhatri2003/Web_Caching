# Web Caching with Proxy Server

## Problem Statement:

This project illustrates web caching between the client, proxy server, and the main server (i.e., the internet). The focus is on showing the caching process at the proxy server. If the requested website is not present in the proxy server's cache, it will request the content from the internet (main server) and return it to the client. Upon arrival at the client end, the requested website is automatically opened in the client's default web browser.

## Software Details:

- Implemented using socket programming in Python.
- Packet analysis is performed using Wireshark.

## Schematic and Diagram:

Please refer to the [Report](./Web_Caching_Report.pdf) for a schematic and diagram depicting the web caching process.

## Usage:
### Run the Python scripts for the client, proxy server, and main server:

###  1. Run proxy server
```bash
python proxy_server.py
```
This starts the proxy server, which will handle requests from the client and communicate with the main server

### 2. Run client
```bash
python client.py
```
Launch the client to push requests to proxy server

### 3. Open Wireshark to analyze the transmitted packets

