from  tkinter import *

class Slide15(Tk):
    def __init__(self):
        Tk.__init__(self)

        frame = game(self)
        frame.pack()

class game(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        self.llist = [[0]*4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                if i != 3 or j!=3:
                    self.llist[i][j] = Label(self,text=i*4+j+1,background = 'orange',bd = 1, relief = 'ridge',height = 4, width = 8)
                    self.llist[i][j].grid(row = i, column = j)
                    self.llist[i][j].bind('<Button-1>',lambda event, r = i, c = j: self.click(r,c))
                else:
                    self.llist[i][j] = Label(self,text=' ',background = 'white',bd = 1, relief = 'ridge',height = 4, width = 8)
                    self.llist[i][j].grid(row = i, column = j)
                    self.llist[i][j].bind('<Button-1>',lambda event, r = i, c = j: self.click(r,c))

    def click(self,r,c):
        if self.llist[r][c]['text'] == ' ':
            return

        for i in range(4):
            if self.llist[r][i]['text'] == ' ':
                x = i-c
                q = int(((x**2)**(1/2))/x/(-1))
                for j in range(x,0,q):
                    a = self.llist[r][c+j]
                    self.llist[r][c+j] = self.llist[r][c+j+q]
                    self.llist[r][c+j+q] = a
                break

            elif self.llist[i][c]['text'] == ' ':
                x = i-r
                q = int(((x**2)**(1/2))/x/(-1))
                for j in range(x,0,q):
                    a = self.llist[r+j][c]
                    self.llist[r+j][c] = self.llist[r+j+q][c]
                    self.llist[r+j+q][c] = a
                break
        
        for i in range(4):
            for j in range(4):
                self.llist[i][j].grid(row = i,column =j)
                self.llist[i][j].bind('<Button-1>',lambda event, r = i, c = j: self.click(r,c))

        

if __name__ == '__main__':
    gameone = Slide15()
    gameone.mainloop()
