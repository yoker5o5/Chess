import sys
from tkinter import *
import random
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


    def possiblemoves(self):
        self.posmoves = []
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
                    self.posmoves.append([i+2, j])
                i += 1
                if [i, j+1] in figpos:
                    self.posmoves.append([i, j+1])
                if [i, j-1] in figpos:
                    self.posmoves.append([i, j-1])
            else: 
                i = self.pos[0]
                if i == 6:
                    self.posmoves.append([i-2, j])
                i -= 1
                if [i, j+1] in figpos:
                    self.posmoves.append([i, j+1])
                if [i, j-1] in figpos:
                    self.posmoves.append([i, j-1])
            if [i, j] not in figpos:
                self.posmoves.append([i, j])
        elif self.type == "top" or self.type == "kraljica":
            for i in range(x, 8):
                if x != i:
                    self.posmoves.append([i, y])
                    if [i, y] in figpos and i > x:
                        break
            for i in range(x, -1, -1):
                if x != i:
                    self.posmoves.append([i, y])
                    if [i, y] in figpos and i < x:
                        break
            for j in range(y, 8):
                if j != y:
                    self.posmoves.append([x, j])
                    if [x, j] in figpos and j > y:
                        break
            for j in range(y, -1, -1):
                if j != y:
                    self.posmoves.append([x, j])
                    if [x, j] in figpos and j < y:
                        break
        if self.type == "lovac" or self.type == "kraljica":
            i = x
            j = y
            while i < 7 and j < 7:
                i += 1
                j += 1
                self.posmoves.append([i, j])
                if [i,j] in figpos:
                    break
            i = x
            j = y
            while i > 0 and j > 0:
                i -= 1
                j -= 1
                self.posmoves.append([i, j])
                if [i,j] in figpos:
                    break
            i = x
            j = y
            while i < 7 and j > 0:
                i += 1
                j -= 1
                self.posmoves.append([i, j])
                if [i,j] in figpos:
                    break
            i = x
            j = y
            while i > 0 and j < 7:
                i -= 1
                j += 1
                self.posmoves.append([i, j])
                if [i,j] in figpos:
                    break
        elif self.type == "konj":
            xx = [x+2, x-2]
            yy = [y-1, y+1]
            xxx = [x+1, x-1]
            yyy = [y+2, y-2]
            for i in xx:
                for j in yy:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        self.posmoves.append([i, j])
            for i in xxx:
                for j in yyy:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        self.posmoves.append([i, j])
        elif self.type == "kralj":
            xx = [x+1, x-1, x]
            yy = [y+1, y-1, y]
            for i in xx:
                for j in yy:
                    if i != x or j != y:
                        if i > -1 and j > -1 and i < 8 and j < 8:
                            if self.boja == "black" and [i, j] not in whiteposmoves:
                                self.posmoves.append([i, j])
                            if self.boja == "white" and [i, j] not in blackposmoves:
                                self.posmoves.append([i, j])
        figpos2 = []
        temp = []
        for fig in figure:
            figpos2.append((fig.pos, fig.boja))
        for x2 in self.posmoves:
            if (x2, self.boja) not in figpos2:
                temp.append(x2)
        return temp

    def createbutton(self):
        self.button = Button(window, text = self.type, fg="white", height=4, width=10, command = self.moves, bg=self.boja) if self.boja == "black" else Button(window, text = self.type, fg="black", height=4, width=10, command = self.moves, bg=self.boja)
        self.button.grid(row=self.pos[0], column=self.pos[1])
    # def createbutton(self):
    #     self.button = Button(window, text = self.type, fg=self.boja, height=5, width=12, command = self.moves, bg="blue") if (self.pos[0] % 2) == 0 and (self.pos[1] % 2) == 1 or (self.pos[0] % 2) == 1 and (self.pos[1] % 2) == 0 else Button(window, text = self.type, fg=self.boja, height=5, width=12, command = self.moves)
    #     self.button.grid(row=self.pos[0], column=self.pos[1])

    def tempbutton(self, i, j):
        # figpos = []
        # for fig in figure:
        #     figpos.append([fig.pos, fig.boja])
        # if [[i, j], self.boja] not in figpos:
        B[i][j] = Button(window, text = self.type, fg=self.boja, height=5, width=12, command = lambda x=[i, j]: self.move(x), bg="red")
        B[i][j].grid(row=i, column=j)

    def moves(self):
        global B
        for i in range(8):
            for j in range(8):
                if type(B[i][j]) != int:
                    B[i][j].destroy()
        for move in self.possiblemoves():
            self.tempbutton(move[0], move[1])

    def move(self, x):
        self.button.destroy()
        for fig in figure:
            if x == fig.pos:
                fig.button.destroy()
                figure.remove(fig)
        if self.type == "piun" and self.boja == "white" and x[0] == 0:
            self.type = "kraljica"
        if self.type == "piun" and self.boja == "black" and x[0] == 7:
            self.type = "kraljica"
        self.pos = x
        self.createbutton()
        for i in range(8):
            for j in range(8):
                if type(B[i][j]) != int:
                    B[i][j].destroy()
        randommove("black")
        checkpos()

        
def checkpos():
    global whiteposmoves, blackposmoves
    whiteposmoves = []
    blackposmoves = []
    for fig in figure:
        if fig.boja == "white":
            whiteposmoves.extend(fig.possiblemoves())
        elif fig.boja == "black":
            blackposmoves.extend(fig.possiblemoves())

def randommove(boja):
        randomfigura = random.choice(figure)
        while randomfigura.boja != boja or len(randomfigura.possiblemoves()) == 0:
            randomfigura = random.choice(figure)
        # bestmove = 0
        # best = [0, 0]
        # print(randomfigura.possiblemoves())
        # for i, move in enumerate(randomfigura.possiblemoves()):
        #     print(move)
        #     if (move[0] + move[1]) > bestmove:
        #         bestmove = move[0] + move[1]
        #         best = move
        randommove = random.choice(randomfigura.possiblemoves())
        #randommove = best
        #print(randommove)
        randomfigura.button.destroy()
        for fig in figure:
            if randommove == fig.pos:
                fig.button.destroy()
                figure.remove(fig)
        if randomfigura.type == "piun" and randomfigura.boja == "white" and randommove[0] == 0:
            randomfigura.type = "kraljica"
        if randomfigura.type == "piun" and randomfigura.boja == "black" and randommove[0] == 7:
            randomfigura.type = "kraljica"
        randomfigura.pos = randommove
        randomfigura.createbutton()

def ucitajfigure():
    global figure
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
    checkpos()
    root.mainloop()

def tabla():
    global root
    global window
    root = Tk()
    root.title("Sah")
    window = Frame(root,bg='lightblue')
    root.geometry("830x767")
    window.place(relx=0,rely=0,relheight=1,relwidth=1)

    B = [[0]*8]*8

    for i, col in enumerate(B):
        for j, _ in enumerate(col):
            if (i % 2) == 0 and (j % 2) == 1 or (i % 2) == 1 and (j % 2) == 0:
                B[i][j] = Label(window, text = " ", height=6, width=14, bg="black")
            else:
                B[i][j] = Label(window, text = " ", height=6, width=14)
            B[i][j].grid(row= i, column=j)


def main(*args):
    tabla()
    ucitajfigure()

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)