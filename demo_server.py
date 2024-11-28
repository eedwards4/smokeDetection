# Imports
import sys
import torch
import socket
from torch import cuda
from ultralytics import YOLO
from PIL import Image
from io import BytesIO


def loader():
    # Load the model
    model = YOLO('./models/model.pt')
    return model


def recognize(image, model):
    # Perform object detection
    results = model(image)
    detected_smoke = False
    detected_fire = False
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            class_name = result.names[class_id]
            if class_name == 'smoke':
                detected_smoke = True
            elif class_name == 'fire':
                detected_fire = True

    return detected_fire, detected_smoke


def is_image(data):
    image_sigs = [
        b'\xFF\xD8\xFF',  # JPG
        b'\x89\x50\x4E\x47',  # PNG
    ]
    return any(data.startswith(sig) for sig in image_sigs)


def start_server():
    print("Starting up...")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)
    print("Listening on {host}:{port}".format(host='localhost', port=5000))

    while True:
        client_socket, addr = server_socket.accept()
        print("Connection from {addr}".format(addr=addr))

        data = b''
        while True:
            chunk = client_socket.recv(1024)
            if not chunk or b"<END>" in chunk:
                data += chunk.replace(b"<END>", b"")  # Remove delimiter
                break
            data += chunk

        print('Data received')

        if is_image(data):
            print("Received an image. Recognizing...")
            fire, smoke = recognize(Image.open(BytesIO(data)), loader())
            if fire and smoke:
                print("Fire and smoke detected")
                client_socket.sendall(b'FIRE_SMOKE')
            elif fire:
                print("Fire detected")
                client_socket.sendall(b'FIRE')
            elif smoke:
                print("Smoke detected")
                client_socket.sendall(b'SMOKE')
            else:
                print("No fire or smoke detected")
                client_socket.sendall(b'NONE')
        else:
            command = data.decode('utf-8')
            print("Received command: {command}".format(command=command))
            if command == 'PING':
                client_socket.sendall(b'PONG')
            elif command == 'SHUTDOWN':
                print("Shutting down...")
                client_socket.sendall(b'Shutting down...')
                client_socket.close()
                server_socket.close()
                print("Connection closed")
                sys.exit(0)
            else:
                print("Invalid command: {command}".format(command=command))
                client_socket.sendall(b'Invalid command')

        client_socket.close()
        print("Connection closed")


if __name__ == '__main__':
    start_server()
