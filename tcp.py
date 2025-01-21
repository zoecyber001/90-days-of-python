   
import socket
import threading

# Function to handle client connections
def handle_client(client_socket):
    # Receive data from the client
    request = client_socket.recv(1024).decode('utf-8')
    print(f"Received: {request}")
    
    # Send a response back to the client
    response = "Message received!"
    client_socket.send(response.encode('utf-8'))
    
    # Close the client connection
    client_socket.close()

# TCP Server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9998))  # Bind to localhost on port 9998
    server.listen(5)  # Listen for incoming connections
    print("Server listening on port 9998...")
    
    while True:
        client_socket, addr = server.accept()  # Accept a new connection
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()  # Handle the client in a new thread

# TCP Client
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9998))  # Connect to the server
    client.send("Hello, Server!".encode('utf-8'))  # Send a message to the server
    response = client.recv(4096).decode('utf-8')  # Receive the response
    print(f"Server response: {response}")
    client.close()  # Close the connection

if __name__ == "__main__":
    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()
    
    # Start the client
    start_client()
