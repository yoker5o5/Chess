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
    def __init__(self, pro, pos, players, boja):
        self.players = players
        self.glavni = Frame(pro,bg=boja)
        self.glavni.grid(row = pos[0], column = pos[1])
        self.window = [0]*3
        for i,_ in enumerate(self.window):
            self.window[i] = Frame(self.glavni)
            self.window[i].grid(row = 1, column = i)
        self.win = [0]*3
        for i in [0, 2]:
            self.win[i] = Frame(self.glavni)
            self.win[i].grid(row = i, column = 1)
        self.figpos = []
        self.ucitajfigure()
    
    def ucitajfigure(self):
        self.polja = []
        self.figure = []
        for i in range(8):
            for j in range(8):
                if (i % 2) == 0 and (j % 2) == 1 or (i % 2) == 1 and (j % 2) == 0:
                    self.label = Label(self.window[1], text = " ", height=6, width=14, bg="black")
                else:
                    self.label = Label(self.window[1], text = " ", height=6, width=14)
                self.label.grid(row= i, column=j)
        for j in [0, 2]:
            for i in range(8, 0, -1):
                self.label = Label(self.window[j], text = str(i),height=6, width=6)
                self.label.grid(row=abs(i-8),column=0)
        for j in [0, 2]:
            for i,slovo in enumerate(["A", "B", "C", "D", "E", "F", "G", "H"]):
                self.label = Label(self.win[j], text = slovo,height=2, width=14)
                self.label.grid(row=j,column=i)
        for i in [0, 7]:
            self.figure.append(Top(self, [0, i], "black"))
            self.figure.append(Top(self, [7, i], "white"))
        for i in [1,6]:
            self.figure.append(Konj(self, [0, i], "black"))
            self.figure.append(Konj(self, [7, i], "white"))
        for i in [2, 5]:
            self.figure.append(Lovac(self, [0, i], "black"))
            self.figure.append(Lovac(self, [7, i], "white"))
        for i in range(8):
            self.figure.append(Piun(self, [1, i],"black"))
        for i in range(8):
            self.figure.append(Piun(self, [6, i],"white"))
        self.figure.append(Kralj(self, [0, 4], "black"))
        self.figure.append(Kraljica(self, [0, 3], "black"))
        self.figure.append(Kralj(self, [7, 4], "white"))
        self.figure.append(Kraljica(self, [7, 3], "white"))


class Figura:
    kraljcheck = 0

    def __init__(self, tabla, pos, boja):
        self.pos = pos
        self.boja = boja
        self.tabla = tabla
        self.enemycolor = "white" if self.boja == "black" else "black"
        self.tabla.figpos.append((pos, boja))
        self.temp = []
        self.createbutton()

    def createbutton(self):
        self.button = Button(self.tabla.window[1], text = self.type, fg=self.enemycolor, height=4, width=10, command = self.moves, bg=self.boja)
        self.button.grid(row=self.pos[0], column=self.pos[1])

    def moves(self):
        for pl in self.tabla.players:
            if pl.napotezu == 1 and pl.color == self.boja:
                self.posmoves = []
                for fig in self.tabla.figure:
                    for t in fig.temp:
                        t.destroy()
                #         fig.temp.remove(temps)
                self.possiblemoves()
                # if pl.chess:
                #     for fig in figure:
                #         if fig.posmoves()
                for i, j in self.posmoves:
                    self.temp.append(tempbutton(self, (i, j)))

    def remove(self):
        self.button.destroy()
        self.tabla.figure.remove(self)
        self.tabla.figpos.remove((self.pos, self.boja))

    def move(self, x):
        # for fig in figure:
        #     if x == fig.pos:
        #         fig.button.destroy()
        #         figure.remove(fig)
        self.tabla.figpos.remove((self.pos, self.boja))
        self.pos = x
        self.tabla.figpos.append((self.pos, self.boja))
        self.button.grid(row=self.pos[0], column=self.pos[1])
        for t in self.temp:
            t.destroy()
            #self.temp.remove(t)
        if self.type == "piun" and self.boja == "white" and x[0] == 0 or self.type == "piun" and self.boja == "black" and x[0] == 7:
            Kraljica(self.pos, self.boja, self.window)
            self.remove()
        if Figura.kraljcheck == 0:
            for fig in self.tabla.figure:
                if fig.pos == x and fig != self:
                    fig.remove()
            for pl in self.tabla.players:
                if pl.napotezu == 0:
                    if self.checkchess():
                        pl.chess = True
                else:
                    pl.chess = False

                pl.napotezu = 0 if pl.napotezu == 1 else 1
    
    def checkchess(self):
        for fig in self.tabla.figure:
            if fig.type == "kralj":
                self.posmoves = []
                self.possiblemoves()
                if fig.pos in self.posmoves:
                    return True
        return False

    def svefigure():
        return [fig for fig in self.tabla.figure]

class tempbutton():
    def __init__(self, fig, pos):
        self.pos = pos
        self.butt = Button(fig.tabla.window[1], text = fig.type, fg=fig.boja, height=3, width=8, command = lambda x=[pos[0], pos[1]]: fig.move(x), bg="red")
        self.butt.grid(row=pos[0], column=pos[1])
    def destroy(self):
        self.butt.destroy()
        

