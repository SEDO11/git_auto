# GUI 반 자동 git 관리 프로그램

from math import *
from tkinter import *
from tkinter import scrolledtext
from datetime import datetime
import os

placeholder_text = "push 할 위치를 입력하세요"

class Cont1:
    def __init__(self, frame):
        self.inframe = Frame(frame)
        self.inframe.pack(fill=X, anchor=N)
        
        self.edt1 = Entry(self.inframe, width=70)
        self.edt1.insert(0, placeholder_text)
        self.edt1.pack(side=RIGHT, padx=5, pady=10)
        
        self.btn1 = Button(self.inframe, text='실행', command=start)
        self.btn1.pack(side=RIGHT, padx=5, pady=10)

def start():
    global txt
    
    time = datetime.now()
    time = str(time.date()).replace('-', '')
    
    git_code = ['git pull', 'git add *', 'git add -A', f'git commit -m "{time}"', 'git push']
    
    result = ''
    url = con1.edt1.get()
    os.chdir(url) # 디렉토리 위치 변경
    path = os.getcwd() # 현재 디렉토리 위치 저장
    
    # print('path: ', path)
    # print('url: ', url)
    
    result += "디렉토리: " + str(path) + "\n\n"
    
    for git in git_code:
        path = os.popen(git).read()
        result += str(path) + "\n\n"
    
    txt.insert(END, result)
    txt.configure(state='disabled')

root = Tk()
root.geometry('600x400')
root.title('반자동 git push')
root.resizable(False, False)

edtFrame = Frame(root)
edtFrame.pack()

con1 = Cont1(edtFrame)

txt = scrolledtext.ScrolledText(edtFrame)
txt.pack(side = BOTTOM, fill=BOTH, expand=1)

root.mainloop()