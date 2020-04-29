from  tkinter import *
from tkinter import messagebox
import random

class Slide15(Tk):
    def __init__(self):
        Tk.__init__(self)

        frame = game(self)
        frame.pack()

class game(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        font = ('Banschrift',25)
        color = '#b2babb'
        self.llist = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if i != 3 or j!=3:
                    self.llist[i][j] = Label(self,text=i*4+j+1,font = font,background = color,bd = 1, relief = 'ridge',height = 2, width = 4)
                else:
                    self.llist[i][j] = Label(self,text=' ',font = font,background = 'white',bd = 1, relief = 'ridge',height = 2, width = 4)
        self.shuffle()
        self.refresh()

    def click(self,r,c):
        if self.llist[r][c]['text'] == ' ':
            return

        for i in range(4):
            if self.llist[r][i]['text'] == ' ':
                x = i-c
                q = int(((x**2)**(1/2))/x/(-1))
                for j in range(x,0,q):
                    self.swap(r,c+j,r,c+j+q)
                break

            elif self.llist[i][c]['text'] == ' ':
                x = i-r
                q = int(((x**2)**(1/2))/x/(-1))
                for j in range(x,0,q):
                    self.swap(r+j,c,r+j+q,c)
                break

        self.refresh()
        
    def refresh(self):
        for i in range(4):
            for j in range(4):
                self.llist[i][j].grid(row = i,column =j)
                self.llist[i][j].bind('<Button-1>',lambda event, r = i, c = j: self.click(r,c))

        self.checkwin()

    def swap(self,r,c,s,d):
        a = self.llist[r][c]
        self.llist[r][c] = self.llist[s][d]
        self.llist[s][d] = a

    def checkwin(self):
        f = 1
        for i in range(4):
            for j in range(4):
                if i != 3 or j!=3:
                    if self.llist[i][j]['text'] != i*4+j+1:
                        f = 0
        
        if f:
            messagebox.showinfo('Congradulations','YOU WIN!!')

    def shuffle(self):
        l = []
        for i in range(100):
            a = random.randint(0,3)
            b = random.randint(0,3)
            c = random.randint(0,3)
            d = random.randint(0,3)    
            self.swap(a,b,c,d)
        for i in range(4):
            for j in range(4):
                l.append(self.llist[i][j]['text'])
                if self.llist[i][j]['text'] == ' ':
                    a = 4-i
                elif self.llist[i][j]['text'] == 1:
                    a1,b1 = i,j
                elif self.llist[i][j]['text'] == 2:
                    a2,b2 = i,j
        j = 1
        t = 0
        def inversions(l,j):
            s = 0
            for i in l:
                if i != ' ':
                    if i < j and l.index(i) > l.index(j):
                        s += 1
            return(s)
        for i in l:
            if i != ' ':
                t += inversions(l,i)
        if t%2 == 0:
            if a%2 == 0:
                self.swap(a1,b1,a2,b2)
        else:
            if a%2 != 0:
                self.swap(a1,b1,a2,b2)

if __name__ == '__main__':
    gameone = Slide15()
    gameone.mainloop()
