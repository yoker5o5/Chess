import sys
from tkinter import *

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.enemycolor = "white" if color == "black" else "black"
        self.chess = False
        self.napotezu = 1 if color == "white" else 0
        
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
    figure = []
    kraljcheck = 0
    B = [[0]*8]*8
    for i in range(8):
        B[i] = [0]*8

    def __init__(self, pos, boja, tabla):
        self.pos = pos
        self.boja = boja
        self.window = tabla
        self.enemycolor = "white" if self.boja == "black" else "black"
        Figura.figpos.append((pos, boja))
        self.createbutton()
        Figura.figure.append(self)

    def createbutton(self):
        self.button = Button(self.window, text = self.type, fg=self.enemycolor, height=4, width=10, command = self.moves, bg=self.boja)
        self.button.grid(row=self.pos[0], column=self.pos[1])

    def moves(self):
        for pl in players:
            if pl.napotezu == 1 and pl.color == self.boja:
                self.posmoves = []
                for i in range(8):
                    for j in range(8):
                        if type(Figura.B[i][j]) != int:
                            Figura.B[i][j].destroy()
                self.possiblemoves()
                # if pl.chess:
                #     for fig in figure:
                #         if fig.posmoves()
                for i, j in self.posmoves:
                    Figura.B[i][j] = Button(self.window, text = self.type, fg=self.boja, height=3, width=8, command = lambda x=[i, j]: self.move(x), bg="red")
                    Figura.B[i][j].grid(row=i, column=j)

    def remove(self): 
        self.button.destroy()
        Figura.figure.remove(self)
        Figura.figpos.remove((self.pos, self.boja))

    def move(self, x):
        # for fig in figure:
        #     if x == fig.pos:
        #         fig.button.destroy()
        #         figure.remove(fig)
        Figura.figpos.remove((self.pos, self.boja))
        self.pos = x
        Figura.figpos.append((self.pos, self.boja))
        self.button.grid(row=self.pos[0], column=self.pos[1])
        for i in range(8):
            for j in range(8):
                if type(Figura.B[i][j]) != int:
                    Figura.B[i][j].destroy()
        if self.type == "piun" and self.boja == "white" and x[0] == 0 or self.type == "piun" and self.boja == "black" and x[0] == 7:
            Kraljica(self.pos, self.boja, self.window)
            self.remove()
        if Figura.kraljcheck == 0:
            for fig in Figura.figure:
                if fig.pos == x and fig != self:
                    fig.remove()
            for pl in players:
                if pl.napotezu == 0:
                    if self.checkchess():
                        pl.chess = True
                else:
                    pl.chess = False

                pl.napotezu = 0 if pl.napotezu == 1 else 1
    
    def checkchess(self):
        for fig in Figura.figure:
            if fig.type == "kralj":
                self.posmoves = []
                self.possiblemoves()
                if fig.pos in self.posmoves:
                    return True
        return False

    def svefigure():
        return [fig for fig in Figura.figure]

        
        

class Piun(Figura):
    def __init__(self, pos, boja, tabla):
        self.type = "piun"
        super().__init__(pos, boja, tabla)

    def possiblemoves(self):
        i = self.pos[0]
        j = self.pos[1]
        if self.boja == "black":
            if Figura.kraljcheck == 0:
                if i == 1:
                    self.posmoves.append([i+2, j])
                    for fig in Figura.figure:
                        if fig.pos == [i+2, j] or fig.pos == [i+1, j]:
                            self.posmoves.remove([i+2, j])
            i += 1
            if ([i, j+1], self.enemycolor)  in Figura.figpos:
                self.posmoves.append([i, j+1])
            if ([i, j-1], self.enemycolor) in Figura.figpos:
                self.posmoves.append([i, j-1])
        else: 
            if Figura.kraljcheck == 0:
                if i == 6:
                    self.posmoves.append([i-2, j])
                    for fig in Figura.figure:
                        if fig.pos == [i-2, j] or fig.pos == [i-1, j]:
                            self.posmoves.remove([i-2, j])
            i -= 1
            if ([i, j+1], self.enemycolor)  in Figura.figpos:
                self.posmoves.append([i, j+1])
            if ([i, j-1], self.enemycolor) in Figura.figpos:
                self.posmoves.append([i, j-1])
        if i >= 0 and i < 8 and ([i,j], self.boja) not in Figura.figpos and ([i,j], self.enemycolor) not in Figura.figpos: #and Figura.kraljcheck == 0
            self.posmoves.append([i, j])
