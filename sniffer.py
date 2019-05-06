from scapy.all import*

data = ""
oldData = ""

def getPacketData(packet):
	global data,oldData
	oldData = data
	try:
		data = packet[Raw].load
		if oldData != data:
			print("%s\n" % data)
	except:
		print("")

sniff(filter="udp port 12321", prn=getPacketData, store=0)

