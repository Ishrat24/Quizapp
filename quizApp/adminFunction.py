import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk, Image


def allReset(root, frame1):
    Label(frame1, text="").grid(row=10, column=0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row=11, column=0, columnspan=5)


# controls the showing result parts
def showResult(root, frame1):
    result = df.show_result()
    root.title("Answers")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Quiz Result", font=('Helvetica', 18, 'bold')).grid(row=0, column=1, rowspan=1)
    Label(frame1, text="").grid(row=1, column=0)

    pick = StringVar(frame1, "-1")  # pick your option

    Label(frame1, text="USA              :       ", font=('Helvetica', 12, 'bold')).grid(row=2, column=1)
    Label(frame1, text=result['usa'], font=('Helvetica', 12, 'bold')).grid(row=2, column=2)

    Label(frame1, text="Finland             :          ", font=('Helvetica', 12, 'bold')).grid(row=3, column=1)
    Label(frame1, text=result['finland'], font=('Helvetica', 12, 'bold')).grid(row=3, column=2)

    Label(frame1, text="UK               :          ", font=('Helvetica', 12, 'bold')).grid(row=4, column=1)
    Label(frame1, text=result['uk'], font=('Helvetica', 12, 'bold')).grid(row=4, column=2)

    Label(frame1, text="Poland    :          ", font=('Helvetica', 12, 'bold')).grid(row=5, column=1)
    Label(frame1, text=result['poland'], font=('Helvetica', 12, 'bold')).grid(row=5, column=2)

    Label(frame1, text="Sweden            :          ", font=('Helvetica', 12, 'bold')).grid(row=6, column=1)
    Label(frame1, text=result['sweden'], font=('Helvetica', 12, 'bold')).grid(row=6, column=2)

    Label(frame1, text="").grid(row=7, column=0)
    Label(frame1, text="The correct answer is: Finland", font=('Helvetica', 18, 'bold')).grid(row=8, column=1, rowspan=1)

    frame1.pack()
    root.mainloop()

# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showResult(root,frame1)
