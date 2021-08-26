from tkinter import *
import time
import os
from tkinter.messagebox import showinfo
import warnings
from tkinter import messagebox as mb




warnings.filterwarnings('ignore')

rt=Tk()
rt.geometry("1600x800+0+0") 
rt.title("TIC TAC TOE")
rt.configure(bg='light green')
########################################################################################################################
Tops=Frame(rt,width = 1600,height = 50,bg='light green',relief=SUNKEN)
Tops.pack(side=TOP)

f1=Frame(rt,width = 550,height = 700,bg='light green',relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(rt,width = 300,height = 700,bg='light green',relief=SUNKEN)
f2.pack(side=RIGHT)
########################################################################################################################
lblInfo=Label(Tops,font=("arial",30,"bold"),text="WELCOME TO THE GAME TIC TAC TOE",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

localtime=time.asctime(time.localtime(time.time()))#DATE TIME FUNCTION

lblDateTime=Label(Tops,font=("arial",20,"bold"),text=localtime,bg="light green",fg="dark green",bd=10,anchor="w")
lblDateTime.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="PRESS START BUTTON TO START THE GAME ",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()
#########################################################################################################################
def start():
    global root
    root=Toplevel(rt)
    root.title("TIC TAC TOE")
    root.configure(bg="light green")
    global numbers
    global x


    numbers=[1,2,3,4,5,6,7,8,9] 
    # y='X' for player1 and 'O' for player2
    y=""
    # x is the counter to keep counting the number of chances
    x=0
    #boards is a list to store the mark with respect to the cell number
    boards=["board"]*10

    def result(boards,mark):
        return ((boards[1] == boards[2] == boards [3] == mark) 
                or (boards[4] == boards[5] == boards [6] == mark) 
                or (boards[7] == boards[8] == boards [9] == mark) 
                or (boards[1] == boards[4] == boards [7] == mark) 
                or (boards[2] == boards[5] == boards [8] == mark)
                or (boards[3] == boards[6] == boards [9] == mark)
                or (boards[1] == boards[5] == boards [9] == mark) 
                or (boards[3] == boards[5] == boards [7] == mark))


    def define_sign(number):
        global x,y,numbers
        """ Checking which button has been clicked and checking if the button has been already clicked or not to avoid over-writing"""
        if number==1 and number in numbers:
            numbers.remove(number)
           
            # If the value of x is even, Person1 will play and vivee versa
            if x%2==0:
                y='X'
                boards[number]=y
            elif x%2!=0:
                y='O'
                boards[number]=y
            #Using config, we write mark the button with appropriate value. 
            b1.config(text=y)
            x=x+1
            mark=y
            # Here we are calling the result() to decide whether we have got the winner or not
            if(result(boards,mark) and mark=='X' ):
                #If Player1 is the winner show a dialog box stating the winner
                showinfo("Result","Player1 wins")
                #Call the destroy function to close the GUI
                call()
            elif(result(boards,mark) and mark=='O'):
                showinfo("Result","Player2 wins")
                call()
            
        if number==2 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y
            elif x%2!=0:
                y='O'
                boards[number]=y
                
            b2.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark)and mark=='X' ):
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,mark)and mark=='O' ):
                showinfo("Reuslt","Player2 wins")
                call()
            
        if number==3 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y

            elif x%2!=0:
                y='O'
                boards[number]=y    
            b3.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark)and mark=='X'):
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,mark) and mark=='O'):
                showinfo("Result","Player2 wins")
                call()
            
        if number==4 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y
            
            elif x%2!=0:
                y='O'
                boards[number]=y  
            b4.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark)and mark=='X'):
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,mark) and mark=='O'):
                showinfo("Result","Player2 wins")
                call()
            
        if number==5 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y
            elif x%2!=0:
                y='O'
                boards[number]=y
                           
            b5.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark)and mark=='X' ):
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,"O")and mark=='O'):
                showinfo("Result","Player2 wins")
                call()
            
        if number==6 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y
            elif x%2!=0:
                y='O'
                boards[number]=y

            b6.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark) and mark=='X'):
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,mark)and mark=='O'):
                showinfo("Result","Player2 wins")
                call()
            
        if number==7 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y

            elif x%2!=0:
                y='O'
                boards[number]=y

            b7.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark) and mark=='X' ):
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,mark) and mark=='O'):
                print("Player2 wins")
                showinfo("Result","Player2 wins")
                call()
            
        if number==8 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y

            elif x%2!=0:
                y='O'
                boards[number]=y
                
            b8.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark) and mark=='X'):
                print("Player1 wins")
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,"O")and mark=='O'):
                print("Player2 wins")
                showinfo("Result","Player2 wins")
                call()
        if number==9 and number in numbers:
            numbers.remove(number)
            if x%2==0:
                y='X'
                boards[number]=y

            elif x%2!=0:
                y='O'
                boards[number]=y
                
            b9.config(text=y)
            x=x+1
            mark=y
            if(result(boards,mark) and mark=='X'):
                print("Player1 wins")
                showinfo("Result","Player1 wins")
                call()
            elif(result(boards,mark) and mark=='O'):
                print("Player2 wins")
                showinfo("Result","Player2 wins")
                call()
                
        # If we have not got any winner, display the dialogbox stating the match has bee tied.
        if(x>8 and result(boards,'X')==False and result(boards,'O')==False):
            showinfo("Result","Match Tied")
            
            call()
            


    label1=Label(root,text="Player1 : X",font=("arial",15,"bold"),bg="light green",fg="dark green",bd=10,anchor="w")
    label1.grid(row=0,column=1)


    l2=Label(root,text="Player2 : O",font=("arial",15,"bold"),bg="light green",fg="dark green",bd=10,anchor="w")
    l2.grid(row=0,column=2)


    
       


    b1=Button(root,width=20,height=10,command=lambda:define_sign(1))
    b1.grid(row=1,column=1)
    b2=Button(root,width=20,height=10,command=lambda:define_sign(2))
    b2.grid(row=1,column=2)
    b3=Button(root,width=20,height=10,command=lambda: define_sign(3))
    b3.grid(row=1,column=3)
    b4=Button(root,width=20,height=10,command=lambda: define_sign(4))
    b4.grid(row=2,column=1)
    b5=Button(root,width=20,height=10,command=lambda: define_sign(5))
    b5.grid(row=2,column=2)
    b6=Button(root,width=20,height=10,command=lambda: define_sign(6))
    b6.grid(row=2,column=3)
    b7=Button(root,width=20,height=10,command=lambda: define_sign(7))
    b7.grid(row=3,column=1)
    b8=Button(root,width=20,height=10,command=lambda: define_sign(8))
    b8.grid(row=3,column=2)
    b9=Button(root,width=20,height=10,command=lambda: define_sign(9))
    b9.grid(row=3,column=3)
    root.mainloop()

lblInfo=Label(Tops,font=("arial",23,"bold"),text="",bg="light green",fg="dark green",bd=10,anchor="w")
lblInfo.pack()

btn15=Button(rt,padx=16,pady=16,bd=8,fg="dark green",font=("arial",18,"bold"),text="START",bg="light green",
                    command=start,anchor="w",width=10,height=0,compound="c")
btn15.place(x=220,y=420)
def call(): 
	res = mb.askquestion('Exit Application', 'Do you really want to exit') 
	
	if res == 'yes' : 
		rt.destroy() 
		
	else : 
		mb.showinfo('Return', 'Returning to main application') 



btn16=Button(rt,padx=16,pady=16,bd=8,fg="dark green",font=("arial",18,"bold"),text="Quit",bg="light green",
                    command=call,anchor="w",width=10,height=0,compound="c")
btn16.place(x=620,y=420)

rt.mainloop()
