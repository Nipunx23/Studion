import time, socket, sys

def run():
    print("\nWelcome to Chat Room\n")
    print("Initialising....\n")
    time.sleep(1)

    s = socket.socket()
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    port = 2006
    s.bind((host, port))
    name = input(str("Enter your name: "))
            
    s.listen(1)
    print("\nWaiting for incoming connections...\n")
    conn, addr = s.accept()
    print("Received connection from ", addr[0], "(", addr[1], ")\n")

    s_name = conn.recv(1024)
    s_name = s_name.decode()
    print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
    conn.send(name.encode())

    while True:
        message = input(str("Me : "))
        if message == "[e]":
            message = "Left chat room!"
            conn.send(message.encode())
            print("\n")
            break
        conn.send(message.encode())
        message = conn.recv(1024)
        message = message.decode()
        print(s_name, ":", message)

if __name__ == "__main__":
     run()