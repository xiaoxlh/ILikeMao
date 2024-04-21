import time
import requests as r
import tkinter
from tkinter import StringVar, ttk
import sv_ttk # type: ignore
import pyperclip as pc
import tkinter.messagebox
import pandas as pd # type: ignore
import ctypes
from tkinter import filedialog

def do1(can):
        session = r.Session()
        i = 0
        uumm = pd.read_excel(select_path,usecols="B:C")
        uul = uumm['账号'].tolist()
        mml = uumm['初始密码'].tolist()
        print(uul,mml)
        for i in range(int(time_box.get())):
            login_data = {'pid': '65edCTyg',
                'identity': uul[i],
                'password': mml[i]}
            session.post('https://api.codemao.cn/tiger/v3/web/accounts/login', json=login_data)
            print(str(session.post("https://api.codemao.cn/nemo/v2/works/" + nw.get() +"/" + can)))
            session.post('https://api.codemao.cn/tiger/v3/web/accounts/loginout', json=login_data)
            time.sleep(1)
            i = i + 1
            out.configure(text=str(i)+'/'+str(time_box.get()))
            out.configure(text='任务已完成，快去查看吧！')
def follow():
        session = r.Session()
        i = 0
        uumm = pd.read_excel(select_path,usecols="B:C")
        uul = uumm['账号'].tolist()
        mml = uumm['初始密码'].tolist()
        print(uul,mml)
        for i in range(int(time_box.get())):
            login_data = {'pid': '65edCTyg',
                'identity': uul[i],
                'password': mml[i]}
            session.post('https://api.codemao.cn/tiger/v3/web/accounts/login', json=login_data)
            print(str(session.post("https://api.codemao.cn/nemo/v2/user/" + nw.get() +"/follow")))
            session.post('https://api.codemao.cn/tiger/v3/web/accounts/loginout', json=login_data)
            time.sleep(1)
            i = i + 1
            out.configure(text=str(i)+'/'+str(time_box.get()))
        out.configure(text='任务已完成，快去查看吧！')
def watch():
        for i in range(int(time_box.get())):
            print(str(r.get("https://shequ.codemao.cn/work/"+ nw.get())))
            time.sleep(1)
            i = i + 1
            out.configure(text=str(i)+'/'+str(time_box.get()))
        out.configure(text='任务已完成，快去查看吧！')
def do():
    if can_box.get() == '点赞':
        do1('like')
    elif can_box.get() == '收藏':
        do1('collection')
    elif can_box.get() == '浏览量':
        watch
    elif can_box.get() == '关注':
        follow
    elif can_box.get() == '再创作':
        do1('fork')
def sun():
            if sv_ttk.get_theme() == "dark":
                sv_ttk.use_light_theme()
                sun_button.config(text="🌙") 

            elif sv_ttk.get_theme() == "light":
                sv_ttk.use_dark_theme()
                sun_button.config(text="☀")       
def select_file():
    select_path = StringVar()
    selected_file_path = filedialog.askopenfilename()  # 使用askopenfilename函数选择单个文件
    select_path.set(selected_file_path)
    return select_path    

root = tkinter.Tk()
select_path = r"D:\xiaox\Desktop\Dev\Python\ILikeMao\uumm.xlsx"

ctypes.windll.shcore.SetProcessDpiAwareness(1)
ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
root.tk.call('tk', 'scaling', ScaleFactor/75)
    
root.title("ILikeMao")
root.geometry('500x300+300+200')
root.iconbitmap(r"D:\xiaox\Desktop\Dev\Python\ILikeMao\ilikemao.ico")
root.minsize(700,600)	
root.maxsize(1000,800)	

sun_button = ttk.Button(root,text="☀", command=sun,style="my.TButton")
sun_button.pack(anchor="ne",pady=5,padx=5)

tip0 = ttk.Label(root,text="选择账密文件",font=('微软雅黑',15,'bold'))
tip0.pack(anchor="w",pady=7,padx=15)
file_button = ttk.Button(root,text="+", command=select_file,style="my.TButton")
file_button.pack(anchor="w",pady=7,padx=15)

tip4 = ttk.Label(root,text="功能",font=('微软雅黑',15,'bold'))
tip4.pack(anchor="w",pady=7,padx=15)
can_box = ttk.Combobox(root, value=('点赞', '收藏', '浏览量','关注','再创作'))
can_box.pack(anchor="w",pady=7,padx=15)

tip1 = ttk.Label(root,text="次数",font=('微软雅黑',15,'bold'))
tip1.pack(anchor="w",pady=7,padx=15)
time_box = ttk.Combobox(root, value=('10', '25', '50'))
time_box.pack(anchor="w",pady=7,padx=15)

tip2 = ttk.Label(root,text="输入要操作的作品或账号Id",font=('微软雅黑',15,'bold'))
tip2.pack(anchor="w",pady=7,padx=15)
nw = ttk.Entry(root,width=60)
nw.pack(anchor="w",pady=7,padx=15)
grass_start_button = ttk.Button(root,text="开始操作", command=do, width=30)
grass_start_button.pack(anchor="w",pady=7,padx=15)
    
tip3 = ttk.Label(root,text="输出",font=('微软雅黑',15,'bold'))
tip3.pack(anchor="w",pady=7,padx=15)
out = ttk.Label(root,text="",font=('微软雅黑',12,'bold'))
out.pack(anchor="w",pady=7,padx=15)

def about():
        tkinter.messagebox.showinfo(title='关于',message='©2024 Xiaoxiao 版本0.0.1-alpha\n本版本为发行预览版\n开源版本可在Github处下载\n官网：https://xiao.asia\nGithub仓库：https://github.com/xiaolovesmall/ILikeMao')
i_button = ttk.Button(root,text="关于", command=about,style="my.TButton")
i_button.pack(anchor="se",pady=7,padx=7)

sv_ttk.use_light_theme()
    
root.mainloop()