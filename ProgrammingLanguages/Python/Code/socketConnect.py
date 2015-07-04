import socket;

s = socket.socket();
s.connect(("time-a.nist.gov",13));
banner = s.recv(1024);
print banner;
