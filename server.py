

import socket

def run_server():
    host = "localhost"
    port = 7500

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(1)

    print("Prasanth's Chat Server is running. Waiting for connection...")

    conn, addr = server.accept()
    print("Connected to", addr)

    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            print("Client disconnected.")
            break
        if msg.lower() == "bye":
            print("Chat ended by Client.")
            break

        print("Client:", msg)
        reply = input("Prasanth: ")
        conn.send(reply.encode())
        if reply.lower() == "bye":
            print("Chat ended by Prasanth.")
            break

    conn.close()
    server.close()

if __name__ == "__main__":
    run_server()