from tkinter import *
import hashlib

s256=hashlib.sha1()
qs256=hashlib.sha1()
def login():
    idData=entryID.get()
    pwdata=entryPW.get()
    if len(idData)>0 and len(pwdata)>0:
        s256.update(pwdata.encode("utf-8"))
        pwhash=s256.hexdigest()
        qs256.update(idData.encode("utf-8"))
        idd=qs256.hexdigest()
        print(idd)
        print(pwhash)
        if idd=='1161e6ffd3637b302a5cd74076283a7bd1fc20d3' and pwhash=='f4542db9ba30f7958ae42c113dd87ad21fb2eddb':
            root.deiconify()
            top.destroy()
        else:
            entryID.delete(0,'end')
            entryPW.delete(0,'end')
            print('帳密錯誤')
    else:
        entryID.delete(0,'end')
        entryPW.delete(0,'end')
        print('請輸入帳密')
        

    

def exitProgram():
    top.destroy()
    root.destroy()

root=Tk()
root.geometry("400x300+200+100")
top=Toplevel(root)
labID=Label(top,text='ID',anchor=E,justify=RIGHT,font=20,bg='#ffff00')
labPW=Label(top,text='Password',anchor=E,justify=RIGHT,font=20)
entryID=Entry(top)
entryPW=Entry(top,show='*')
btnLogin=Button(top,text='login',command=login,font=20)
btnExit=Button(top,text='Exit',command=exitProgram,font=20,bg='red')
labID.grid(row=0,column=0,sticky=NSEW)
entryID.grid(row=0,column=1,sticky=NSEW)
labPW.grid(row=1,column=0,sticky=NSEW)
entryPW.grid(row=1,column=1,sticky=NSEW)
btnLogin.grid(row=2,column=0,sticky=NSEW)
btnExit.grid(row=2,column=1,sticky=NSEW)
flag=True
def setest(n):
    global flag
    if n==0:
        if flag:
            q0.config(text='0',font=20,bg='#ffff00')
        else:
            q0.config(text='X',font=20,bg='#ffff00')
        q0.config(state=DISABLED)
    elif n==1:
        if flag:
            q1.config(text='0',font=20,bg='#ffff00')
        else:
            q1.config(text='X',font=20,bg='#ffff00')
        q1.config(state=DISABLED)
    elif n==2:
        if flag:
            q2.config(text='0',font=20,bg='#ffff00')
        else:
            q2.config(text='X',font=20,bg='#ffff00') 
        q2.config(state=DISABLED)
    elif n==3:
        if flag:
            q3.config(text='0',font=20,bg='#ffff00')
        else:
            q3.config(text='X',font=20,bg='#ffff00')
        q3.config(state=DISABLED)
    elif n==4:
        if flag:
            q4.config(text='0',font=20,bg='#ffff00')
        else:
            q4.config(text='X',font=20,bg='#ffff00')
        q4.config(state=DISABLED)
    elif n==5:
        if flag:
            q5.config(text='0',font=20,bg='#ffff00')
        else:
            q5.config(text='X',font=20,bg='#ffff00')
        q5.config(state=DISABLED)
    elif n==6:
        if flag:
            q6.config(text='0',font=20,bg='#ffff00')
        else:
            q6.config(text='X',font=20,bg='#ffff00')
        q6.config(state=DISABLED)
    elif n==7:
        if flag:
            q7.config(text='0',font=20,bg='#ffff00')
        else:
            q7.config(text='X') 
        q7.config(state=DISABLED)
    elif n==8:
        if flag:
            q8.config(text='0',font=20,bg='#ffff00')
        else:
            q8.config(text='X',font=20,bg='#ffff00')
        q8.config(state=DISABLED)
    flag=not flag 
    if q0.cget('text')==q1.cget('text')and q0.cget('text')==q2.cget('text') and q0.cget('text') !='':
        if q0.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q3.cget('text')==q4.cget('text')and q3.cget('text')==q5.cget('text') and q3.cget('text') !='':
        if q3.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q6.cget('text')==q7.cget('text')and q6.cget('text')==q8.cget('text') and q6.cget('text') !='':
        if q6.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q0.cget('text')==q3.cget('text')and q0.cget('text')==q6.cget('text') and q0.cget('text') !='':
        if q0.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q1.cget('text')==q4.cget('text')and q1.cget('text')==q7.cget('text') and q1.cget('text') !='':
        if q1.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q2.cget('text')==q5.cget('text')and q2.cget('text')==q8.cget('text') and q2.cget('text') !='':
        if q2.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q0.cget('text')==q4.cget('text')and q0.cget('text')==q8.cget('text') and q0.cget('text') !='':
        if q0.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')
    if q2.cget('text')==q4.cget('text')and q2.cget('text')==q6.cget('text') and q2.cget('text') !='':
        if q2.cget('text')=='0':
            print('p1 win')
        else:
            print('p2 win')





root.geometry("400x400+200+100")
root.title="Button test"




root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)

q0 = Button(root, text="1",command=lambda:setest(0))
q0.grid(row=0, column=0, sticky=NSEW)
q1 = Button(root, text="2",command=lambda:setest(1))
q1.grid(row=0, column=1, sticky=NSEW)
q2 = Button(root, text="3",command=lambda:setest(2))
q2.grid(row=0, column=2, sticky=NSEW)
q3 = Button(root, text="4",command=lambda:setest(3))
q3.grid(row=1, column=0, sticky=NSEW)
q4 = Button(root, text="5",command=lambda:setest(4))
q4.grid(row=1, column=1, sticky=NSEW)
q5 = Button(root, text="6",command=lambda:setest(5))
q5.grid(row=1, column=2, sticky=NSEW)
q6 = Button(root, text="7",command=lambda:setest(6))
q6.grid(row=2, column=0, sticky=NSEW)
q7 = Button(root, text="8",command=lambda:setest(7))
q7.grid(row=2, column=1, sticky=NSEW)
q8 = Button(root, text="9",command=lambda:setest(8))
q8.grid(row=2, column=2, sticky=NSEW)





root.withdraw()
root.mainloop()