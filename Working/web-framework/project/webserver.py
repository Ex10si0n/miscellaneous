import socket
import re
import multiprocessing
import framework.applications
from framework.config import *

class WSGIServer(object):
    def __init__(self):
        '''
        Initialize WSGIServer, Creating sockets
        :return: None
        '''
        self.tcpsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcpsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcpsocket.bind(("", port))
        self.tcpsocket.listen(128)

    def service(self, instsocket):
        '''
        Service clients host
        Retriving and sending documents
        :param instsocket:
        :return: None
        '''

        request = instsocket.recv(1024).decode("utf-8")
        request_lines = request.splitlines()
        print("[Server] New Connection Established.")
        print(request_lines[5])

        # GET /index.html HTTP/2.0
        file_name = ""
        retr = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
        if retr:
            file_name = retr.group(1)
            if file_name == "/":
                file_name = "/index.html"

        if not file_name.endswith(".py"):
            try:
                fi = open(template_dir + file_name, "rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
                fi_404 = open(template_dir + "/" + page_not_found, "r")
                response += fi_404.read()
                instsocket.send(response.encode("utf-8"))
            else:
                content = fi.read()
                fi.close()
                response = "HTTP/1.1 200 OK\r\n\r\n"
                instsocket.send(response.encode("utf-8"))
                instsocket.send(content)
        else:
            '''
            Dynamic Resources Request --> Handling Dynamic Resources
            Supporting WSGI Protocol
            '''
            env = dict()
            env['PATH_INFO'] = file_name
            body = framework.applications.application(env, self.set_response_header)
            header = "HTTP/1.1 %s\r\n" % self.status
            for h in self.headers:
                header += "%s:%s\r\n" % (h[0], h[1])
            header += "\r\n"

            response = header + body
            instsocket.send(response.encode("utf-8"))

        instsocket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [("Server", "WebServer")]
        self.headers += headers


    def run(self):
        '''
        Use for controlling and managing client connection
        :return: None
        '''

        while True:
            instsocket, clientaddr = self.tcpsocket.accept()
            proc = multiprocessing.Process(target=self.service, args=(instsocket,))
            proc.start()
            # Closing a reference of sub-process
            instsocket.close()

        self.tcpsocket.close()

def main():
    '''
    For controlling, Creating a web server instance
    :return: None
    '''
    server = WSGIServer()
    print("[Server] Welcome to use Mini Web Server")
    print("[Server] Server Running at", "127.0.0.1:%d" % port)
    server.run()


if __name__ == "__main__":
    main()
