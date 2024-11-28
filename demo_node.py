import time
import socket
# Additional imports go here


# Sends an image to the server
def send_image(image, host='localhost', port=5000):
    print("Sending image...")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(image + b"<END>")
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from server: {response}")
    except ConnectionRefusedError:
        print("Error: Could not connect to the server.")
    except Exception as e:
        print(f"Error: {e}")


def send_command(command, host='localhost', port=5000):
    print(f"Sending command: {command}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            client_socket.sendall(command.encode('utf-8') + b"<END>")
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Response from server: {response}")
    except ConnectionRefusedError:
        print("Error: Could not connect to the server.")
    except Exception as e:
        print(f"Error: {e}")


# DEMO ONLY: Load an image from a file
def load_image(image_path):
    with open(image_path, 'rb') as f:
        return f.read()


# DEMO ONLY: Send a few images to the server
def demo():
    demo_path = './demo_images/'
    image_paths = [
        demo_path + 'forest.jpg',
        demo_path + 'firecanada.jpg',
        demo_path + 'notSmoke.jpg',
        demo_path + 'fireGirlMeme.jpg'
    ]

    print('Starting demo...')

    for image in image_paths:
        image_data = load_image(image)
        send_image(image_data)
        time.sleep(10)

    print('Demo complete.')
    print('Shutting down server')
    send_command('SHUTDOWN')
    print('Exiting...')
    exit(0)


if __name__ == '__main__':
    demo()
