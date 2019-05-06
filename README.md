# Packet Sniffer Attack Solution Imitation
## Python 2.7, Linux

## How to use?
Open 3 terminal windows in ubuntu.<br> In every window open the derictory containing python files.<br>
Example:
```bash
cd Documents/PacketSniffer
```
1) Run server: 
```bash 
python ./NetworkService.py 
```
2) Run client:
```bash 
python ./Client.py 
```
3) Run adversary:
```bash 
sudo python ./sniffer.py 
```
## How it works? 
Network service listens on UDP port 12321, which accepts connections on that port and echoes complete lines back to clients. <br>
The client connecting to this service via UDP. <br>
Every 3 seconds the client sends some data and waits for the server to echo it.<br>
The data is spilt into packets of 100 bytes size. <br>
Each UDP packet contains a sequence number and data .<br>
The adversary is listens on localhost to the connection between the client and the server.
## Attack
The adversary is preventing from packets with chosen sequence numbers from ar-riving to their destination. (In this code, package number 2. The loss is simulated in the client) <br>
## Solution
1. Client and server fix a random number 𝑑.
2. The client calculates 𝑒=𝑥𝜋1⊕𝑥𝜋2⊕⋯⊕𝑥𝜋𝑑 where the 𝜋𝑖 are the packet indexes.
3. The client sends a packet containing 𝑒 and the indexes as a payload in addition to each 𝑑 original packets. If a packet is missing it calculated using the already received packets.
