from tkinter import *
from googletrans import Translator
from tkinter import ttk, messagebox


root = Tk()
root.geometry()

def translate():
    translator= Translator()
  
    translated0= translator.translate( og_text.get(1.0, END), src='en', dest='fr')
              
    trans_text.insert(1.0,translated0.text)
    print(translated0)
   
def clear():
  
    og_text.delete(1.0, END)
    trans_text.delete(1.0, END)
    
og_text = Text(root, height=10, width=40)
og_text.grid(row=0, column=0, pady=20, padx=10)

trans_btn= Button(root, text="translate" , command= translate)
trans_btn.grid(row=0,column=1)

trans_text = Text(root, height=10, width=40)
trans_text.grid(row=0, column=2, pady=20, padx=10)

og_lang1= Label(root,width=50,  text="english")

og_lang1.grid(row=1, column=0)

trans_lang=Label(root,width=50,  text="french")

trans_lang.grid(row=1, column=2)

clear_btn= Button(root, text= "clear", command=clear)
clear_btn.grid(row= 3, column=1)

root.mainloop()
