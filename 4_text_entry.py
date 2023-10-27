from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END, "Type something")

e = Entry(root, width=30)
e.pack()
e.insert(0, "type 1line")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 1 : 1번째 라인, 0 : 0번째 column
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()