class Piun(Figura):
    def __init__(self, tabla, pos, boja):
        self.type = "piun"
        super().__init__(tabla, pos, boja)

    def possiblemoves(self):
        i = self.pos[0]
        j = self.pos[1]
        if self.boja == "black":
            if Figura.kraljcheck == 0:
                if i == 1:
                    self.posmoves.append([i+2, j])
                    for fig in self.tabla.figure:
                        if fig.pos == [i+2, j] or fig.pos == [i+1, j]:
                            self.posmoves.remove([i+2, j])
            i += 1
            if ([i, j+1], self.enemycolor)  in self.tabla.figpos:
                self.posmoves.append([i, j+1])
            if ([i, j-1], self.enemycolor) in self.tabla.figpos:
                self.posmoves.append([i, j-1])
        else: 
            if Figura.kraljcheck == 0:
                if i == 6:
                    self.posmoves.append([i-2, j])
                    for fig in self.tabla.figure:
                        if fig.pos == [i-2, j] or fig.pos == [i-1, j]:
                            self.posmoves.remove([i-2, j])
            i -= 1
            if ([i, j+1], self.enemycolor)  in self.tabla.figpos:
                self.posmoves.append([i, j+1])
            if ([i, j-1], self.enemycolor) in self.tabla.figpos:
                self.posmoves.append([i, j-1])
        if i >= 0 and i < 8 and ([i,j], self.boja) not in self.tabla.figpos and ([i,j], self.enemycolor) not in self.tabla.figpos: #and Figura.kraljcheck == 0
            self.posmoves.append([i, j])
class Top(Figura):

    def __init__(self, tabla, pos, boja):
        self.type = "top"
        super().__init__(tabla, pos, boja)

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        for i in range(x, 8):
            if x != i:
                if ([i, y], self.boja) in self.tabla.figpos and i > x and ([i, y], self.enemycolor) not in self.tabla.figpos:
                    break
                self.posmoves.append([i, y])
                if ([i, y], self.enemycolor) in self.tabla.figpos and i > x:
                    break
        for i in range(x, -1, -1):
            if x != i:
                if ([i, y], self.boja) in self.tabla.figpos and i < x and ([i, y], self.enemycolor) not in self.tabla.figpos:
                    break
                self.posmoves.append([i, y])
                if ([i, y], self.enemycolor) in self.tabla.figpos and i < x:
                    break
        for j in range(y, 8):
            if j != y:
                if ([x, j], self.boja) in self.tabla.figpos and j > y and ([x, j], self.enemycolor) not in self.tabla.figpos:
                    break
                self.posmoves.append([x, j])
                if ([x, j], self.enemycolor) in self.tabla.figpos and j > y:
                    break
        for j in range(y, -1, -1):
            if j != y:
                if ([x, j], self.boja) in self.tabla.figpos and j < y and ([x, j], self.enemycolor) not in self.tabla.figpos:
                    break
                self.posmoves.append([x, j])
                if ([x, j], self.enemycolor) in self.tabla.figpos and j < y:
                    break
    
class Lovac(Figura):

    def __init__(self, tabla, pos, boja):
        self.type = "lovac"
        super().__init__(tabla, pos, boja)

    def possiblemoves(self):
        i = self.pos[0]
        j = self.pos[1]
        while i < 7 and j < 7:
            i += 1
            j += 1
            if ([i,j], self.boja) in self.tabla.figpos and ([i,j], self.enemycolor) not in self.tabla.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in self.tabla.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if ([i,j], self.boja) in self.tabla.figpos and ([i,j], self.enemycolor) not in self.tabla.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in self.tabla.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i < 7 and j > 0:
            i += 1
            j -= 1
            if ([i,j], self.boja) in self.tabla.figpos and ([i,j], self.enemycolor) not in self.tabla.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in self.tabla.figpos:
                break
        i = self.pos[0]
        j = self.pos[1]
        while i > 0 and j < 7:
            i -= 1
            j += 1
            if ([i,j], self.boja) in self.tabla.figpos and ([i,j], self.enemycolor) not in self.tabla.figpos:
                break
            self.posmoves.append([i, j])
            if ([i,j], self.enemycolor) in self.tabla.figpos:
                break
class Kraljica(Figura):

    def __init__(self, tabla, pos, boja):
        self.type = "kraljica"
        super().__init__(tabla, pos, boja)

    def possiblemoves(self):
        Lovac.possiblemoves(self)
        Top.possiblemoves(self)
class Konj(Figura):

    def __init__(self, tabla, pos, boja):
        self.type = "konj"
        super().__init__(tabla, pos, boja)

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        xx = [[x+2, x-2], [x+1, x-1]]
        yy = [[y-1, y+1], [y+2, y-2]]
        for g, _ in enumerate(xx):
            for i in xx[g]:
                for j in yy[g]:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        if ([i, j], self.boja) not in self.tabla.figpos or ([i,j], self.enemycolor) in self.tabla.figpos:
                            self.posmoves.append([i, j])
class Kralj(Figura):
    def __init__(self, tabla, pos, boja):
        self.type = "kralj"
        super().__init__(tabla, pos, boja)

    def possiblemoves(self):
        x = self.pos[0]
        y = self.pos[1]
        xx = [x+1, x-1, x]
        yy = [y+1, y-1, y]
        for i in xx:
            for j in yy:
                if i != x or j != y:
                    if i > -1 and j > -1 and i < 8 and j < 8:
                        if ([i,j], self.boja) not in self.tabla.figpos:
                            temp = self.pos
                            Figura.kraljcheck = 1
                            self.move([i, j])
                            self.posmoves.append([i, j])
                            for fig in self.tabla.figure:
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
                        if ([i,j], self.boja) not in self.tabla.figpos:
                            self.posmoves.append([i, j])

def main(*args):
    root = Tk()
    players = []
    players.append(Player("Djordje", "white"))
    players.append(Player("Boris", "black"))
    tabla = Tabla(root, (0, 0), players, "")
    players2 = []
    players2.append(Player("Djordje", "white"))
    players2.append(Player("Boris", "black"))
    t = Tabla(root, (0, 1), players2, "red")
    #ta = Tabla(root, (0, 1))
    root.mainloop()

if __name__ == '__main__':
    _, *script_args = sys.argv
    main(*script_args)