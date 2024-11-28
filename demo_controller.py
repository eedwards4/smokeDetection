import socket

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


def controller():
    while True:
        command = input('Enter a command: ')
        if command == 'exit':
            break
        elif command == 'shutdown' or command == 'ping':
            send_command(command.upper())
        else:
            print('Invalid command. Please enter "shutdown", "ping" or "exit".')

    print('Exiting...')


if __name__ == '__main__':
    controller()