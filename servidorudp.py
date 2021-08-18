import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # protocolo ipv4, protocolo udp

print("Socket criado com sucesso!")

host = "localhost"
port = 5432
message = "\nServidor: I knew you when our common goal was waiting for the world to end"

s.bind((host, port))

while True:
    data, end = s.recvfrom(4096)
    if data:
        print("Servidor enviando mensagem...")
        s.sendto(data + (message.encode()), end)