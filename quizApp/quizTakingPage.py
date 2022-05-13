import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk, Image


def pickAnswer(root, frame1, vote, client_socket):
    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode())  # 4

    message = client_socket.recv(1024)  # Success message
    print(message.decode())  # 5
    message = message.decode()
    if message == "Successful":
        Label(frame1, text="Quiz Taken Successfully", font=('Helvetica', 18, 'bold')).grid(row=1, column=1)
    else:
        Label(frame1, text="Failed Taking Quiz... \nTry again", font=('Helvetica', 18, 'bold')).grid(row=1, column=1)

    client_socket.close()


def quizTakingPg(root, frame1, client_socket):
    root.title("Which Country Drinks the Most Coffee Per-Capita?")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Which Country Drinks the Most Coffee Per-Capita?", font=('Helvetica', 14, 'bold')).grid(row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    vote = StringVar(frame1, "-1")

    Radiobutton(frame1, text="USA", variable=vote, value="usa", indicator=0, height=4, width=15,
                command=lambda: pickAnswer(root, frame1, "usa", client_socket)).grid(row=1, column=1)

    Radiobutton(frame1, text="Finland", variable=vote, value="finland", indicator=0, height=4, width=15,
                command=lambda: pickAnswer(root, frame1, "finland", client_socket)).grid(row=2, column=1)

    Radiobutton(frame1, text="UK", variable=vote, value="uk", indicator=0, height=4,
                width=15, command=lambda: pickAnswer(root, frame1, "uk", client_socket)).grid(row=3, column=1)

    Radiobutton(frame1, text="Poland", variable=vote, value="poland", indicator=0, height=4, width=15,
                command=lambda: pickAnswer(root, frame1, "poland", client_socket)).grid(row=4, column=1)

    Radiobutton(frame1, text="\nSweden    \n  ", variable=vote, value="sweden", indicator=0, height=4, width=15,
                command=lambda: pickAnswer(root, frame1, "sweden", client_socket)).grid(row=5, column=1)

    frame1.pack()
    root.mainloop()

# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         quizTakingPg(root,frame1,client_socket)
