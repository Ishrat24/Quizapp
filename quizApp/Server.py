import socket
import threading
import dframe as df
from threading import Thread
from dframe import *

lock = threading.Lock()


def client_thread(connection):
    data = connection.recv(1024)  # receiving participant details            #2

    # verifyIdPassword participant details here
    log = (data.decode()).split(' ')
    log[0] = int(log[0])
    if df.verifyIdPassword(log[0], log[1]):  # 3 Authenticate
        if df.ifEligible(log[0]):
            print('Participant Logged in... ID:' + str(log[0]))
            connection.send("Authenticate".encode())
        else:
            print('Participant Already Took The Quiz by ID:' + str(log[0]))
            connection.send("QuizTaken".encode())
    else:
        print('Invalid Participant')
        connection.send("InvalidParticipant".encode())

    data = connection.recv(1024)  # 4 Get Quiz Answer (Pick quiz option)
    print("Quiz Taken from ID: " + str(log[0]) + "  Processing...")
    lock.acquire()
    # update Database
    if df.update_option_picked(data.decode(), log[0]):
        print("Quiz Taken Successfully by Participant ID = " + str(log[0]))
        connection.send("Successful".encode())
    else:
        print("Quiz Update Failed by Participant ID = " + str(log[0]))
        connection.send("Quiz Update Failed".encode())
        # 5

    lock.release()
    connection.close()


def quiz_Server():
    serversocket = socket.socket()
    host = socket.gethostname()
    port = 4001

    ThreadCount = 0

    try:
        serversocket.bind((host, port))
    except socket.error as e:
        print(str(e))
    print("Waiting for the connection")

    serversocket.listen(10)

    print("Listening on " + str(host) + ":" + str(port))

    while True:
        client, address = serversocket.accept()

        print('Connected to :', address)

        client.send("Connection Established".encode())  ### 1
        t = Thread(target=client_thread, args=(client,))
        t.start()
        ThreadCount += 1
        # break

    serversocket.close()


if __name__ == '__main__':
    quiz_Server()
