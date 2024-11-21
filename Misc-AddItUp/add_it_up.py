import socket
import nclib
import random
import threading
import time

# Predefined list of questions
questions = [
    "What is the capital of France?",
    "What is 5 + 7?",
    "Name a programming language that starts with 'P'.",
    "What color is the sky on a clear day?",
    "Who wrote 'To Kill a Mockingbird'?",
    "What is the square root of 64?",
    "What is the chemical symbol for water?",
    "Name a planet in our solar system.",
    "What is 10 * 10?",
    "What is the boiling point of water in Celsius?"
]


def handle_client(client_socket):
    client = nclib.Netcat(sock=client_socket)  # Wrap socket with nclib.Netcat
    try:
        #client.send(b"Welcome to the Question Server!\n")
        client.send(b"How many questions would you like to answer? ")

        # Receive user input and convert to integer
        questions = int(client.recv().decode('utf-8').strip())

       # client.send(f"Great! You will answer {num_questions} question(s).\n".encode('utf-8'))
        for i in range(questions):
            x = random.randint(0, 10)
            y = random.randint(0, 10)

            client.send(f"What is {x} + {y}? ".encode('utf-8'))
            answer = client.recv().decode('utf-8').strip()
            client.send(f"calculating\n".encode('utf-8'))
            totaltime = pow(2, i)
            client.send(f"...\n".encode('utf-8'))
            time.sleep(totaltime / 3)
            client.send(f"...\n".encode('utf-8'))
            time.sleep(totaltime / 3)
            client.send(f"...\n".encode('utf-8'))
            time.sleep(totaltime / 3)

            if int(answer) != x + y: 
                client.send(f"I weep for the future 😭\n".encode('utf-8'))
                exit(69)
            #client.send(f"Your answer: {answer}\n".encode('utf-8'))

        f = open('./flag.txt', 'r')
        flag = f.read()
        client.send(f'\n{flag[:questions]}\n')
    except Exception as e:
        client.send(f"An error occurred: {e}\n".encode('utf-8'))
    finally:
        client.close()

def main():
    # Create a raw socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))
    server_socket.listen(5)  # Allow up to 5 pending connections
    print("Server is listening on port 5000...")

    try:
        while True:
            # Accept a new client connection
            client_socket, addr = server_socket.accept()
            print(f"New client connected from {addr}")

            # Handle client in a new thread
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("\nShutting down server.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()

