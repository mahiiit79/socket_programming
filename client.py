# Import the cryptography module
from cryptography.fernet import Fernet
# client.py
import socket


# Define the host and port of the server
host = "127.0.0.1"
port = 8500

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect to the server
s.connect((host, port))
# Receive the key from the server
key = s.recv(1024)
# Print the key
print("Key:", key)


# Create a Fernet object with the key
f = Fernet(key)

# Ask the user to enter a string
string = input("Enter a string: ")
# Encode the string to bytes
string = string.encode()
# Encrypt the string using the Fernet object
encrypted = f.encrypt(string)
# Print the encrypted string
print("Encrypted:", encrypted)
# Send the encrypted string to the server
s.sendall(encrypted)
# Receive the decrypted string from the server
decrypted = s.recv(1024)
# Print the decrypted string
print("Decrypted:", decrypted.decode())
# Close the socket
s.close()