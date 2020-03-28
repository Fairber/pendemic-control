


import wx
import pymysql
import Demo
import Demo_add
import Demo_delete
import Demo_login
import Demo_show
import Demo_update
import Demo_error
import Demo_success
import sys
sys.path

conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="usbw",database="school")
cursor=conn.cursor()

user_name="root"
password="123"

create_table='''create table  if not exists score
( number varchar(20) not null,
name varchar(20)  null,
computer double  null,
math double  null,
english double  null,
password varchar(20) null,
primary key(number));'''

#创建成绩表
def createtable(sql):
    try:
        cursor.execute(sql)
        conn.commit()
        print("建表成功")
    except Exception as e:
        print("表已存在")
#添加成绩信息
def add(list):
    sql="insert into score values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql,list)
    conn.commit()
#查找相应学号信息
def search(id):
    sql="select * from score where number = %s"
    cursor.execute(sql,[id])
    results = cursor.fetchall()
    return results
#更改相应学号信息
def update(list):
    sql="update score set computer=%s,math=%s,english=%s where number = %s"
    cursor.execute(sql,list)
    conn.commit()
#删除相应学号的数据
def delete(id):
    sql="delete from score where number =%s"
    cursor.execute(sql,[id])
    conn.commit()

#登录界面
class Myframe(Demo_login.MyFrame1):
    def __init__(self, parent):
        Demo_login.MyFrame1.__init__(self, parent)

    def login(self, event):
        try:
            name=self.m_textCtrl1.GetValue()
            pw=self.m_textCtrl2.GetValue()
            pword = search(name)
            if user_name ==name and password ==pw:
                app = wx.App(False)
                frame = Myframe2(None)
                frame.Show(True)
                app.MainLoop()
            elif pword[0][5] == pw:
                app = wx.App(False)
                frame = Myframe6(None)
                frame.Show(True)
                app.MainLoop()
            else:
                app = wx.App(False)
                frame = MyDialog(None)
                frame.Show(True)
                app.MainLoop()

        except:
            app = wx.App(False)
            frame = MyDialog(None)
            frame.Show(True)
            app.MainLoop()

    def register(self, event):
        exit(0)

#添加信息界面
class Myframe3(Demo_add.MyFrame3):
    def __init__(self,parent):
        Demo_add.MyFrame3.__init__(self,parent)

    def add1(self, event):
        try:
            id = self.m_textCtrl3.GetValue()
            name=self.m_textCtrl4.GetValue()
            computer=self.m_textCtrl5.GetValue()
            math=self.m_textCtrl6.GetValue()
            english=self.m_textCtrl7.GetValue()
            pw=self.m_textCtrl8.GetValue()
            list=[id,name,computer,math,english,pw]
            add(list)
            app = wx.App(False)
            frame = MyDialog1(None)
            frame.Show(True)
            app.MainLoop()
        except:
            app = wx.App(False)
            frame = MyDialog(None)
            frame.Show(True)
            app.MainLoop()

#主界面
class  Myframe2(Demo.MyFrame2):
    def __init__(self,parent):
        Demo.MyFrame2.__init__(self,parent)

    def add(self, event):
        app = wx.App(False)
        frame = Myframe3(None)
        frame.Show(True)
        app.MainLoop()

    def delete(self, event):
        app = wx.App(False)
        frame = Myframe4(None)
        frame.Show(True)
        app.MainLoop()

    def update(self, event):
        app = wx.App(False)
        frame = Myframe5(None)
        frame.Show(True)
        app.MainLoop()

    def select(self, event):
        app = wx.App(False)
        frame = Myframe6(None)
        frame.Show(True)
        app.MainLoop()

    def exit(self,event):
        exit(0)
#删除界面
class Myframe4(Demo_delete.MyFrame4):
    def __init__(self,parent):
        Demo_delete.MyFrame4.__init__(self,parent)

    def delete1(self, event):
        try:
            id=self.m_textCtrl8.GetValue()
            delete(id)
            app = wx.App(False)
            frame = MyDialog1(None)
            frame.Show(True)
            app.MainLoop()
        except:
            app = wx.App(False)
            frame = MyDialog(None)
            frame.Show(True)
            app.MainLoop()

#修改信息界面
class Myframe5(Demo_update.MyFrame5):
    def __init__(self,parent):
        Demo_update.MyFrame5.__init__(self,parent)

    def update1(self, event):
        try:
            id = self.m_textCtrl9.GetValue()
            computer =self.m_textCtrl11.GetValue()
            math = self.m_textCtrl12.GetValue()
            english=self.m_textCtrl13.GetValue()
            list=[computer,math,english,id]
            update(list)
            app = wx.App(False)
            frame = MyDialog1(None)
            frame.Show(True)
            app.MainLoop()
        except:
            app = wx.App(False)
            frame = MyDialog(None)
            frame.Show(True)
            app.MainLoop()

#查询信息界面
class Myframe6(Demo_show.MyFrame6):
    def __init__(self,parent):
        Demo_show.MyFrame6.__init__(self,parent)

    def select1(self, event):
        id = self.m_textCtrl14.GetValue()
        try:
            list = search(id)

            self.m_textCtrl15.SetValue(str(list[0][1]))
            self.m_textCtrl16.SetValue(str(list[0][2]))
            self.m_textCtrl17.SetValue(str(list[0][3]))
            self.m_textCtrl18.SetValue(str(list[0][4]))
        except:
            app = wx.App(False)
            frame = MyDialog(None)
            frame.Show(True)
            app.MainLoop()

#错误处理
class MyDialog(Demo_error.MyDialog2):
    def __init__(self,parent):
        Demo_error.MyDialog2.__init__(self,parent)

    def exit(self, event):
        self.Close(True)

#成功提示
class MyDialog1(Demo_success.MyDialog2):
    def __init__(self,parent):
        Demo_success.MyDialog2.__init__(self,parent)

    def exit(self, event):
        self.Close(True)


#主函数
def main():
    createtable(create_table)

    app = wx.App(False)
    frame = Myframe(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()