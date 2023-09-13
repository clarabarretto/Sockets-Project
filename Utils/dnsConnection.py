import socket

def DNSrequest(url):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 1990)

    try:
        while True:
            client_socket.sendto(url.encode('utf-8'), server_address)
            print('Requisição para DNS feita')

            response, _ = client_socket.recvfrom(1024)

            parsed_response = int(response.decode('UTF-8'))
            print(f'Resposta DNS {parsed_response}')
            return parsed_response
    except socket.error:
        return ("Erro durante a execução")

    finally:
        client_socket.close()