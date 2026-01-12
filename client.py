import socket

def run_client():
    host = "localhost"
    port = 7500

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    print("Connected to Prasanth's Chat Server. Type 'bye' to exit.\n")

    while True:
        msg = input("Client: ")
        client.send(msg.encode())

        if msg.lower() == "bye":
            print("You ended the chat.")
            break

        reply = client.recv(1024).decode()
        if not reply:
            print("Server closed connection.")
            break

        print("Prasanth:", reply)
        if reply.lower() == "bye":
            print(" ended the chat.")
            break

    client.close()

if __name__ == "__main__":
    run_client()