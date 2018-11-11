import socket
import ssl

PORT =  9750
HOST = socket.gethostbyname(socket.gethostname())

"""SSL context for secured connections, we are not using any special certificate loading only the default certificates"""
sslcontext = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
"""the bob.crt certificate file and bob.key private key are downloaded from the internet whose private key are open to world use only for learning purpose """
sslcontext.load_cert_chain("D://python//webserver//bob.crt", "D://python//webserver//bob.key")

"""We are creating a socket using the command socket.socket(socket_family, socket_type, protocol=0)
The AF_INET is Address Family, are addresses in the internet or network, Sock_Stream is streaming of data as used in the TCP connection"""
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
listen_socket_ssl = sslcontext.wrap_socket(listen_socket,server_side=True)
print ('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket_ssl.accept()
    request = client_connection.recv(1024)
    print (request)

    http_response = """\
HTTP/1.1 200 OK

Hello, World! Simple webserver for learning purpose
"""

    client_connection.sendall(http_response.encode())
    client_connection.close()