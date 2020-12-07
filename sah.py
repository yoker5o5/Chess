import sys
from tkinter import *

class Figura:
    def __init__(self, pos, type, boja):
        self.pos = pos
        self.type = type
        self.boja = boja

    # def moves(self):
    #     for i in range(8):
    #         for j in range(8):

    def move(self):
        if self.boja == "black":
            self.pos[0] += 1
        else:
            self.pos[0] -=1
        page1()


def main(*args):
    global root, figure
    global window
    figure = []
    figure.append(Figura([0, 0], "top", "black"))
    for i in range(8):
        figure.append(Figura([1, i], "piun", "black"))
    for i in range(8):
        figure.append(Figura([6, i], "piun", "white"))
    figure.append(Figura([0, 3], "k", "black"))
    root = Tk()

    root.title("Sah")
    window = Frame(root,bg='lightblue')
    page1()
    root.mainloop()

def page1():
    root.geometry("751x688")
    window.place(relx=0,rely=0,relheight=1,relwidth=1)

    B = [[0]*8]*8

    figpos = []
    for fig in figure:
        for i, col in enumerate(B):
            #B[i] = [0]*8
            for j, _ in enumerate(col):
                if (i % 2) == 0 and (j % 2) == 1 or (i % 2) == 1 and (j % 2) == 0:
                    B[i][j] = Button(window, text = fig.type, fg=fig.boja, height=5, width=12, command = fig.move, bg="red") if [i, j] == fig.pos else Button(window, text = " ", height=5, width=12, bg="red")
                else:
                    B[i][j] = Button(window, text = fig.type, fg=fig.boja, height=5, width=12, command = fig.move) if [i, j] == fig.pos else Button(window, text = " ", height=5, width=12)
                if [i, j] not in figpos:
                    B[i][j].grid(row=i, column=j)
        figpos.append(fig.pos)

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)