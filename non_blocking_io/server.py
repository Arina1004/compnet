import select
import socket

SERVER_ADDRESS = ('localhost', 8080)

MAX_CONNECTIONS = 4


INPUTS = list()
OUTPUTS = list()


def get_non_blocking_server_socket():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(0)

    server.bind(SERVER_ADDRESS)


    server.listen(MAX_CONNECTIONS)

    return server


def handle_readables(readables, server):

    for resource in readables:

        if resource is server:
            connection, client_address = resource.accept()
            connection.setblocking(0)
            INPUTS.append(connection)
            print("new connection from {address}".format(address=client_address))

        else:
            data = ""
            try:
                data = resource.recv(1024).decode('utf-8')

            except ConnectionResetError:
                pass

            if data:

                print("getting data: {data}".format(data=str(data)))

                if resource not in OUTPUTS:
                    OUTPUTS.append(resource)

            else:

                clear_resource(resource)


def clear_resource(resource):

    if resource in OUTPUTS:
        OUTPUTS.remove(resource)
    if resource in INPUTS:
        INPUTS.remove(resource)
    resource.close()

    print('closing connection ' + str(resource))


def handle_writables(writables):

    for resource in writables:
        try:
            resource.send(bytes('Hello from server!', encoding='UTF-8'))
        except OSError:
            clear_resource(resource)


if __name__ == '__main__':

    server_socket = get_non_blocking_server_socket()
    INPUTS.append(server_socket)

    print("server is running, please, press ctrl+c to stop")
    try:
        while INPUTS:
            readables, writables, exceptional = select.select(INPUTS, OUTPUTS, INPUTS)
            handle_readables(readables, server_socket)

    except KeyboardInterrupt:
        clear_resource(server_socket)
        print("Server stopped! Thank you for using!")