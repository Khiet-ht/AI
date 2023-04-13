from tkinter import *
from random import randint
def callback(r,c):
    global player
    global stop_game
    if player == 'X' and states[r][c] == 0 and stop_game == False :
        b[r][c].configure(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
        check_for_winner()
    if player == 'O' and stop_game == False :
       # rd()
        stupid()
        danh_an()
    check_stop_game()
    check_for_winner()
def stupid():
    global player
#chặn cột    
    for i in range(3):
        if states[i][0] == states[i][1]!=0 and player == "O" and states[i][2] == 0:
            b[i][2].configure(text='O', fg='orange', bg='black')
            states[i][2] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[i][1] == states[i][2]!=0 and player == "O" and states[i][0] == 0:
            b[i][0].configure(text='O', fg='orange', bg='black')
            states[i][0] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[i][0] == states[i][2]!=0 and player == "O" and states[i][1] == 0:
            b[i][1].configure(text='O', fg='orange', bg='black')
            states[i][1] = "O"
            player = "X"
            check_for_winner() 
#chặn hàng            
    for i in range(3):
        if states[0][i]==states[1][i]!=0 and player == "O":
            b[2][i].configure(text='O', fg='orange', bg='black')
            states[2][i] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[0][i]==states[2][i]!=0 and player == "O" and states[1][i] == 0:
            b[1][i].configure(text='O', fg='orange', bg='black')
            states[1][i] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[2][i]==states[1][i]!=0 and player == "O" and states[0][i] == 0:
            b[0][i].configure(text='O', fg='orange', bg='black')
            states[0][i] = "O"
            player = "X"
            check_for_winner()
#chặn chéo            

    if states[0][0]==states[1][1]!=0 and player == "O" :
        b[2][2].configure(text='O', fg='orange', bg='black')
        states[2][2] = "O"
        player = "X"
        check_for_winner()
    if states[0][0]==states[2][2]!=0 and player == "O" and states[1][1] == 0:
        b[1][1].configure(text='O', fg='orange', bg='black')
        states[1][1] = "O"
        player = "X"
        check_for_winner()
    if states[2][2]==states[1][1]!=0 and player == "O" and states[0][0] == 0:
        b[0][0].configure(text='O', fg='orange', bg='black')
        states[0][0] = "O"
        player = "X"
        check_for_winner()
     
    if states[2][0]==states[1][1]!=0 and player == "O" and states[0][2] == 0:
        b[0][2].configure(text='O', fg='orange', bg='black')
        states[0][2] = "O"
        player = "X"
        check_for_winner()
    if states[0][2]==states[1][1]!=0 and player == "O" and states[2][0] == 0:
        b[2][0].configure(text='O', fg='orange', bg='black')
        states[2][0] = "O"
        player = "X"
        check_for_winner()
    if states[2][0]==states[0][2]!=0 and player == "O" :
        b[1][1].configure(text='O', fg='orange', bg='black')
        states[1][1] = "O"
        player = "X"
        check_for_winner()
    if player == 'O' and stop_game == False:
        r=randint(0, 2)
        c=randint(0, 2)
        while states[r][c] != 0:
            r=randint(0, 2)
            c=randint(0, 2)
            check_stop_game()
            if stop_game==1:
                break
        else:
            b[r][c].configure(text='O', fg='orange', bg='black')
            states[r][c] = 'O'
            player = 'X'
                    
def danh_an():
    global player
 #cột    
    for i in range(3):
        if states[i][0] == states[i][1] =='O' and player == "O" and states[i][2] == 0:
            b[i][2].configure(text='O', fg='orange', bg='black')
            states[i][2] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[i][1] == states[i][2] =='O' and player == "O" and states[i][0] == 0:
            b[i][0].configure(text='O', fg='orange', bg='black')
            states[i][0] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[i][0] == states[i][2]=='O' and player == "O" and states[i][1] == 0:
            b[i][1].configure(text='O', fg='orange', bg='black')
            states[i][1] = "O"
            player = "X"
            check_for_winner() 
#hàng            
    for i in range(3):
        if states[0][i]==states[1][i]=='O' and player == "O":
            b[2][i].configure(text='O', fg='orange', bg='black')
            states[2][i] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[0][i]==states[2][i]=='O' and player == "O" and states[1][i] == 0:
            b[1][i].configure(text='O', fg='orange', bg='black')
            states[1][i] = "O"
            player = "X"
            check_for_winner()
    for i in range(3):
        if states[2][i]==states[1][i]=='O' and player == "O" and states[0][i] == 0:
            b[0][i].configure(text='O', fg='orange', bg='black')
            states[0][i] = "O"
            player = "X"
            check_for_winner()
#chéo            

    if states[0][0]==states[1][1]=='O' and player == "O" :
        b[2][2].configure(text='O', fg='orange', bg='black')
        states[2][2] = "O"
        player = "X"
        check_for_winner()
    if states[0][0]==states[2][2]=='O' and player == "O" and states[1][1] == 0:
        b[1][1].configure(text='O', fg='orange', bg='black')
        states[1][1] = "O"
        player = "X"
        check_for_winner()
    if states[2][2]==states[1][1]=='O' and player == "O" and states[0][0] == 0:
        b[0][0].configure(text='O', fg='orange', bg='black')
        states[0][0] = "O"
        player = "X"
        check_for_winner()
     
    if states[2][0]==states[1][1]=='O' and player == "O" and states[0][2] == 0:
        b[0][2].configure(text='O', fg='orange', bg='black')
        states[0][2] = "O"
        player = "X"
        check_for_winner()
    if states[0][2]==states[1][1]=='O' and player == "O" and states[2][0] == 0:
        b[2][0].configure(text='O', fg='orange', bg='black')
        states[2][0] = "O"
        player = "X"
        check_for_winner()
    if states[2][0]==states[0][2]=='O' and player == "O" :
        b[1][1].configure(text='O', fg='orange', bg='black')
        states[1][1] = "O"
        player = "X"
        check_for_winner()
    if player == 'O' and stop_game == False:
        stupid()
def rd():
    global player     
    r=randint(0, 2)
    c=randint(0, 2)
    while states[r][c] != 0:
        r=randint(0, 2)
        c=randint(0, 2)
        check_stop_game()
        if stop_game==1:
            break
    else:
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
def get_open_spots():
    return [[r,c] for r in range(3) for c in range(3)
            if states[r][c]==0]
def check_stop_game():
    global stop_game
    if get_open_spots()==[]:
        stop_game=True
    else: stop_game=False
def check_for_winner():
    global stop_game
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='grey')
            b[i][1].configure(bg='grey')
            b[i][2].configure(bg='grey')
            stop_game = True

    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='grey')
            b[1][i].configure(bg='grey')
            b[2][i].configure(bg='grey')
            stop_game = True

    if states[0][0]==states[1][1]==states[2][2]!=0:
        b[0][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[2][2].configure(bg='grey')
        stop_game = True

    if states[2][0]==states[1][1]==states[0][2]!=0:
        b[2][0].configure(bg='grey')
        b[1][1].configure(bg='grey')
        b[0][2].configure(bg='grey')
        stop_game = True
def restart():
    global stop_game
    global b
    global states
    global player
    for i in range(3):
        for j in range(3):
            b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',command = lambda r=i,c=j: callback(r,c))
            b[i][j].grid(row = i, column = j)
    states = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    stop_game=False
    player = 'X'
root = Tk()
b = [[0,0,0],
     [0,0,0],
     [0,0,0]]

states = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(3):
    for j in range(3):
        b[i][j] = Button(font=('Verdana', 56), width=3, bg='yellow',command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)

b1=Button(text='RESTART',font=('Times',24), command=restart)
b1.grid(row=1, column=3,)
player = 'X'
stop_game = False

mainloop()