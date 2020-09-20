from tkinter import *
import tkinter.messagebox
import random

root = Tk()
root.title("Ernie's Random Number Generator-Two Dimensional Graph Plots")
root.geometry("1380x640+0+0")
root.config(bg="Cadet Blue")

#--------Outer Frame-------------------------------
MainFrame =Frame(root,bg="Cadet Blue")
MainFrame.grid()


#-------------Inner Frame 1-Left Side------------------------

DataFrame1 =Frame(MainFrame,bd=4,width=1000,height=600,padx=40,pady=33,relief =RIDGE,bg="Cadet Blue")
DataFrame1.grid(row=0,column=0)

#-------------Inner Frame 2-Right Side------------------------

DataFrame2 =Frame(MainFrame,bd=5,width=1000,height=600,padx=40,pady=70,relief =RIDGE,bg="Cadet Blue")
DataFrame2.grid(row=0,column=1)



lblTitle=Label(DataFrame1,font=("Arial",14,"bold"),text="DATA SCIENCE",bg="Cadet Blue",fg="Yellow")
lblTitle.grid(row= 0, column=0,sticky =W)

#------------------------ iCanvas Function----------

def iCanv():
    canvas.delete("all")
    canvas.create_line(100,450,800,450,width=4)
    canvas.create_line(100,450,100,50,width=4)

    for i in range(11):
        x= 100 + (i*60)
        canvas.create_line(x,450,x,445,width=4)
        canvas.create_text(x,455, text="%d"%(50*i), anchor=N)

    for i in range(10):
        y= 450 - (i*40)
        canvas.create_line(100,y,105,y,width=4)
        canvas.create_text(95,y, text="%5.1f"%(50.*i), anchor="e")






#----------------------Variables-------------------------------

#-- in X:

Ax1 = IntVar()
Ax2 = IntVar()
Ax3 = IntVar()
Ax4 = IntVar()
Ax5 = IntVar()
Ax6 = IntVar()
Ax7 = IntVar()
Ax8 = IntVar()

#-- in Y:

Ay1 = IntVar()
Ay2 = IntVar()
Ay3 = IntVar()
Ay4 = IntVar()
Ay5 = IntVar()
Ay6 = IntVar()
Ay7 = IntVar()
Ay8 = IntVar()

#--- Labeling Axes:

lblX_Axis=Label(DataFrame2,font=("Arial",14,"bold"),text="X Axis",bg="Cadet Blue",fg="Yellow")
lblX_Axis.grid(row= 0, column=0,sticky =W)

lblY_Axis=Label(DataFrame2,font=("Arial",14,"bold"),text="Y Axis",bg="Cadet Blue",fg="White")
lblY_Axis.grid(row= 0, column=1,sticky =W)

#----- Text Widget(Entry Widget)---

txtAxis1x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax1)
txtAxis1x.grid(row=1,column=0)

txtAxis1y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay1)
txtAxis1y.grid(row=1,column=1)

txtAxis2x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax2)
txtAxis2x.grid(row=2,column=0)

txtAxis2y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay2)
txtAxis2y.grid(row=2,column=1)


txtAxis3x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax3)
txtAxis3x.grid(row=3,column=0)

txtAxis3y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay3)
txtAxis3y.grid(row=3,column=1)

txtAxis4x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax4)
txtAxis4x.grid(row=4,column=0)

txtAxis4y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay4)
txtAxis4y.grid(row=4,column=1)


txtAxis5x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax5)
txtAxis5x.grid(row=5,column=0)

txtAxis5y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay5)
txtAxis5y.grid(row=5,column=1)

txtAxis6x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax6)
txtAxis6x.grid(row=6,column=0)

txtAxis6y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay6)
txtAxis6y.grid(row=6,column=1)


txtAxis7x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax7)
txtAxis7x.grid(row=7,column=0)

txtAxis7y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay7)
txtAxis7y.grid(row=7,column=1)

txtAxis8x= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ax8)
txtAxis8x.grid(row=8,column=0)

txtAxis8y= Entry(DataFrame2,font=("Arial",14,"bold"),bg="Ghost White",borderwidth=5, width=10,bd=10,textvariable=Ay8)
txtAxis8y.grid(row=8,column=1)





#----------------------Creating Canvas--------------------

canvas = Canvas(DataFrame1,width=900,height=470,bg ="Powder Blue")
canvas.grid(row=1,column=0)


#------- X Axis:
canvas.create_line(100,450,800,450,width=4)

#------- Y Axis:
canvas.create_line(100,450,100,50,width=4)





#-------GRADING  AXES---------------------

#----Grading in X:

for i in range(11):
    x= 100 + (i*60)
    canvas.create_line(x,450,x,445,width=4)
    canvas.create_text(x,455, text="%d"%(50*i), anchor=N)

#----Grading in Y:

for i in range(10):
    y= 450 - (i*40)
    canvas.create_line(100,y,105,y,width=4)
    canvas.create_text(95,y, text="%5.1f"%(50.*i), anchor="e")

#------------------------ FUNCTIONS------------------------------

def iGraph():
    iCanv()
    x1 = random.randint(20,109)
    x2 = random.randint(20,109)
    x3 = random.randint(20,109)
    x4 = random.randint(20,109)
    x5 = random.randint(20,109)
    x6 = random.randint(20,109)
    x7 = random.randint(20,109)
    x8 = random.randint(20,109)



    y1 = random.randint(50,450)
    y2 = random.randint(50,450)
    y3 = random.randint(50,450)
    y4 = random.randint(50,450)
    y5 = random.randint(50,450)
    y6 = random.randint(50,450)
    y7 = random.randint(50,450)
    y8 = random.randint(50,450)


    Ax1.set(x1)
    Ax2.set(x2)
    Ax3.set(x3)
    Ax4.set(x4)
    Ax5.set(x5)
    Ax6.set(x6)
    Ax7.set(x7)
    Ax8.set(x8)


    Ay1.set(y1)
    Ay2.set(y2)
    Ay3.set(y3)
    Ay4.set(y4)
    Ay5.set(y5)
    Ay6.set(y6)
    Ay7.set(y7)
    Ay8.set(y8)


    for x,y in [(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),
                (x6,y6),(x7,y7),(x8,y8)]:


        x = 50 +7*x
        y = 450 -(4*y)/5

        canvas.create_oval(x-6,y-6,x+6,y+6,width=2,
                           outline ="Black",fill = "Yellow")


def iExit():
    qExit = tkinter.messagebox.askyesno("Exit System","Do You Want To Exit ?")
    if qExit > 0:
        root.destroy()
        return

#------------------------Button-Trigger-------------------------------

Button(DataFrame2, text ="Graph",font=("Arial",12,"bold"),width=11,bd=2,padx=8,
       pady=8,bg ="Cadet Blue",fg="White",command=iGraph).grid(row=9,column=0)
    
Button(DataFrame2, text ="Exit",font=("Arial",12,"bold"),width=11,bd=2,padx=8,
       pady=8,bg ="Cadet Blue",fg="White",command=iExit).grid(row=9,column=1)
    




root.mainloop()
