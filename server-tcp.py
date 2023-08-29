import socket

def calculator(expression):
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Expressão inválida"

def main():
    server_address = ("localhost", 1980)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)  # Define o número máximo de conexões pendentes

    print("TCP iniciado")

    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Conexão estabelecida com o cliente({client_address})")

            while True:
                data = client_socket.recv(1024)
                decoded_data = data.decode("utf-8")

                if (not data or decoded_data == 'Parar transmissão'):
                    print("Conexão encerrada")
                    break

                response = calculator(decoded_data)
                client_socket.send(response.encode('utf-8'))

                if response != "Expressão inválida":
                    print(f"A expressão inserida foi: {decoded_data}")
                    print(f"O resultado da expressão é: {response}")

            client_socket.close()

    except socket.error:
        print("Erro durante a execução")

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
