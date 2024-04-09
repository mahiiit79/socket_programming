import socket
import threading
from cryptography.fernet import Fernet


# Generate a key for encryption and decryption
key = Fernet.generate_key()
# Create a Fernet object with the key
f = Fernet(key)

# Define the host and port for the server
host = "127.0.0.1"
port = 8500

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the host and port
s.bind((host, port))
# Listen for incoming connections
s.listen()

# Define a function to handle each client
def client_handler(conn, addr):
    # Send the key to the client
    conn.sendall(key)
# Receive the encrypted string from the client
    encrypted = conn.recv(1024)
# Decrypt the string using the Fernet object
    decrypted = f.decrypt(encrypted)
# Print the decrypted string
    print("Received from", addr, ":", decrypted.decode())
# Send the decrypted string back to the client
    conn.sendall(decrypted)
# Close the connection
    conn.close()

# Loop forever to accept new connections
while True:
    #Accept a connection from a client
    conn, addr = s.accept()
    # Print the address of the client
    print("Connected to", addr)
# Create a new thread to handle the client
    threading.Thread(target=client_handler, args=(conn, addr)).start()