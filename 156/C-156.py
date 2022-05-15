# -*- coding: utf-8 -*-
"""
Created on Sun May 15 09:28:57 2022

@author: Cupcake@250
"""
from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.title("Dice Game")
root.geometry("400x500")
root.configure(bg="yellow")

img=ImageTk.PhotoImage(Image.open("dice1.4.jpg"))

label_player1=Label(root,text="Player1",bg="royal blue",fg="white")
label_player1.place(relx=0.1,rely=0.3,anchor=CENTER)

label_player2=Label(root,text="Player2",bg="royal blue",fg="white")
label_player2.place(relx=0.9,rely=0.3,anchor=CENTER)

label_score1=Label(root,text="",bg="green",fg="white")
label_score1.place(relx=0.1,rely=0.4,anchor=CENTER)

label_score2=Label(root,text="",bg="green",fg="white")
label_score2.place(relx=0.9,rely=0.4,anchor=CENTER)

random_dice_label=Label(root,text="",bg="red",fg="white")
random_dice_label.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()

