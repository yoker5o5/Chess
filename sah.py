import sys
from tkinter import *
class Figura:

    def __init__(self, pos, type, boja):
        self.pos = pos
        self.type = type
        self.boja = boja
        global B
        B = [[0]*8]*8
        for i in range(8):
            B[i] = [0]*8
        self.createbutton()

    def createbutton(self):
        self.button = Button(window, text = self.type, fg=self.boja, height=5, width=12, command = self.moves, bg="blue") if (self.pos[0] % 2) == 0 and (self.pos[1] % 2) == 1 or (self.pos[0] % 2) == 1 and (self.pos[1] % 2) == 0 else Button(window, text = self.type, fg=self.boja, height=5, width=12, command = self.moves)
        self.button.grid(row=self.pos[0], column=self.pos[1])

    def tempbutton(self, i, j):
        figpos = []
        for fig in figure:
            figpos.append([fig.pos, fig.boja])
        if [[i, j], self.boja] not in figpos:
            B[i][j] = Button(window, text = self.type, fg=self.boja, height=5, width=12, command = lambda x=[i, j]: self.move(x), bg="red")
            B[i][j].grid(row=i, column=j)

    def moves(self):
        global B
        for i in range(8):
            for j in range(8):
                if type(B[i][j]) != int:
                    B[i][j].destroy()
        figpos = []
        for fig in figure:
            figpos.append(fig.pos)
        x = self.pos[0]
        y = self.pos[1]
        if self.type == "piun":
            j = self.pos[1]
            if self.boja == "black":
                i = self.pos[0]
                if i == 1:
                    self.tempbutton(i+2, j)
                i += 1
            else: 
                i = self.pos[0]
                if i == 6:
                    self.tempbutton(i-2, j)
                i -= 1
            self.tempbutton(i, j)
        elif self.type == "top" or self.type == "kraljica":
            for i in range(x, 8):
                if x != i:
                    self.tempbutton(i, y)
                    if [i, y] in figpos and i > x:
                        break
            for i in range(x, -1, -1):
                if x != i:
                    self.tempbutton(i, y)
                    if [i, y] in figpos and i < x:
                        break
            for j in range(y, 8):
                if j != y:
                    self.tempbutton(x, j)
                    if [x, j] in figpos and j > y:
                        break
            for j in range(y, -1, -1):
                if j != y:
                    self.tempbutton(x, j)
                    if [x, j] in figpos and j < y:
                        break
        if self.type == "lovac" or self.type == "kraljica":
            i = x
            j = y
            while i < 7 and j < 7:
                i += 1
                j += 1
                self.tempbutton(i, j)
                if [i,j] in figpos:
                    break
            i = x
            j = y
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                self.tempbutton(i, j)
                if [i,j] in figpos:
                    break
            i = x
            j = y
            while i < 7 and j > 0:
                i += 1
                j -= 1
                self.tempbutton(i, j)
                if [i,j] in figpos:
                    break
            i = x
            j = y
            while i > 0 and j < 7:
                i -= 1
                j += 1
                self.tempbutton(i, j)
                if [i,j] in figpos:
                    break
        elif self.type == "konj":
            xx = [x+2, x-2]
            yy = [y-1, y+1]
            xxx = [x+1, x-1]
            yyy = [y+2, y-2]
            for i in xx:
                for j in yy:
                    try:
                        self.tempbutton(i, j)
                    except:
                        pass
            for i in xxx:
                for j in yyy:
                    try:
                        self.tempbutton(i, j)
                    except:
                        pass
        elif self.type == "kralj":
            xx = [x+1, x-1, x]
            yy = [y+1, y-1, y]
            for i in xx:
                for j in yy:
                    if i != x or j != y:
                        try:
                            self.tempbutton(i, j)
                        except:
                            pass
    def move(self, x):
        self.button.destroy()
        self.pos = x
        self.createbutton()
        for i in range(8):
            for j in range(8):
                if type(B[i][j]) != int:
                    B[i][j].destroy()
        

def main(*args):
    global root, figure
    global window
    root = Tk()
    root.title("Sah")
    window = Frame(root,bg='lightblue')
    tabla()
    figure = []
    for i in [0, 7]:
        figure.append(Figura([0, i], "top", "black"))
        figure.append(Figura([7, i], "top", "white"))
    for i in [1,6]:
        figure.append(Figura([0, i], "konj", "black"))
        figure.append(Figura([7, i], "konj", "white"))
    for i in [2, 5]:
        figure.append(Figura([0, i], "lovac", "black"))
        figure.append(Figura([7, i], "lovac", "white"))
    for i in range(8):
        figure.append(Figura([1, i], "piun", "black"))
    for i in range(8):
        figure.append(Figura([6, i], "piun", "white"))
    figure.append(Figura([0, 4], "kralj", "black"))
    figure.append(Figura([0, 3], "kraljica", "black"))
    figure.append(Figura([7, 4], "kralj", "white"))
    figure.append(Figura([7, 3], "kraljica", "white"))

    root.mainloop()

def tabla():
    root.geometry("751x688")
    window.place(relx=0,rely=0,relheight=1,relwidth=1)

    B = [[0]*8]*8

    for i, col in enumerate(B):
        for j, _ in enumerate(col):
            if (i % 2) == 0 and (j % 2) == 1 or (i % 2) == 1 and (j % 2) == 0:
                B[i][j] = Label(window, text = " ", height=5, width=12, bg="blue")
            else:
                B[i][j] = Label(window, text = " ", height=5, width=12)
            B[i][j].grid(row= i, column=j)

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)