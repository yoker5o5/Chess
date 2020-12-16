import sys
from tkinter import *

class Tabla:
    def __init__(self):
        self.root = Tk()
        self.root.title("Sah")
        self.window = Frame(self.root,bg='lightblue')
        self.root.geometry("830x767")
        self.window.place(relx=0,rely=0,relheight=1,relwidth=1)

        B = [[0]*8]*8

        for i, col in enumerate(B):
            for j, _ in enumerate(col):
                if (i % 2) == 0 and (j % 2) == 1 or (i % 2) == 1 and (j % 2) == 0:
                    B[i][j] = Label(self.window, text = " ", height=6, width=14, bg="black")
                else:
                    B[i][j] = Label(self.window, text = " ", height=6, width=14)
                B[i][j].grid(row= i, column=j)

    def prikaz(self):
        self.root.mainloop()


class Figura:
    figpos = []

    B = [[0]*8]*8
    for i in range(8):
        B[i] = [0]*8

    def __init__(self, pos, boja, tabla):
        self.pos = pos
        self.boja = boja
        self.window = tabla
        self.enemycolor = "white" if self.boja == "black" else "black"
        Figura.figpos.append((pos, boja))
        self.posmoves = []


    def checkfigpos(self):
        pass

    def createbutton(self):
        self.button = Button(self.window, text = self.type, fg=self.enemycolor, height=4, width=10, command = self.possiblemoves, bg=self.boja)
        self.button.grid(row=self.pos[0], column=self.pos[1])

    def moves(self):
        for i in range(8):
            for j in range(8):
                if type(Figura.B[i][j]) != int:
                    Figura.B[i][j].destroy()
        for i, j in self.posmoves:
            Figura.B[i][j] = Button(self.window, text = self.type, fg=self.boja, height=3, width=8, command = lambda x=[i, j]: self.move(x), bg="red")
            Figura.B[i][j].grid(row=i, column=j)

    def move(self, x):
        # for fig in figure:
        #     if x == fig.pos:
        #         fig.button.destroy()
        #         figure.remove(fig)
        # if self.type == "piun" and self.boja == "white" and x[0] == 0:
        #     self.type = "kraljica"
        # if self.type == "piun" and self.boja == "black" and x[0] == 7:
        #     self.type = "kraljica"
        self.figpos.remove((self.pos, self.boja))
        self.pos = x
        self.figpos.append((self.pos, self.boja))
        self.button.grid(row=self.pos[0], column=self.pos[1])
        self.posmoves = []
        for i in range(8):
            for j in range(8):
                if type(Figura.B[i][j]) != int:
                    Figura.B[i][j].destroy()

class Piun(Figura):
    def __init__(self, pos, boja, tabla):
        super().__init__(pos, boja, tabla)
        self.type = "piun"
        self.createbutton()

    def possiblemoves(self):
        i = self.pos[0]
        j = self.pos[1]
        if self.boja == "black":
            if i == 1:
                self.posmoves.append([i+2, j])
            i += 1
            # if [i, j+1] in figpos:
            #     self.posmoves.append([i, j+1])
            # if [i, j-1] in figpos:
            #     self.posmoves.append([i, j-1])
        else: 
            if i == 6:
                self.posmoves.append([i-2, j])
            i -= 1
            # if [i, j+1] in figpos:
            #     self.posmoves.append([i, j+1])
            # if [i, j-1] in figpos:
            #     self.posmoves.append([i, j-1])
        self.posmoves.append([i, j])
        self.moves()

class Top(Figura):

    def __init__(self, pos, boja, tabla):
        super().__init__(pos, boja, tabla)
        self.type = "top"
        self.createbutton()

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        for i in range(x, 8):
            if x != i:
                if ([i, y], self.boja) in Figura.figpos and i > x:
                    break
                self.posmoves.append([i, y])
                if ([i, y], self.enemycolor) in Figura.figpos and i > x:
                    break
        for i in range(x, -1, -1):
            if x != i:
                if ([i, y], self.boja) in Figura.figpos and i < x:
                    break
                self.posmoves.append([i, y])
                if ([i, y], self.enemycolor) in Figura.figpos and i < x:
                    break
        for j in range(y, 8):
            if j != y:
                if ([x, j], self.boja) in Figura.figpos and j > y:
                    break
                self.posmoves.append([x, j])
                if ([x, j], self.enemycolor) in Figura.figpos and j > y:
                    break
        for j in range(y, -1, -1):
            if j != y:
                if ([x, j], self.boja) in Figura.figpos and j < y:
                    break
                self.posmoves.append([x, j])
                if ([x, j], self.enemycolor) in Figura.figpos and j < y:
                    break
        self.moves()
    
class Lovac(Figura):

    def __init__(self, pos, boja, tabla):
        super().__init__(pos, boja, tabla)
        self.type = "lovac"
        self.createbutton()

    def possiblemoves(self):
        i = self.pos[0]
        j = self.pos[1]
        while i < 7 and j < 7:
            i += 1
            j += 1
            if ([i,j], self.boja) in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if ([i,j], self.boja) in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i < 7 and j > 0:
            i += 1
            j -= 1
            if ([i,j], self.boja) in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i > 0 and j < 7:
            i -= 1
            j += 1
            if ([i,j], self.boja) in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        self.moves()
class Kraljica(Figura):

    def __init__(self, pos, boja, tabla):
        super().__init__(pos, boja, tabla)
        self.type = "kraljica"
        self.createbutton()

    def possiblemoves(self):
        Lovac.possiblemoves(self)
        Top.possiblemoves(self)


def main(*args):
    t = Tabla()
    figure = []
    for i in [0, 7]:
        figure.append(Top([0, i], "black", t.window))
        figure.append(Top([7, i], "white", t.window))
    # for i in [1,6]:
    #     figure.append(Figura([0, i], "konj", "black"))
    #     figure.append(Figura([7, i], "konj", "white"))
    for i in [2, 5]:
        figure.append(Lovac([0, i], "black", t.window))
        figure.append(Lovac([7, i], "white", t.window))
    for i in range(8):
        figure.append(Piun([1, i],"black", t.window))
    for i in range(8):
        figure.append(Piun([6, i],"white", t.window))
    figure.append(Kraljica([7, 3], "white", t.window))
    t.prikaz()

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)