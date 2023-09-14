import socket
import time

from Utils.dnsConnection import DNSrequest

def init():
    port = DNSrequest('calculadoraTCP')
    main(port)

def main(port):
    instructions = [  
        '2+2',
        '18+16',
        '17*15',
        '20/5',
        '13+22',
        'Parar transmissão'
    ]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', port)

    try:
        client_socket.connect(server_address)
        print("Conexão estabelecida com o servidor")

        for instruction in instructions:
            initial_time = time.time()
            client_socket.send(instruction.encode('utf-8'))

            if (instruction == 'Parar transmissão'):
                print('Você encerrou a transmissão')
                break

            response = client_socket.recv(1024)
            final_time = time.time()

            print(response.decode('utf-8'))

            time_diff = final_time - initial_time

            print(time_diff, 'Time diff')

    except socket.error:
        print("Erro durante a execução")

    finally:
        client_socket.close()

if __name__ == "__main__":
    init()
