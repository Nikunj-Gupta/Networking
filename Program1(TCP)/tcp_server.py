import socket # Using the socket library

def capitalizer():
	host = "127.0.0.1" # stating the host
	port = 5000 # stating the port number
	
	s = socket.socket() # creating a new socket object
	s.bind((host,port)) # binding the tuple of (host,port) to the socket object s
	
	s.listen(1) # Now the socket starts listening at but 1 connection at a time
	
	c, addr = s.accept()
	print "Connection from: " + str(addr)
	
	while True:
		data = c.recv(1024)
		if not data:
			break
		print "Data Recieved from Connected User: " + str(data)
		data = str(data).upper()
		print "New Data being Sent: " + str(data)
		c.send(data)
	c.close()
	
if __name__ == "__main__":
	capitalizer()
