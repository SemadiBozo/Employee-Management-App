from tkinter import Tk,Label,Button,PhotoImage
import sys
import pythonprojectlib as lib
font="Bahnschrift" #Font
program=lib.Program() #Calling Program Class
#----------Main Body----------
form=Tk()
bg=PhotoImage(file="bg.png")
img=PhotoImage(file="img.png")
form.title("Main Program")
form.geometry("500x300")
form.resizable(False,False)
form.iconbitmap("icon1.ico")
form.overrideredirect(True)
#----------Background Image----------
Label(form,image=bg).place(x=-2.4,y=-2.4)
Label(form,image=img).pack(side="top")
#----------Main Buttons-----------
Button(form,font=(font,20,"bold"),text="Run Program",command=program.Start).place(x=150,y=135)
Button(form,font=(font,20,"bold"),text="Exit",command=sys.exit).place(x=210,y=220)
form.mainloop()