import re
import tkinter as t
from tkinter import messagebox
from PIL import ImageTk,Image


window = t.Tk()

window.title("登录")
window.geometry('300x200')
window.configure(bg = 'LavenderBlush')


l1 = t.Label(text = "姓名",bg = 'ghostwhite')
l1.place(x = 50,y = 50)
userval = t.StringVar()
e1 = t.Entry(window,textvariable = userval,bg = 'white')
e1.place(x = 85,y = 50)

l2 = t.Label(text = "密码",bg = 'ghostwhite')
l2.place(x = 50,y = 90)
passwordval = t.StringVar()
e2 = t.Entry(window,textvariable = passwordval,show = '*',bg = 'white')
e2.place(x = 85,y = 90)

def newtop():
    window.destroy()
    new = t.Tk()
    new.title("学生管理系统")
    new.geometry('300x300')
    new.configure(bg="cornsilk")

    '''val = t.StringVar()
    norval = t.StringVar()
    aval = t.StringVar()
    sval = t.StringVar()
    dval = t.StringVar()
    scval = t.StringVar()

    l = t.Label(new,text='姓名',textvariable = nval,bg = 'lightyellow')
    l.place(x=50, y=30)
    e1 = t.Entry(new)
    e1.place(x=85, y=30)


    l = t.Label(new,text = '学号',textvariable = norval,bg = 'lightyellow')
    l.place(x = 50,y = 70)
    e2 = t.Entry(new)
    e2.place(x = 85,y = 70)

    l = t.Label(new, text='年龄',textvariable = aval,bg = 'lightyellow')
    l.place(x =50,y=110)
    e3 = t.Entry(new)
    e3.place(x = 85,y=110)

    l = t.Label(new, text='性别',textvariable = sval,bg = 'lightyellow')
    l.place(x = 50,y = 150)
    e4 = t.Entry(new)
    e4.place(x= 85, y = 150)

    l = t.Label(new, text='专业',textvariable = dval,bg = 'lightyellow')
    l.place(x =50, y=190)
    e5 = t.Entry(new)
    e5.place(x=85, y=190)

    l = t.Label(new, text='学院',textvariable = scval,bg = 'lightyellow')
    l.place(x=50, y=230)
    e6 = t.Entry(new)
    e6.place(x=85, y=230)'''



    def save():

        news = t.Tk()
        news.geometry('300x300')

        nval = t.StringVar()
        norval = t.StringVar()
        aval = t.StringVar()
        sval = t.StringVar()
        dval = t.StringVar()

        l = t.Label(news, text='姓名', bg='lightyellow')
        l.place(x=30, y=30)
        e1 = t.Entry(news,textvariable = nval)
        e1.place(x=85, y=30)


        l = t.Label(news, text='学号', bg='lightyellow')
        l.place(x=30, y=70)
        e2 = t.Entry(news,textvariable = norval)
        e2.place(x=85, y=70)

        l = t.Label(news, text='英语' , bg='lightyellow')
        l.place(x=30, y=110)
        e3 = t.Entry(news,textvariable = aval)
        e3.place(x=85, y=110)

        l = t.Label(news, text='C语言',bg='lightyellow')
        l.place(x=30, y=150)
        e4 = t.Entry(news,textvariable = sval )
        e4.place(x=85, y=150)

        l = t.Label(news, text='python', bg='lightyellow')
        l.place(x=30, y=190)
        e5 = t.Entry(news, textvariable = dval)
        e5.place(x=85, y=190)
        def saven():
            filename = "information.txt"

            with open (filename,'a') as f:
                if e1.get()!= None and e2.get()!= None and e3.get()!= None and e4.get()!= None and e5.get()!= None :
                    f.write(e1.get()+',')
                    f.write(e2.get()+',')
                    f.write(e3.get()+',')
                    f.write(e4.get()+',')
                    f.write(e5.get()+'\n')
                    f.close()
                    t.messagebox.showinfo(title='保存提示', message="保存成功")
                    clearn()
                else:
                    t.messagebox.showinfo(title='保存提示', message="保存失败 请确保信息正确完整")
                    clearn()

        newsb = t.Button(news,text = "保存", height =1,width =5,command = saven)
        newsb.place(x = 150,y=230)




    def search():

        news = t.Tk()
        news.geometry('300x300')

        nval = t.StringVar()
        norval = t.StringVar()
        aval = t.StringVar()
        sval = t.StringVar()
        dval = t.StringVar()

        l = t.Label(news, text='姓名', bg='lightyellow')
        l.place(x=30, y=30)
        e1 = t.Entry(news, textvariable=nval)
        e1.place(x=85, y=30)

        l = t.Label(news, text='学号', bg='lightyellow')
        l.place(x=30, y=70)
        e2 = t.Entry(news, textvariable=norval)
        e2.place(x=85, y=70)

        l = t.Label(news, text='英语', bg='lightyellow')
        l.place(x=30, y=110)
        e3 = t.Entry(news, textvariable=aval)
        e3.place(x=85, y=110)

        l = t.Label(news, text='C语言', bg='lightyellow')
        l.place(x=30, y=150)
        e4 = t.Entry(news, textvariable=sval)
        e4.place(x=85, y=150)

        l = t.Label(news, text='python', bg='lightyellow')
        l.place(x=30, y=190)
        e5 = t.Entry(news, textvariable=dval)
        e5.place(x=85, y=190)
        filename = 'information.txt'
        def searchn():
            with open(filename, 'r') as f:
                list = []
                for i in f.readlines():
                    list.append(i.strip('\n').split(','))
                f.close()
                name = e1.get()
                for i in range(len(list)):
                    if name == list[i][0]:
                        e2.insert('0',list[i][1])
                        e3.insert('0',list[i][2])
                        e4.insert('0',list[i][3])
                        e5.insert('0',list[i][4])

        newsb = t.Button(news, text="查询", height=1, width=5, command=searchn)
        newsb.place(x=150, y=230)

    def update():
        pass

    def clearn():
        pass

    def line():
        pass

    def summerize():
        news = t.Tk()
        news.geometry('300x300')

        nval = t.StringVar()
        norval = t.StringVar()
        aval = t.StringVar()
        sval = t.StringVar()
        dval = t.StringVar()

        l = t.Label(news, text='姓名', bg='lightyellow')
        l.place(x=30, y=30)
        e1 = t.Entry(news, textvariable=nval)
        e1.place(x=85, y=30)

        l = t.Label(news, text='学号', bg='lightyellow')
        l.place(x=30, y=70)
        e2 = t.Entry(news, textvariable=norval)
        e2.place(x=85, y=70)

        l = t.Label(news, text='综合成绩', bg='lightyellow')
        l.place(x=30, y=110)
        e3 = t.Entry(news, textvariable=aval)
        e3.place(x=85, y=110)

        filename = 'information.txt'

        def searchn():
            with open(filename, 'r') as f:
                list = []
                for i in f.readlines():
                    list.append(i.strip('\n').split(','))
                f.close()
                name = e1.get()
                for i in range(len(list)):
                    if name == list[i][0]:
                        A = int(list[i][2])
                        B = int(list[i][3])
                        C = int(list[i][4])
                        D = (A+B+C)/3
                        e2.insert('0', list[i][1])
                        e3.insert('0', str(D))


        newsb = t.Button(news, text="查询", height=1, width=5, command=searchn)
        newsb.place(x=150, y=230)


    b3 = t.Button(new,text = "录入学生信息",height =1,width =10,command = save)
    b3.place(x= 110,y= 30)

    b5 = t.Button(new, text="查找学生信息", height=1, width=10,command = search)
    b5.place(x= 110, y= 70)

    b4 = t.Button(new, text= "删除学生信息", height=1, width=10,command = clearn)
    b4.place(x= 110, y= 110)

    b6 = t.Button(new, text="修改学生信息", height=1, width=10, command=update)
    b6.place(x= 110, y= 150)

    b7 = t.Button(new, text="排序", height=1, width=10, command=line)
    b7.place(x= 110, y=190)

    b8 = t.Button(new, text="统计学生信息", height=1, width=10, command=summerize)
    b8.place(x= 110, y=230)
    


def login():
    a = e1.get()
    b = e2.get()
    if a == "1" and b == "1":
        t.messagebox.showinfo(title = '登陆提示',message = "登陆成功")
        newtop()

    else:
        t.messagebox.showinfo(title = '登陆提示',message = "密码或用户名错误")
        clearw()

def clearw():
    e1.delete('0', len(list(e1.get())))
    e2.delete('0', len(list(e2.get())))




b1 = t.Button(window,text = "登录",height =1,width =5,command = login,bg = 'azure')
b1.place(x = 90,y = 120)
b2 = t.Button(window,text = "清空",height =1,width =5,command = clearw,bg = 'azure')
b2.place(x = 180,y = 120)
window.mainloop()
