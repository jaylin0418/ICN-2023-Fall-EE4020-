import socket
from datetime import datetime

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

def pow(a,b):
    answer = 1
    for i in range(b):
        answer = answer * a
    return answer

# Function to calculate the expression
def calculate_expression(expression):
    if '+' in expression:
        l = expression.split('+')
        return str(float(l[0])+float(l[1]))
    elif '-' in expression:
        l = expression.split('-')
        return str(float(l[0])-float(l[1]))
    elif '*' in expression:
        l = expression.split('*')
        return str(float(l[0])*float(l[1]))
    elif '/' in expression:
        l = expression.split('/')
        return str(float(l[0])/float(l[1]))
    elif '%' in expression:
        l = expression.split('%')
        return str((float(l[0])%float(l[1])))
    elif '^' in expression:
        l = expression.split('^')
        return str(pow(int(l[0]),int(l[1])))
    elif '!' in expression:
        l = expression.split('!')
        return str(factorial(int(l[0])))
    elif 'P' in expression:
        l = expression.split('P')
        return str(factorial(int(l[0]))/factorial(int(l[0])-int(l[1])))
    elif 'C' in expression:
        l = expression.split('C')
        return str(factorial(int(l[0]))/(factorial(int(l[0])-int(l[1]))*factorial(int(l[1]))))

# Server setup
# Specify the IP address and port number (Use "127.0.0.1" for localhost on local machine)
# TODO Start
HOST, PORT = "127.0.0.1", 6071

# TODO end

with open('./server_log.txt', 'w') as logFile:
    # 1. Create a socket
    # 2. Bind the socket to the address
    # TODO Start
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((HOST, PORT))
    # TODO End

    while True:
        # Listen to a new request with the socket
        # TODO Start
        serverSocket.listen(0)
        # TODO End

        now = datetime.now()
        print("The Server is running..")
        logFile.write(now.strftime("%H:%M:%S ") + "The Server is running..\n")
        logFile.flush()


        # Accept a new request and admit the connection
        # TODO Start
        client, address = serverSocket.accept()
        # TODO End

        client.settimeout(15)
        print(str(address) + " connected")
        now = datetime.now()
        logFile.write(now.strftime("%H:%M:%S ") + "connected " + str(address) + '\n')
        logFile.flush()

        try:
            while True:
                client.send(b"Please input a question for calculation")

                #client 就是 connection socket
                # Recieve the data from the client
                # TODO Start
                question = client.recv(4096).decode()
                # TODO End

                now = datetime.now()
                logFile.write(now.strftime("%H:%M:%S ") + question + '\n')
                logFile.flush()

                # TODO: Call the calculate_expression function here
                ans = calculate_expression(question)

                # Ask if the client want to terminate the process
                message = f"{ans}\nDo you wish to continue? (Y/N)"


                # Send the answer back to the client
                # TODO Start
                client.send(message.encode())
                anse = client.recv(4096).decode()
                # TODO End

                # Terminate the process or continue
                if anse.lower() != 'y':
                    break
        except ConnectionResetError:
            print("Connection reset by peer")
            logFile.write("Connection reset by peer\n")
            logFile.flush()
        except Exception as e:
            print("An error occurred:", e)
            logFile.write(f"An error occurred: {e}\n")
            logFile.flush()

        client.close()
logFile.close()
