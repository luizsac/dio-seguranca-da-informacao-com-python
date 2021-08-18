import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # protocolo ipv4, protocolo tcp
    except socket.error as e:
        print("A conexão falhou!")
        print(f"Erro: {e}")
        sys.exit()
    
    print("Socket criado com sucesso!")

    target = input("Digite o host ou ip a ser conectado: ")
    port = input("Digite a porta a ser conectada: ")

    try:
        s.connect((target, int(port)))  # tupla contendo host e porta
        print(f"Cliente conectado com sucesso no host {target}, porta {port}")
        s.shutdown(2)
    except socket.error as e:
        print(f"Não foi possível conectar à porta {port} do host {target}")
        print(f"Erro: {e}")
        sys.exit()

if __name__ == "__main__":
    main()