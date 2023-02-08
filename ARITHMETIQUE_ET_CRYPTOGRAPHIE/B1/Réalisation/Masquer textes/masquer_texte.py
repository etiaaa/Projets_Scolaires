from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb


Affichage =Tk()
Affichage.title("Steganographie - Masquer du texte")
Affichage.geometry("1000x650+500+260")
Affichage.resizable(False,False)
Affichage.configure(bg="#F4D8B9")

def AfficherImage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Selectionner une image du fichier',filetypes=(("PNG file", "*.png"),("JPG File","*.jpg"),("BMP File","*.bmp"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image=img

def Cacher():
    global secret
    message=text1.get(1.0,END)
    secret =lsb.hide(str(filename),message)

def AfficherTexte():
    clear_message=lsb.reveal(filename)
    text1.delete(1.0,END)
    text1.insert(END, clear_message)

def SauvegarderImage():
    secret.save("hidden.png")


#Fond Image
frame1=Frame(Affichage,bd=3,bg="#B89B9B",width=380,height=300,relief=GROOVE)
frame1.place(x=40,y=80)

lbl=Label(frame1,bg="black")
lbl.place(x=40,y=10)

#Fond Texte
frame2=Frame(Affichage,bd=3,bg="#B96F6F",width=360,height=300,relief=GROOVE)
frame2.place(x=600,y=80)

text1=Text(frame2,font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=300, height=200)

#Boutons Image
frame3=Frame(Affichage,bd=3,bg="#F8A6A6",width=380,height=100,relief=GROOVE)
frame3.place(x=40,y=370)

Button(frame3,text="Afficher Image",width=12,height=2,font="arial 14 bold",command=AfficherImage).place(x=20,y=20)
Button(frame3,text="Sauvegarder Image",width=15,height=2,font="arial 14 bold",command=SauvegarderImage).place(x=180,y=20)


#Boutons Texte
frame4=Frame(Affichage,bd=3,bg="#F8A6A6",width=360,height=100,relief=GROOVE)
frame4.place(x=600,y=370)

Button(frame4,text="Cacher Texte",width=12,height=2,font="arial 14 bold",command=Cacher).place(x=20,y=20)
Button(frame4,text="Afficher Texte",width=12,height=2,font="arial 14 bold",command=AfficherTexte).place(x=180,y=20)


Affichage.mainloop()
