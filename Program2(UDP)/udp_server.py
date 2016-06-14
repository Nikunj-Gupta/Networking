import socket # Using the socket library

def capitalizer():
	host = "127.0.0.1" # stating the host
	port = 5000 # stating the port number
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating a new socket object
	s.bind((host,port)) # binding the tuple of (host,port) to the socket object s
	
	print "Server Started"
		
	while True:
		data, addr = s.recvfrom(1024)
		print "Data from: " + str(addr)
		print "Data: " + str(data)
		data = str(data).upper()
		print "Sending: " + str(data)
		s.sendto(data, addr)
	s.close()
	
if __name__ == "__main__":
	capitalizer()
