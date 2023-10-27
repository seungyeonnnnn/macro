import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk  # 이미지 파일을 불러오기 위한 PIL 라이브러리

root = Tk()
root.title("B Macro")
root.geometry("640x640")

def create_new_file():
    msgbox.showinfo("Information", "ㅈ같네 ㅅㅂ")

def about_menu():
    msgbox.showinfo("Information", "B Macro v0.0\nContact : fkdltldls@naver.com")

def sel_img_file():
    global img_label
    file = filedialog.askopenfile(title="파일 선택", filetypes=[("이미지 파일", "*.png;*.jpg;*jpeg;*gif;*bmp")])
    if file:
        image_path = file.name
        file.close()

        # 파일 경로 출력
        label3.config(text=f"사진 경로 : {image_path}")

        # 선택한 이미지를 불러와서 표시
        image = Image.open(image_path)
        image = image.resize((160, 160))  # 160x160 크기로 리사이즈
        photo = ImageTk.PhotoImage(image)

        # 이미지를 라벨에 표시
        img_label = Label(img_frame)
        img_label.config(image=photo)
        img_label.image = photo
        img_label.pack()


def del_img_file():
    label3.config(text="사진 경로")
    img_label.destroy()

msg_frame = LabelFrame(root, text="보낼 메세지")
msg_frame.pack(side="top", anchor="center", fill="both", expand=True, padx=5, pady=5)

img_frame = LabelFrame(root, text="사진도 보내려면 경로를 선택해 주세요. 없으면 보내지 않습니다.")
img_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

exe_frame = LabelFrame(root, text="실행")
exe_frame.pack(side="top", fill="both", expand=True, padx=5, pady=5)

# frame_burger = Frame(root, relief="solid", bd=1)
# frame_burger.pack(side="left", fill="both", expand=True)

# label1 = Label(msg_frame, text="보낼 메세지")
# label1.pack()

txt1 = Text(msg_frame, width=50, height=6)
txt1.pack()
txt1.insert(END, "놀러오세요.\n이벤트 중입니다.🎉")

# label2 = Label(img_frame, text="사진도 보내려면 경로를 선택해 주세요.")
# label2.pack(side="top")

btn_sel_path = Button(img_frame, width=10, padx=5, pady=5, text="경로 선택", command=sel_img_file)
btn_sel_path.pack()

btn_del_path = Button(img_frame, width=10, padx=5, pady=5, text="선택 취소", command=del_img_file)
btn_del_path.pack()

label3 = Label(img_frame, text="사진 경로 : ")
label3.pack()

# img_label = Label(img_frame)

label4 = Label(exe_frame, text="친구 리스트 첫 번째에 포커스를 두고 실행을 눌러주세요.\n5초 후 작동 시작합니다.")
label4.pack()

btn_exe = Button(exe_frame, width=10, padx=5, pady=5, text="실행")
btn_exe.pack()

btn_cancel = Button(exe_frame, width=10, padx=5, pady=5, text="중지")
btn_cancel.pack()

label5 = Label(exe_frame, text="실행 중입니다.")
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
menu.add_cascade(label="Info", menu=menu_view)

root.config(menu=menu)
root.mainloop()