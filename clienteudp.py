import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # protocolo ipv4, protocolo udp

print("Socket criado com sucesso!")

host = "localhost"
port = 5433
message = "Hello again, friend of a friend"

try:
    s.sendto(message.encode(), (host, 5432))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f"Cliente: {data}")
except socket.error as e:
    print("Erro na conexão!")
    print(f"Erro: {e}")
finally:
    print("Cliente fechando a conexão")
    s.close()