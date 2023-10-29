import time
import datetime
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import keyboard

KEY = "1234"
EXPIRE_Y = 2023
EXPIRE_M = 11
EXE = True
INTERVAL = 0.2

root = Tk()
root.title("B Macro")
root.geometry("640x400")

def create_new_file():
    msgbox.showinfo("Information", "Not Available")

def about_menu():
    msgbox.showinfo("Information", "B Macro v0.A\nContact : fkdltldls@naver.com")

def about_expire():
    msgbox.showinfo("About Expire", "만료일\n{}년 {}월 까지".format(EXPIRE_Y, EXPIRE_M))

def exe_check():
    current_datetime = datetime.datetime.now()
    if (current_datetime.year <= EXPIRE_Y) & (current_datetime.month <= EXPIRE_M):
        if KEY == keycode.get():
            if "1" in combobox_num.get() or "2" in combobox_num.get():
                kakao_macro()
            else:
                msgbox.showerror("Error", "보낼 개수가 선택되지 않았습니다.")
        else:
            label5.config(text="키 코드가 일치하지 않아 실행되지 않습니다.")
    else:
        label5.config(text="사용 기간이 만료되어 실행되지 않습니다.")

def exe_cancel():
    label5.config(text="중지되었습니다.")
    EXE = False

def kakao_macro():
    label5.config(text="5초 후 실행 됩니다.")
    root.update()
    time.sleep(1)
    label5.config(text="4초 후 실행 됩니다.")
    root.update()
    time.sleep(1)
    label5.config(text="3초 후 실행 됩니다.")
    root.update()
    time.sleep(1)
    label5.config(text="2초 후 실행 됩니다.")
    root.update()
    time.sleep(1)
    label5.config(text="1초 후 실행 됩니다.")
    root.update()
    time.sleep(1)
    label5.config(text="☆ 실행 중입니다 ☆")
    root.update()
    for i in range(int(combobox_exe.get())):
        time.sleep(INTERVAL)
        keyboard.press_and_release('Enter')
        time.sleep(INTERVAL)
        keyboard.press_and_release('win+v')
        time.sleep(INTERVAL)
        keyboard.press_and_release('Enter')
        time.sleep(INTERVAL)
        keyboard.press_and_release('Enter')
        time.sleep(INTERVAL)
        keyboard.press_and_release('Enter')
        if "2" in combobox_num.get():
            time.sleep(INTERVAL)
            keyboard.press_and_release('win+v')
            time.sleep(INTERVAL)
            keyboard.press_and_release('down')
            time.sleep(INTERVAL)
            keyboard.press_and_release('Enter')
            time.sleep(INTERVAL)
            keyboard.press_and_release('Enter')
            time.sleep(INTERVAL)
            keyboard.press_and_release('Enter')
        time.sleep(INTERVAL)
        keyboard.press_and_release('ESC')
        time.sleep(INTERVAL)
        keyboard.press_and_release('down')
    label5.config(text="완료하였습니다.")


key_frame = LabelFrame(root, text="키 코드")
key_frame.pack(side="top", anchor="center", fill="both", expand=True, padx=5, pady=5)

msg_frame = LabelFrame(root, text="보낼 메세지와 사진 세팅")
msg_frame.pack(side="top", anchor="center", fill="both", expand=True, padx=5, pady=5)

exe_frame = LabelFrame(root, text="실행")
exe_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

keycode = Entry(key_frame, width=50)
keycode.pack()
keycode.insert(END, "1234")

txt1 = Label(msg_frame, text="\"Window키 + v\"를 누르면 나오는 클립보드의 내용을 순서대로 전송합니다.\n클립보드 내에 몇 가지 항목을 보낼지 선택하시고 클립보드를 세팅해주세요.\n예시1 : 메세지 또는 사진만 \"Ctrl+c\"하고 1을 선택\n예시2 : 메세지와 사진을 순서대로 각각 \"Ctrl+c\"하고 2를 선택\n메세지와 사진은 모두 PC카카오에서 복사해주세요.\n잘 복사되었는지 \"Window키 + v\"를 눌러서 확인해주세요.")
txt1.pack()
num_of_send = ["1개 항목만 보내기", "2개 항목 보내기"]
combobox_num = ttk.Combobox(msg_frame, height=2, values=num_of_send, state="readonly")
combobox_num.pack()
combobox_num.set("보낼 개수를 선택해주세요")

label4 = Label(exe_frame, text="반복 횟수(친구의 수)를 선택한 후 친구 리스트 첫 번째에 포커스를 두고 실행을 눌러주세요.\n5초 후 작동 시작합니다.")
label4.pack()

num_of_exe = [i for i in range(1, 1000)]
combobox_exe = ttk.Combobox(exe_frame, height=5, values=num_of_exe, state="readonly")
combobox_exe.pack()
combobox_exe.set(1)

btn_exe = Button(exe_frame, width=10, padx=5, pady=5, text="실행", command=exe_check)
btn_exe.pack()

# btn_cancel = Button(exe_frame, width=10, padx=5, pady=5, text="중지", command=exe_cancel)
# btn_cancel.pack()

label5 = Label(exe_frame)
label5.pack()

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="About Macro", command=about_menu)
menu_view.add_checkbutton(label="About Expire", command=about_expire)
menu.add_cascade(label="Info", menu=menu_view)

root.config(menu=menu)
root.mainloop()