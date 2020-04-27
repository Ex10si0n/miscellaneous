import socket

def returnData(new_socket):
    # Get index.html
    index = open("index.html")
    # 1. Recv Browser's Request (HTTP Request)
    # GET / HTTP/1.1
    request = new_socket.recv(1024)
    print(request)

    # 2. Return data which format is HTTP to Browser
    # 2.1 header
    response = "HTTP/1.1 200 OK\r\n" + "\r\n"
    # 2.2 body
    response += index.read()
    new_socket.send(response.encode("utf-8"))
    # Close Socket
    new_socket.close()

def main():
    # Create Socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind
    tcp_server_socket.bind(("", 9002))
    # Listen Socket
    tcp_server_socket.listen(128)
    while True:
        # Wait for client to establish link
        new_socket, client_addr = tcp_server_socket.accept()
        # service for client
        returnData(new_socket)
    tcp_server_socket.close()
    
if __name__ == '__main__':
    main()
