import sys
from tkinter import *

def main(*args):
    global root
    root = Tk()
    root.title("Sah")
    page1()
    root.mainloop()

def page1():

    root.geometry("1000x1000")
    window = Frame(root,bg='lightblue')
    window.place(relx=0,rely=0,relheight=1,relwidth=1)

    B = [[0]*8]*8

    for i, col in enumerate(B):
        for j, _ in enumerate(col):
            B[i][j] = Button(window, text =" ", height=5, width=12)
            B[i][j].grid(row=i, column=j)

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)