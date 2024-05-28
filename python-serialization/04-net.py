import socket
import json
import threading
import time

def start_server(host='localhost', port=65432):
    """
    Function to start the server, which listens for incoming connections,
    receives a serialized dictionary, deserializes it, and prints it.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    with conn:
        data = conn.recv(1024)
        if data:
            received_dict = json.loads(data.decode('utf-8'))
            print("Received Dictionary from Client:")
            print(received_dict)

    server_socket.close()

def send_data(dictionary, host='localhost', port=65432):
    """
    Function to send a serialized dictionary to the server.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    serialized_data = json.dumps(dictionary).encode('utf-8')
    client_socket.sendall(serialized_data)

    client_socket.close()

# For testing purposes
if __name__ == "__main__":
    def main():
        # Start the server in a separate thread
        server_thread = threading.Thread(target=start_server)
        server_thread.start()

        # Give server some time to start listening
        time.sleep(1)

        # Run the client to send data
        sample_dict = {
            'name': 'Alice',
            'age': 30,
            'city': 'Paris'
        }
        send_data(sample_dict)

        # Ensure server thread ends
        server_thread.join()

    main()
