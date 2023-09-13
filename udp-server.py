import socket
from Services.calculator import calculator

def main():
    server_address = ("localhost", 1960)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)

    print("UDP iniciado")
    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)
            decoded_data = data.decode("utf-8")

            if (not data or decoded_data == 'Parar transmissão'):
                print("Conexão encerrada")
                break

            response = calculator(decoded_data)
            server_socket.sendto(response.encode('utf-8'), client_address)

            if response != "Expressão inválida":
                print(f"A expressão inserida foi: {decoded_data}")
                print(f"O resultado da expressão é: {response}")

    except socket.error:
        return "Erro durante a execução"

    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
