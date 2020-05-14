from  tkinter import Tk,Label,Frame,Button
from tkinter import messagebox
import random

class Slide15(Tk):
    def __init__(self):
        Tk.__init__(self)

        default = 4
        self.frame = game(self,default)
        self.frame.grid(row = 0,column = 0)
        
        self.playagainb = Button(self,text = 'Play Again',command = lambda:self.playagain(default))
        self.playagainb.grid(row = 1, column = 0,sticky = 'W')

        self.settingsb = Button(self,text = 'Settings',command = lambda:self.settings())
        self.settingsb.grid(row = 1, column = 0,sticky = 'E')

    def aftergame(self):
        self.frame.destroy()

    def playagain(self,n):
        try:
            self.temp.destroy()
        except:
            pass
        finally:
            self.frame.destroy()
            self.frame = game(self,n)
            self.frame.grid(row = 0,column = 0)

    def settings(self):
        self.temp = Tk()
        b3 = Button(self.temp,text = '3x3',command = lambda:self.playagain(3))
        b3.grid(row = 0,column = 0)

        b4 = Button(self.temp,text = '4x4',command = lambda:self.playagain(4))
        b4.grid(row = 1,column = 0)


class game(Frame):
    def __init__(self,parent,g):
        Frame.__init__(self,parent)
        self.parent = parent
        font = ('Banschrift',25)
        color = '#b2babb'
        self.width = g
        self.llist = [[0]*self.width for _ in range(self.width)]
        for i in range(self.width):
            for j in range(self.width):
                if i != self.width-1 or j!=self.width-1:
                    self.llist[i][j] = Label(self,text=i*self.width+j+1,font = font,background = color,bd = 1, relief = 'ridge',height = 2, width = 4)
                else:
                    self.llist[i][j] = Label(self,text=' ',font = font,background = 'white',bd = 1, relief = 'ridge',height = 2, width = 4)
        self.shuffle()
        self.refresh()

    def click(self,r,c):
        if self.llist[r][c]['text'] == ' ':
            return

        for i in range(self.width):
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
        for i in range(self.width):
            for j in range(self.width):
                self.llist[i][j].grid(row = i,column =j)
                self.llist[i][j].bind('<Button-1>',lambda event, r = i, c = j: self.click(r,c))

        self.checkwin()

    def swap(self,r,c,s,d):
        a = self.llist[r][c]
        self.llist[r][c] = self.llist[s][d]
        self.llist[s][d] = a

    def checkwin(self):
        flag = 1
        for i in range(self.width):
            for j in range(self.width):
                if i != self.width-1 or j!=self.width-1:
                    if self.llist[i][j]['text'] != i*self.width+j+1:
                        flag = 0

        if flag:
            messagebox.showinfo('Congradulations','YOU WIN!!')
            self.parent.aftergame()

    def shuffle(self):
        l = []
        for i in range(self.width*10):#randomly sliding 100 times
            a = random.randint(0,self.width-1)
            b = random.randint(0,self.width-1)
            c = random.randint(0,self.width-1)
            d = random.randint(0,self.width-1)
            self.swap(a,b,c,d)

        for i in range(self.width):#making a linear list
            for j in range(self.width):
                l.append(self.llist[i][j]['text'])
                if self.llist[i][j]['text'] == ' ':
                    a = self.width-i
                elif self.llist[i][j]['text'] == 1:
                    a1,b1 = i,j
                elif self.llist[i][j]['text'] == 2:
                    a2,b2 = i,j

        def inversions(l,j):
            s = 0
            for i in l:
                if i != ' ':
                    if i < j and l.index(i) > l.index(j):
                        s += 1
            return(s)

        inv_count = 0
        for i in l:# counting total no. of inversions
            if i != ' ':
                inv_count += inversions(l,i)

        if self.width % 2 == 0:
            if inv_count%2 == 0:
                if a%2 == 0:
                    self.swap(a1,b1,a2,b2)
            else:
                if a%2 != 0:
                    self.swap(a1,b1,a2,b2)
        else:
            if inv_count % 2 != 0:
                self.swap(a1,b1,a2,b2)


if __name__ == '__main__':
    gameone = Slide15()
    gameone.mainloop()
