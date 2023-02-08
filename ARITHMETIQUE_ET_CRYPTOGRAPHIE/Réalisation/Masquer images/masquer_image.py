from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb



root=Tk()
root.title("Steganographie - Masquer Texte")
root.geometry("1000x650+500+260")
root.resizable(False,False)
root.configure(bg="#FFA48F")

def AfficherImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Selectionner une image du ficher',filetypes=(("PNG file", "*.png"),("JPG File","*.jpg"),("BMP File","*.bmp"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def JoindreCle():
    global Cle
    Cle=frame2.get(1.0,END)
    filename =lsb.hide(str(filename),Cle)

def AfficherCle():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Selectionner la clé du ficher',filetypes=(("PNG file", "*.png"),("JPG File","*.jpg"),("BMP File","*.bmp"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lb2.configure(image=img,width=250,height=250)
    lb2.image=img
   
def SauvegarderImage():
    filename.save("hidden.png")



#first Frame
frame1=Frame(root,bd=3,bg="#FFEC8F",width=380,height=300,relief=GROOVE)
frame1.place(x=40,y=80)

lbl=Label(frame1,bg="black")
lbl.place(x=40,y=10)

#secon Frame
frame2=Frame(root,bd=3,bg="#FFCF8F",width=360,height=300,relief=GROOVE)
frame2.place(x=600,y=80)

lb2=Label(frame2,bg="black")
lb2.place(x=40,y=10)

#third Frame
frame3=Frame(root,bd=3,bg="#C8FF8F",width=380,height=100,relief=GROOVE)
frame3.place(x=40,y=370)

Button(frame3,text="Ouvrir Image",width=12,height=2,font="arial 14 bold",command=AfficherImage).place(x=20,y=20)
Button(frame3,text="Sauvegarder Image",width=15,height=2,font="arial 14 bold",command=SauvegarderImage).place(x=180,y=20)


#fouth Frame
frame4=Frame(root,bd=3,bg="#C8FF8F",width=360,height=100,relief=GROOVE)
frame4.place(x=600,y=370)

Button(frame4,text="Ouvrir Cle",width=12,height=2,font="arial 14 bold",command=AfficherCle).place(x=20,y=20)
Button(frame4,text="Joindre CLe",width=12,height=2,font="arial 14 bold",command=JoindreCle).place(x=180,y=20)


root.mainloop()
