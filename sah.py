import sys
from tkinter import *

class Figura:
    def __init__(self, pos, type, boja):
        self.pos = pos
        self.type = type
        self.boja = boja
    def move(self):
        self.pos[0] += 1
        page1()


def main(*args):
    global root, figure
    figure = []
    figure.append(Figura([0, 0], "top", "crna"))
    figure.append(Figura([1, 0], "p", "crna"))
    figure.append(Figura([1, 1], "p", "crna"))
    figure.append(Figura([1, 2], "p", "crna"))
    figure.append(Figura([0, 3], "k", "crna"))
    print (figure)
    root = Tk()

    root.title("Sah")
    page1()
    root.mainloop()

def page1():
    root.geometry("1000x1000")
    window = Frame(root,bg='lightblue')
    window.place(relx=0,rely=0,relheight=1,relwidth=1)

    B = [[0]*8]*8

    figpos = []
    for fig in figure:
        for i, col in enumerate(B):
            B[i] = [0]*8
            for j, _ in enumerate(col):
                B[i][j] = Button(window, text = fig.type + " - " + fig.boja, height=5, width=12, command = fig.move) if [i, j] == fig.pos else Button(window, text = " ", height=5, width=12)
                if [i, j] not in figpos:
                    B[i][j].grid(row=i, column=j)
        figpos.append(fig.pos)

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)