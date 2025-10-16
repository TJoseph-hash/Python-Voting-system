from socket import *
ServerName = "127.0.0.1"
ServerPort = 12004
ClientSocket = socket(AF_INET,SOCK_DGRAM)

file1= open("votes.txt")
## file2 = open("response.txt")


print("Name: Tishawn Joseph")
print("Student ID: 816042378")



try:
    with open("votes.txt", "r") as file1:
        lines = file1.readlines()
        if not lines:
            print("End of file — no data to process.")
        else:
            print("\nFile is being processed...\n")

            for line in lines:
                name = line.strip()
                if name == "":
                    continue  # Skip empty lines
                
                # Send name to the server
                ClientSocket.sendto(bytes(name, "utf-8"), (ServerName, ServerPort))
                print("Sent to Voting system:", name)

                # Receive server’s response
                modifiedMessage, serverAddress = ClientSocket.recvfrom(2048)
                print(f"Received back from voting server: {modifiedMessage.decode()}\n")

 

finally:
    file1.close()
    ClientSocket.close()