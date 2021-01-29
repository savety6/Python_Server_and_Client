import socket

af = input("Local or public(1/2): ")
if af == "1":
    af = socket.AF_INET
elif af == "2":
    socket.AF_INET6
s = input("IP Addres : ")

HEADER = 64
PORT = 5050
SERVER = s
ADDR = (SERVER, PORT)

FORMAT  ="utf-8"
D_M = "MISS!"

client = socket.socket(af, socket.SOCK_STREAM)
client.connect(ADDR)

def send(_msg):
    massage = _msg.encode(FORMAT)
    msg_lenght = len(massage)
    send_lenght = str(msg_lenght).encode(FORMAT)
    send_lenght += b' ' * (HEADER - len(send_lenght))
    client.send(send_lenght)
    client.send(massage)
    print(client.recv(2048).decode(FORMAT))


while True:
    my_masage = input("[SEND MASSAGE]: ")
    if my_masage == "exit":
        send(D_M)
    else:
        send(my_masage)