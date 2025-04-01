# TensorFlow Image Classification Server

This repository contains a Python-based server for performing image classification using a pre-trained TensorFlow model. The server processes images sent from a client, classifies them using TensorFlow, and sends the classification result back to the client. This setup is ideal for integrating edge AI applications, where the server performs real-time image classification, and the client handles image capture and display.

## Features

- **Image Classification with TensorFlow:** The server uses a pre-trained TensorFlow model (e.g., MobileNetV2) to classify images.
- **Client-Server Communication:** The system supports communication over TCP sockets, allowing the client to send images to the server for classification and receive results back.
- **Real-time Processing:** The server processes images in real-time, making it ideal for applications that require quick decision-making based on visual data.
- **Scalable Architecture:** This architecture can be extended to support additional AI applications and integrated with biometric authentication systems or other machine learning tasks.

## Getting Started

To run the TensorFlow classification server and client, follow the steps below:

### Prerequisites

- **Python 3.x** (preferably 3.8 or higher)
- **TensorFlow 2.1 or higher** for AI image classification
- **OpenCV** for image processing and capturing images on the client-side
- **NumPy** for efficient array operations
- **Socket programming** for server-client communication

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jamesql/tensorflow-classification-server.git
   cd tensorflow-classification-server
   ```

2. Install requirements
   ```bash
   pip install -r requirements.txt
   ```
This will install:

- `tensorflow==2.1` for image classification

- `opencv-python` for image capture and processing

- `numpy` for array manipulation

- `socket` for server-client communication

Usage
1. Start the Server
The server runs a socket listener to receive images, classify them, and send back the results. To start the server:

```bash
python server.py
The server will listen on a predefined IP address and port (typically localhost and port 5000 by default). You can modify these settings in the script as needed.
```

2. Start the Client
The client captures an image (using OpenCV), sends it to the server for classification, and displays the result.

```bash
python client.py
The client will capture an image (e.g., from the webcam) and send it to the server. The server will classify the image using a pre-trained TensorFlow model, and the classification result will be displayed on the client-side.
```
