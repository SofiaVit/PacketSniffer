import socket
import random
import time

DATA = "The moon has a face like the clock in the hall; She shines on thieves on the garden wall,On streets and fields and harbour quays,And birdies asleep in the forks of the trees.The squalling cat and the squeaking mouse,The howling dog by the door of the house,The bat that lies in bed at noon,All love to be out by the light of the moon.But all of the things that belong to the dayCuddle to sleep to be out of her way;And flowers and children close their eyesTill up in the morning the sun shall arise."


e = ""
d = random.randint(2,(len(DATA))/100)
previousLine = ""

new_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ("localhost", 12321)

linesToSend = [DATA[i:i+100] for i in range(0, len(DATA), 100)]

randomNumber = ("random=%d" % d)

new_socket.sendto(randomNumber,server)

i = 1
previousD = 0

while True:
	for line in linesToSend:
		sendLine = "Packet number:%d,Data: %s" % (i, line)
		if i == previousD+1:
			e = line
		if i != 2:
			new_socket.sendto(sendLine, server)
		if i != previousD+1:
			e = ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(e,line))
		if i - d == 0:
			previousD = d
			d = d*2
			e += ("NUMBERS%d" % i)
			new_socket.sendto(e,server)
			e = ""				
		i = i + 1	
		time.sleep(3.0)
new_socket.close()
