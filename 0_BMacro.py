import time
import datetime
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk  # 이미지 파일을 불러오기 위한 PIL 라이브러리
import keyboard
import pyautogui

KEY = "1234"
EXPIRE_Y = 2023
EXPIRE_M = 11

text_to_type = "abcdefg"

root = Tk()
root.title("B Macro")
root.geometry("640x480")

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
            kakao_macro()
        else:
            label5.config(text="키 코드가 일치하지 않아 실행되지 않습니다.")
    else:
        label5.config(text="사용 기간이 만료되어 실행되지 않습니다.")

def exe_cancel():
    label5.config(text="중지되었습니다.")

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
    # while(True):
    keyboard.press_and_release('Enter')
    time.sleep(0.2)
    pyautogui.typewrite(text_to_type, interval=0.1)
    time.sleep(0.2)
    keyboard.press_and_release('Enter')
    time.sleep(0.2)
    keyboard.press_and_release('ESC')
    exe_cancel()

key_frame = LabelFrame(root, text="키 코드")
key_frame.pack(side="top", anchor="center", fill="both", expand=True, padx=5, pady=5)

msg_frame = LabelFrame(root, text="보낼 메세지")
msg_frame.pack(side="top", anchor="center", fill="both", expand=True, padx=5, pady=5)

img_frame = LabelFrame(root, text="사진도 보내려면 아래를 확인해주세요.")
img_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

exe_frame = LabelFrame(root, text="실행")
exe_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# frame_burger = Frame(root, relief="solid", bd=1)
# frame_burger.pack(side="left", fill="both", expand=True)

# label1 = Label(msg_frame, text="보낼 메세지")
# label1.pack()

keycode = Entry(key_frame, width=50)
keycode.pack()
keycode.insert(END, "1234")

txt1 = Text(msg_frame, width=50, height=6)
txt1.pack()
txt1.insert(END, "놀러오세요.\n이벤트 중입니다.🎉")

chk_var_img = IntVar()
chk_box_img = Checkbutton(img_frame, text="사진도 보내기", variable=chk_var_img)
chk_box_img.pack()

help_msg = Label(img_frame, text="※ 사진을 보내려면 보내려는 사진을 클립보드에 복사해주세요.\n\"Ctrl+v\"시 사진이 붙어져야합니다.")
help_msg.pack()

chk_var_img_after = IntVar()
chk_var_img_after.set(1)
chk_box_img_after = Checkbutton(img_frame, text="사진을 먼저 보내기(체크 해제 시 메세지를 먼저 보냅니다.)", variable=chk_var_img_after, onvalue=1)
chk_box_img_after.pack()

label4 = Label(exe_frame, text="친구 리스트 첫 번째에 포커스를 두고 실행을 눌러주세요.\n5초 후 작동 시작합니다.")
label4.pack()

btn_exe = Button(exe_frame, width=10, padx=5, pady=5, text="실행", command=exe_check)
btn_exe.pack()

btn_cancel = Button(exe_frame, width=10, padx=5, pady=5, text="중지", command=exe_cancel)
btn_cancel.pack()

label5 = Label(exe_frame)
label5.pack()

menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File", command=create_new_file)
# menu_file.add_command(label="New window")
# menu_file.add_separator()
# menu_file.add_command(label="Open File...")
# menu_file.add_separator()
# menu_file.add_command(label="Save All", state="disable")
# menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="About Macro", command=about_menu)
menu_view.add_checkbutton(label="About Expire", command=about_expire)
menu.add_cascade(label="Info", menu=menu_view)

root.config(menu=menu)
root.mainloop()