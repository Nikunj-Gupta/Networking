import socket

def Client():
	host = "127.0.0.1"
	port = 5000
	
	s = socket.socket()
	s.connect((host,port))
	
	message = raw_input("Enter Message: ")
	while (message != 'q'):
		s.send(message)
		data = s.recv(1024)
		print "Message recieved from Server: " + str(data)
		message = raw_input("Enter New Message: ")
	s.close()
	
if __name__ == "__main__":
	Client()
