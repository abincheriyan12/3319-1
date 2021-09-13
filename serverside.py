#Abin Cheriyan
#Cis 3319 - Project 1
from des import DesKey
import socket

#created the socket
soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
#binded socket to address
soket.bind(('', port))
soket.listen(10)
#reading the key in
with open("key", "r") as f:
    des_key = f.read()

key = DesKey(des_key.encode('utf-8')) #create key
print(" Server is running............ yayy")
conn, addr = soket.accept() #accept connection request
print(" Accepted new connection from %s " % (str(addr)))
conn.send(str(" Connection has been established! ").encode())

while True:
    recieve = conn.recv(1024)
    print("*" * 30)
    print(" Recieved ciphertext is: %s" % recieve.decode('utf-8', 'ignore'))
    pt = key.decrypt(recieve, padding = True).decode() #decrypt the key
    print(" Recieved plaintext is: %s " % pt)
    print("*" *30)
    if pt == "bye": #Bye breaks and closes the connection
        break
    message = input("type your message: ")
    ct = key.encrypt(message.encode('utf-8'), padding=True)
    print("*" *30)
    print(" Key is ", des_key)
    print(" Plaintext is: %s " % message)
    print(" Ciphertext is: %s " % ct.decode('utf-8', 'ignore'))
    print("*" * 30)
    conn.send(ct) #sending the ciphertext
conn.close()

