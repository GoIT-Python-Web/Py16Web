import socket


def main():
    host = socket.gethostname()
    port = 4000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen()

    conn, address = server_socket.accept()
    print(f"Connection from {address}")
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break
        print(f"Received message {msg}")
        message = input('>>> ')
        conn.send(message.encode())
    conn.close()
    server_socket.close()


if __name__ == '__main__':
    main()
