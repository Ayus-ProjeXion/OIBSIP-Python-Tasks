#Project:CHAT APP
#Name:Ayusman Mishra
import socket
def main():
    print("Chat app by Ayusman ")
    print("1. Host a Server(wait for a message)")
    print("2. Connect a Client (send a message)")
    role=input("Chose your role(1 or 2 ): ")
    host='127.0.0.1'
    port=5005
    if role=="1":
        server =socket.socket()
        server.bind((host,port))
        server.listen(1)
        print("Server started.Waiting for a message")
        conn,addr=server.accept()
        print(f"Connection from: {addr}")
        data=conn.recv(1024).decode()
        print(f"Meassage recieved: {data}")
        conn.close()
    elif role=="2":
        client=socket.socket()
        client.connect((host,port))
        message=input("Type your message to the server: ") 
        client.send(message.encode()) 
        print("Message Sent!")
        client.close()
if __name__=="__main__":
    main()          
