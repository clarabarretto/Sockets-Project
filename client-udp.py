import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = ('localhost', 1960)

    while True:
        mensagem = input()
        client_socket.sendto(mensagem.encode('utf-8'), server_address)

        response, server_address = client_socket.recvfrom(1024)
        
if __name__ == "__main__":
    main()