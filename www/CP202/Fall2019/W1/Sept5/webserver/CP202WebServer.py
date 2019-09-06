import socket
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind(('', 8888))
listen_socket.listen(1)
while True:
    client_connection, client_address = listen_socket.accept()
    request_data = client_connection.recv(1024)
    http_response = b"""\
HTTP/1.1 200 OK

WLU - CP202 - Web Server
"""
    client_connection.sendall(http_response)
    client_connection.close()
