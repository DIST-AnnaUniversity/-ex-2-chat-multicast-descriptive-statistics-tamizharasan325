import socket

def main():
    # Define host and port
    host = '127.0.0.1'
    port = 1234

    # Create socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    client_socket.connect((host, port))
    print(f"[*] Connected to {host}:{port}")

    while True:
        # Send message to server
        message = input("Enter your message: ")
        client_socket.send(message.encode())

        # Receive response from server
        response = client_socket.recv(1024)
        print("[Received] from server: ", response.decode())

    # Close connection
    client_socket.close()

if __name__ == "__main__":
    main()
