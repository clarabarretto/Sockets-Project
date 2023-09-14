import socket
import time

from Utils.dnsConnection import DNSrequest

def init():
    port = DNSrequest('calculadoraUDP')
    print(port, 99999999999)
    main(port)

def main(port):
    instructions = [  
        '(2+2)/2*18',
        '18+16-13+26*40',
        '(17*15/5)*20',
        '20/5+45',
        '13+22+12+4+25-100',
        'Parar transmissão'
    ]

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', port)

    try:
        for instruction in instructions:
            initial_time = time.time()
            client_socket.sendto(instruction.encode('utf-8'), server_address)

            if (instruction == 'Parar transmissão'):
                print('Você encerrou a transmissão')
                break

            response, _ = client_socket.recvfrom(1024)
            final_time = time.time()

            print(response.decode('utf-8'))

            time_diff = final_time - initial_time

            print(time_diff, 'Time diff')
    except socket.error:
        return ("Erro durante a execução")

    finally:
        client_socket.close()

if __name__ == "__main__":
    init()