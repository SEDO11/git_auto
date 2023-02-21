from math import *
from tkinter import *
from tkinter import filedialog, messagebox, scrolledtext
from datetime import datetime
import os
import csv


class GitManager:
    def __init__(self, root):
        self.root = root

        # 입력창과 실행 버튼을 포함하는 프레임 생성
        self.edt_frame = Frame(self.root)
        self.edt_frame.pack(fill=X, anchor=N)

        self.edt_path = Entry(self.edt_frame, width=70)
        self.edt_path.insert(0, "push 할 위치를 입력하세요")
        self.edt_path.pack(side=RIGHT, padx=5, pady=10)

        self.btn_run = Button(self.edt_frame, text="실행", command=self.start)
        self.btn_run.pack(side=RIGHT, padx=5, pady=10)

        # 실행 결과를 표시하는 ScrolledText 위젯 생성
        self.txt_result = scrolledtext.ScrolledText(self.root)
        self.txt_result.pack(side=BOTTOM, fill=BOTH, expand=1)

    def start(self):
        # 실행 결과를 저장할 CSV 파일 생성
        csv_file = open("git_push_result.csv", mode="w", newline="")
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Command", "Result"])

        # Git 저장소 위치 변경
        url = self.edt_path.get()
        os.chdir(url)

        # 실행 결과 저장
        commands = [
            "git pull",
            "git add .",
            f'git commit -m "{datetime.now().date().strftime("%Y%m%d")}"',
            "git push",
        ]
        for cmd in commands:
            result = os.popen(cmd).read()
            csv_writer.writerow([cmd, result])

        # 실행 결과를 ScrolledText 위젯에 출력
        self.txt_result.delete("1.0", END)
        with open("git_push_result.csv") as f:
            reader = csv.reader(f)
            next(reader)  # 헤더 제외
            for row in reader:
                cmd, result = row
                self.txt_result.insert(END, f"{cmd}\n")
                self.txt_result.insert(END, f"{result}\n\n")
        self.txt_result.configure(state="disabled")

        # 실행 결과를 메시지 박스로 알림
        messagebox.showinfo(title="완료", message="Git push가 완료되었습니다.")

if __name__ == "__main__":
    root = Tk()
    root.geometry("600x400")
    root.title("반자동 git push")
    root.resizable(False, False)

    GitManager(root)

    root.mainloop()