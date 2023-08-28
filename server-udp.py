import socket

def soma(a,b):
    return a + b

def main(): 
    # funções

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = ('localhost', 1960)
    server_socket.bind(server_address)

    print("UDP iniciado")

    while True:
        data,client_address = server_socket.recvfrom(1024)

        decoded_data = data.decode('utf-8')

        response = 'chegou'
        variables = 
                
        print(decoded_data)
        print(decoded_data.split('+'))
        server_socket.sendto(response.encode('utf-8'), client_address)

    server_socket.close()

if __name__ == "__main__":
    main()