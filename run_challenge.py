from sys import argv
from socket import *
from subprocess import *

def get_s(port):
	print("[*] binding...")
	s = socket()
	s.bind(("0.0.0.0", port))
	s.listen(5)
	return s.accept()[0]

def execute(port):
	s = get_s(port)
	fds = [s,s,s]
	print("[*] exec tree.bin with fds: " + str(fds))
	Popen("./tree.bin",  stdin=s, stdout=s, stderr=s)
	
if __name__ == "__main__":
	port = int(argv[1]) if len(argv) > 1 else 1337
	execute(port)
