import tkinter 
from tkinter import * 
import time
obj=tkinter.Tk()
obj.title("Graphical Interface")
obj.geometry('2000x1000')
label=Label(obj,bg='lightgreen',fg='teal',text="Resturant Management System",font=("Arial Bold",30))
label.grid(column=10,row=1,padx=20,pady=20,sticky=N)
p=time.strftime('%a  %d-%m-%Y   %H:%M:%S')
label=Label(obj,text=p)
label.grid()
label.grid(column=10,row=2)
abc=[]
t=0
gst=0
t1=0
s=0
options=[1,2,3,4,5,6,7,8,9,10]
op1=[1,2,3,4,5,6]
op2=[1,2,3,4,5,6,7,8]
op3=[1,2,3,4,5,6,7,8,9]
op4=[1,2,3,4,5]
op5=[1,2,3,4,5]
cost=[200,150,100,160,250,300]
val=["Total cost::","Service tax::","G.S.T::","Total Payable Amount::"]
items=["BIG MEAL[price=RS.200]","BIG LUNCH[price=RS.150]","ITALIAN PASTA[price=RS.100]","CHINESE BIG BOWL[price=RS.160]","SUGAR CRUSH[price=RS.250]","CLASSICL THALI[price=RS.300]"]
variable=IntVar(obj)
v1=IntVar(obj)
v2=IntVar(obj)
v3=IntVar(obj)
v4=IntVar(obj)
v5=IntVar(obj)
flag=1
label=Label(obj,text="order no.")
label.grid(column=6,row=9)
label=Label(obj,text=flag)
label.grid(column=7,row=9)
e1=StringVar(obj)
e2=StringVar(obj)
e3=StringVar(obj)
e4=StringVar(obj)
for i in range(0,6):
    label=Label(obj,text=items[i])
    label.grid(column=9,row=10+i,padx=30,sticky=W)
    if i==0:
        w=OptionMenu(obj,variable,*options)
        w.grid(column=10,row=10+i,padx=30,pady=10,sticky=W)
    if i==1:    
        w=OptionMenu(obj,v1,*op1)
        w.grid(column=10,row=10+i,padx=30,pady=10,sticky=W)
    if i==2:
        w=OptionMenu(obj,v2,*op2)
        w.grid(column=10,row=10+i,padx=30,pady=10,sticky=W)
    if i==3:
        w=OptionMenu(obj,v3,*op3)
        w.grid(column=10,row=10+i,padx=30,pady=10,sticky=W)
    if i==4:
        w=OptionMenu(obj,v4,*op4)
        w.grid(column=10,row=10+i,padx=30,pady=10,sticky=W)
    if i==5:
        w=OptionMenu(obj,v5,*op5)
        w.grid(column=10,row=10+i,padx=30,pady=10,sticky=W)  
for i in range(0,4):
    label=Label(obj,text=val[i])
    label.grid(column=10,row=10+i,pady=10)     
    if i==0:
        e11=Entry(obj,textvariable=e1)
        e11.grid(row=10+i,column=11)
    if i==1:
        e22=Entry(obj,textvariable=e2)
        e22.grid(row=10+i,column=11)
    if i==2:
        e33=Entry(obj,textvariable=e3)
        e33.grid(row=10+i,column=11)
    if i==3:
        e44=Entry(obj,textvariable=e4)
        e44.grid(row=10+i,column=11)        

def submit():
    flag=1
    flag+=1
    label=Label(obj,text=flag)
    label.grid(column=7,row=9)
    for i in range(0,6):
        if i==0:
            abc.append(variable.get())
        if i==1:
            abc.append(v1.get())
        if i==2:
            abc.append(v2.get())
        if i==3:
            abc.append(v3.get())
        if i==4:
            abc.append(v4.get())
        if i==5:
            abc.append(v5.get())
           
def total():
    submit()
    t=0
    for j in range(0,4):
        if j==0:
            for i in range(0,6):
                t= t +(abc[i]*cost[i])
                e1.set(str(t))

        if j==1:
            gst=(0.05*t)
            e2.set(str(gst))


        if j==2:
            s=(0.04*t)
            e3.set(str(s))

        if j==3:
            t1=gst+s+t
            e4.set(str(t1))

def reset():
    t=0
    gst=0
    t1=0
    s=0
    for i in range(0,6):
        if i==0:
            variable.set(0)
        if i==1:
            v1.set(0)
        if i==2:
            v2.set(0)
        if i==3:
            v3.set(0)
        if i==4:
            v4.set(0)
        if i==5:
            v5.set(0)
    for i in range(0,4):
        if i==0:
            e11=Entry(obj,textvariable="")
            e11.grid(row=10+i,column=11)
        if i==1:
            e22=Entry(obj,textvariable="")
            e22.grid(row=10+i,column=11)
        if i==2:
            e33=Entry(obj,textvariable="")
            e33.grid(row=10+i,column=11)
        if i==3:
            e44=Entry(obj,textvariable="")
            e44.grid(row=10+i,column=11)

button=Button(obj,text="Submit",command=submit)
button.grid(column=10,row=14)
button=Button(obj,text="Reset",command=reset)
button.grid(column=10,row=15)
button=Button(obj,text="Total",command=total)
button.grid(column=11,row=15)
button=Button(obj,text="Exit",command=exit)
button.grid(column=12,row=15)
obj.mainloop()
