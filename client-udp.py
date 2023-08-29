import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 1960)

    try:
        while True:
            mensagem = input('Digite a expressão desejada: ')
            client_socket.sendto(mensagem.encode('utf-8'), server_address)

            if (not mensagem or mensagem == 'Parar transmissão'):
                print('Você encerrou a transimmsão')
                break

            response, _ = client_socket.recvfrom(1024)
            print(response.decode('utf-8'))

    except socket.error:
        return ("Erro durante a execução")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()