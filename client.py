import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive message from client
        request = client_socket.recv(1024)
        if not request:
            break
        print("[Received] from client: ", request.decode())

        # Send message to client
        response = input("Enter your response: ")
        client_socket.send(response.encode())

    # Close connection with client
    client_socket.close()

def main():
    # Define host and port
    host = '127.0.0.1'
    port = 1234

    # Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind socket to address
    server_socket.bind((host, port))

    # Start listening for incoming connections
    server_socket.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        # Accept connection from client
        client_socket, client_address = server_socket.accept()
        print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

        # Create client thread to handle communication
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()

