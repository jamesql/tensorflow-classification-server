import socket
import tensorflow as tf
import numpy as np
import cv2
import pickle
import struct

# Load a pre-trained model (MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights="imagenet")

def handle_client(client_socket):
    while True:
        # Receive the size of the image
        image_size_data = client_socket.recv(4)
        print(image_size_data)
        if len(image_size_data) < 4:
            print("Error receiving image size")
            break

        image_size = struct.unpack("L", image_size_data)[0]
        print(image_size)

        # Receive the image data itself
        data = b""
        while len(data) < image_size:
            data += client_socket.recv(4096)
        
        # Deserialize the image data (deserialize the bytes)
        image = pickle.loads(data)

        # Process the image (resize and preprocess for the AI model)
        image = cv2.resize(image, (224, 224))  # Resize to the model's expected input size
        image = tf.keras.applications.mobilenet_v2.preprocess_input(image)  # Preprocess image
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Get predictions from the model
        predictions = model.predict(image)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions)

        # Send the predictions back to the client (send top label)
        result = decoded_predictions[0][0][1]  # Get the label of the top prediction
        client_socket.send(result.encode())

    client_socket.close()

def start_server(host="0.0.0.0", port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server started at {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection from {addr}")
        handle_client(client_socket)

if __name__ == "__main__":
    start_server()