class Top(Figura):

    def __init__(self, pos, boja, tabla):
        self.type = "top"
        super().__init__(pos, boja, tabla)

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        for i in range(x, 8):
            if x != i:
                if ([i, y], self.boja) in Figura.figpos and i > x and ([i, y], self.enemycolor) not in Figura.figpos:
                    break
                self.posmoves.append([i, y])
                if ([i, y], self.enemycolor) in Figura.figpos and i > x:
                    break
        for i in range(x, -1, -1):
            if x != i:
                if ([i, y], self.boja) in Figura.figpos and i < x and ([i, y], self.enemycolor) not in Figura.figpos:
                    break
                self.posmoves.append([i, y])
                if ([i, y], self.enemycolor) in Figura.figpos and i < x:
                    break
        for j in range(y, 8):
            if j != y:
                if ([x, j], self.boja) in Figura.figpos and j > y and ([x, j], self.enemycolor) not in Figura.figpos:
                    break
                self.posmoves.append([x, j])
                if ([x, j], self.enemycolor) in Figura.figpos and j > y:
                    break
        for j in range(y, -1, -1):
            if j != y:
                if ([x, j], self.boja) in Figura.figpos and j < y and ([x, j], self.enemycolor) not in Figura.figpos:
                    break
                self.posmoves.append([x, j])
                if ([x, j], self.enemycolor) in Figura.figpos and j < y:
                    break
    
class Lovac(Figura):

    def __init__(self, pos, boja, tabla):
        self.type = "lovac"
        super().__init__(pos, boja, tabla)

    def possiblemoves(self):
        i = self.pos[0]
        j = self.pos[1]
        while i < 7 and j < 7:
            i += 1
            j += 1
            if ([i,j], self.boja) in Figura.figpos and ([i,j], self.enemycolor) not in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if ([i,j], self.boja) in Figura.figpos and ([i,j], self.enemycolor) not in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i < 7 and j > 0:
            i += 1
            j -= 1
            if ([i,j], self.boja) in Figura.figpos and ([i,j], self.enemycolor) not in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i > 0 and j < 7:
            i -= 1
            j += 1
            if ([i,j], self.boja) in Figura.figpos and ([i,j], self.enemycolor) not in Figura.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in Figura.figpos:
                break
class Kraljica(Figura):

    def __init__(self, pos, boja, tabla):
        self.type = "kraljica"
        super().__init__(pos, boja, tabla)

    def possiblemoves(self):
        Lovac.possiblemoves(self)
        Top.possiblemoves(self)
class Konj(Figura):

    def __init__(self, pos, boja, tabla):
        self.type = "konj"
        super().__init__(pos, boja, tabla)

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        xx = [[x+2, x-2], [x+1, x-1]]
        yy = [[y-1, y+1], [y+2, y-2]]
        for g, _ in enumerate(xx):
            for i in xx[g]:
                for j in yy[g]:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        if ([i, j], self.boja) not in Figura.figpos or ([i,j], self.enemycolor) in Figura.figpos:
                            self.posmoves.append([i, j])
class Kralj(Figura):
    def __init__(self, pos, boja, tabla):
        self.type = "kralj"
        super().__init__(pos, boja, tabla)

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        xx = [x+1, x-1, x]
        yy = [y+1, y-1, y]
        for i in xx:
            for j in yy:
                if i != x or j != y:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        if ([i,j], self.boja) not in Figura.figpos:
                            temp = self.pos
                            Figura.kraljcheck = 1
                            self.move([i, j])
                            self.posmoves.append([i, j])
                            for fig in Figura.figure:
                                if fig.type != "kralj" or fig.boja != self.boja:
                                    fig.posmoves = []
                                    if fig.type == "kralj":
                                        fig.checkmoves()
                                    else:
                                        fig.possiblemoves()
                                    if fig.boja != self.boja and [i, j] in fig.posmoves and [i, j] in self.posmoves:
                                        self.posmoves.remove([i, j])
                            self.move(temp)
                            Figura.kraljcheck = 0
    def checkmoves(self):
        x = self.pos[0]
        y = self.pos[1]
        xx = [x+1, x-1, x]
        yy = [y+1, y-1, y]
        for i in xx:
            for j in yy:
                if i != x or j != y:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        if ([i,j], self.boja) not in Figura.figpos:
                            self.posmoves.append([i, j])

def main(*args):
    global figure, players
    t = Tabla()
    players = []
    players.append(Player("Djordje", "white"))
    players.append(Player("Boris", "black"))
    for i in [0, 7]:
        Top([0, i], "black", t.window)
        Top([7, i], "white", t.window)
    for i in [1,6]:
        Konj([0, i], "black", t.window)
        Konj([7, i], "white", t.window)
    for i in [2, 5]:
        Lovac([0, i], "black", t.window)
        Lovac([7, i], "white", t.window)
    for i in range(8):
        Piun([1, i],"black", t.window)
    for i in range(8):
        Piun([6, i],"white", t.window)
    Kralj([0, 4], "black", t.window)
    Kraljica([0, 3], "black", t.window)
    Kralj([7, 4], "white", t.window)
    Kraljica([7, 3], "white", t.window)
    t.prikaz()
if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)