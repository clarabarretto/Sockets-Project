import socket

services = {
    'calculadoraUDP': 1960,
    'calculadoraTCP': 1980
}
    
def main():
    server_address = ("localhost", 1990)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(server_address)

    print("DNS iniciado")
    try:
        while True:
            data, client_address = server_socket.recvfrom(1024)

            service_url = data.decode("utf-8")

            print(service_url)

            if (service_url not in services):
                response = 'Serviço não encontrado'
                server_socket.sendto(response.encode('utf-8'), client_address)
                continue

            service_port = services[service_url]
            server_socket.sendto(str(service_port).encode('utf-8'), client_address)
            break
    except socket.error:
        return "Erro durante a execução"

    finally:
        server_socket.close()
        print("DNS finalizdo")

if __name__ == "__main__":
    main()
