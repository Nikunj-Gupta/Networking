import socket

def Client():
	host = "127.0.0.1"
	port = 5001 # Different port number because we are technically setting up another server
	
	server = ("127.0.0.1", 5000)
	
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect((host,port))
	
	message = raw_input("Enter Message: ")
	while (message != 'q'):
		s.sendto(message, server)
		data, addr = s.recvfrom(1024)
		print "Message recieved from Server: " + str(data)
		message = raw_input("Enter New Message: ")
	s.close()
	
if __name__ == "__main__":
	Client()
