import socket
import cv2
import pickle
import struct
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def send_image_to_server(image, server_ip="127.0.0.1", server_port=9999):
    # Serialize the image using pickle
    data = pickle.dumps(image)
    size = len(data)

    # Create a socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    # Send the size of the image data first
    client_socket.send(struct.pack("L", size))  # Send the size (4 bytes)

    # Send the image data
    client_socket.sendall(data)

    # Receive the prediction from the server
    prediction = client_socket.recv(1024).decode()
    print(f"Prediction from server: {prediction}")

    # Close the connection
    client_socket.close()

def select_image_from_computer():
    # Use Tkinter to create a file dialog for image selection
    Tk().withdraw()  # Hide the root window of Tkinter
    file_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp")])
    
    if file_path:
        # Read the selected image
        image = cv2.imread(file_path)

        # Resize the image to match the model's input size (224x224)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
        return image
    else:
        print("No image selected.")
        return None

if __name__ == "__main__":
    # Select an image from the computer
    image = select_image_from_computer()

    if image is not None:
        send_image_to_server(image)
