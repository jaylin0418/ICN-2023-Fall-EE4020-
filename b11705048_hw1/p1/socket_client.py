import socket
import time

# ANSI escape codes for colors
RED = '\033[91m'
RESET = '\033[0m'

def log_message(logFile, message, color=RESET):
    formatted_message = color + message + RESET
    print(formatted_message)
    logFile.write(message + '\n')  # Write the unformatted message to the log file
    logFile.flush()

with open('./b11705048_p1_client_result.txt', 'w') as logFile:
    log_message(logFile, "The Client is running..")

    # Configure the server IP with its corrosponding port number
    # Specify the TCP connection type and make connection to the server
    # TODO Start
    HOST, PORT = "127.0.0.1", 6071
    #HOST, PORT = "140.112.42.104" ,7777
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    # TODO End


    # You can change the test case or create other test cases on your own
    with open('./p1_testcase_b5', 'r') as Testcase:
        for PreprocessingLine in Testcase:
            line = PreprocessingLine.strip()
            time.sleep(3)

            if line == "Y" or line == "N":
                # If the line is "Y" or "N", treat it as a response to a server prompt
                response = line
                log_message(logFile, "Response to server prompt: " + response)
                
                
                # Send the response to the server
                # TODO Start
                s.send(response.encode())
                # TODO End
            else:
                # If not "Y" or "N," assume it's a mathematical expression
                question = line
                #log_message(logFile, "Question: " + question)

                
            
                # Receive the server's message
                # TODO Start
                server_message = s.recv(4096).decode()
                # TODO End

                # Log the server's message
                log_message(logFile, "Received the message from server: ", RESET)
                log_message(logFile, server_message, RED)
                
                log_message(logFile, "Question: " + question)


                # Send the question to the server
                # TODO Start
                s.send(question.encode())
                # TODO End

                # Receive and log the answer from the server
                # TODO Start
                ans = s.recv(4096).decode()
                # TODO End

                log_message(logFile, "Get the answer from server: ", RESET)
                log_message(logFile, ans, RED)

    s.close()
logFile.close()