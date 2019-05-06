import SocketServer
import datetime
import time
import re

d = 0
e = ""
PacketsSended = []
MessagesAccepted = []

def findMissingPacket(e):
	global PacketsSended
	lastPacket = int(e.split('NUMBERS', 1)[1])
	for x in range((lastPacket-d)+1,lastPacket+1):
		if x not in PacketsSended:
			print("\nPacket number %d is missing" % x)
			getMissingPacket(e,x,lastPacket)

def getMissingPacket(e,missingPacket,lastPacket):
	global PacketsSended,MessagesAccepted
	e = e[:e.index("NUMBERS")]
	start = 0
	end = 0
	if missingPacket != (lastPacket-d)+1:
		start = (lastPacket-d)+1		
	else:
		start = (lastPacket-d)+2
	if missingPacket != lastPacket:
		end = lastPacket
	else:
		end = lastPacket-1
	start = PacketsSended.index(start)
	end = PacketsSended.index(end)
	AllPackets = ""
	for x in range(start,end+1):
        	e = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(MessagesAccepted[x],e))
	print("Missing Data = %s\n" % e)		
		


class Echo(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
	pass


class EchoHandler(SocketServer.DatagramRequestHandler):


    def handle(self):
	global PacketsSended,MessagesAccepted,d,e
        print("accept connection from %s" % self.client_address[0])
        while True:
            line = self.rfile.readline()
            if not line:
                break
	    if line.startswith("random="):
		print("data recieved from client:\n%s" % line.rstrip())
		d = int(line.split("random=", 1)[1])
	    elif line.startswith("Packet number:"):
		print("data recieved from client:\n%s" % line.rstrip())
		result = line.split("Packet number:",1)[1]
		PacketsSended.append(int(result[:result.index(",")]))
		MessagesAccepted.append(line.split("Data: ",1)[1])		
	    elif "NUMBERS" in line:
		print("data recieved from client:\n%s" % line.rstrip())
		e += line
		completeE = e
		e = ""
		findMissingPacket(completeE)
	    else:
                e += line
		print("data recieved from client:\n%s" % line.rstrip())
            self.wfile.write(line)
	    print("Client send data at time:%s" % datetime.datetime.now().time())
        print("%s disconnected\n" % self.client_address[0])


networkService = Echo(("localhost", 12321), EchoHandler)
print("Network service listens on %s:%s" % networkService.server_address)
networkService.serve_forever()
