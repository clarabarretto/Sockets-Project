import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 1980)

    try:
        client_socket.connect(server_address)
        print("Conexão estabelecida com o servidor")

        while True:
            mensagem = input('Digite a expressão desejada: ')
            client_socket.send(mensagem.encode('utf-8'))

            if (not mensagem or mensagem == 'Parar transmissão'):
                print('Você encerrou a transmissão')
                break

            response = client_socket.recv(1024)
            print(response.decode('utf-8'))

    except socket.error:
        print("Erro durante a execução")

    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
