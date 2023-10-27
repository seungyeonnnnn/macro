import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os  # 이미지 파일 삭제를 위한 os 모듈

def open_image_file():
    # 파일 대화 상자를 열어서 이미지 파일 선택
    file = filedialog.askopenfile(title="이미지 파일 선택", filetypes=[("이미지 파일", "*.png;*.jpg")])

    # 사용자가 이미지 파일을 선택하고 확인을 누르면
    if file:
        global image_path
        image_path = file.name
        file.close()

        # 파일 경로 출력
        file_path_label.config(text=f"선택한 파일 경로: {image_path}")

        # 선택한 이미지를 불러와서 160x160 픽셀 크기로 리사이즈
        image = Image.open(image_path)
        image = image.resize((160, 160))
        photo = ImageTk.PhotoImage(image)

        # 이미지를 라벨에 표시
        image_label.config(image=photo)
        image_label.image = photo
        image_label.pack()

def delete_image():
    global image_path
    if image_path:
        # 이미지 파일 삭제
        # os.remove(image_path)
        # 이미지 라벨 초기화
        image_label.config(image=None)
        # 파일 경로 초기화
        file_path_label.config(text="선택한 파일 경로: ")

# GUI 창을 생성
root = tk.Tk()
root.title("이미지 파일 선택")

# "이미지 열기" 버튼을 생성
open_button = tk.Button(root, text="이미지 열기", command=open_image_file)
open_button.pack()

# "경로 삭제" 버튼을 생성
delete_button = tk.Button(root, text="경로 삭제", command=delete_image)
delete_button.pack()

# 이미지를 표시할 라벨 생성
image_label = tk.Label(root)

# 파일 경로 출력 라벨 생성
file_path_label = tk.Label(root, text="선택한 파일 경로: ")
file_path_label.pack()

# 초기 이미지 경로를 None으로 설정
image_path = None

# GUI 루프 시작
root.mainloop()
