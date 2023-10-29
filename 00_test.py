# import keyboard
# import time

# time.sleep(5)
# # keyboard.press_and_release('ctrl+alt+d')
# for i in range(10):
#     time.sleep(1)
#     keyboard.press_and_release('3')

# import pyperclip

# text_to_copy = "이것은 클립보드에 복사된 텍스트입니다."
# pyperclip.copy(text_to_copy)

# text_pasted = pyperclip.paste()
# print("클립보드에서 가져온 텍스트:", text_pasted)

from PIL import Image
import pyperclip

# 이미지 파일 경로
image_path = "C:\\Users\\SEUNGYEON\\Desktop\\Clipboard01.png"
image_path = "C:/Users/SEUNGYEON/Desktop/macro/temp_clipboard_image.png"

# 이미지를 클립보드에 복사
def copy_image_to_clipboard(image_path):
    try:
        image = Image.open(image_path)
        image.save("temp_clipboard_image.png")  # 일시적으로 이미지를 저장
        pyperclip.copy("temp_clipboard_image.png")  # 클립보드에 이미지 파일 경로 복사
        print(f"이미지를 클립보드에 복사했습니다.")
    except Exception as e:
        print(f"이미지를 클립보드에 복사하는 중 오류 발생: {str(e)}")

# 클립보드에 복사한 이미지 붙여넣기
def paste_image_from_clipboard():
    try:
        image_path = pyperclip.paste()  # 클립보드에서 이미지 파일 경로 가져오기
        if image_path.endswith(".png"):
            image = Image.open(image_path)
            image.show()  # 이미지를 뷰어로 열기
            print(f"클립보드에서 이미지를 붙여넣었습니다.")
        else:
            print("클립보드에 있는 내용이 이미지 파일이 아닙니다.")
    except Exception as e:
        print(f"클립보드에서 이미지를 붙여넣는 중 오류 발생: {str(e)}")

# 이미지를 클립보드에 복사
copy_image_to_clipboard(image_path)

# 클립보드에 복사한 이미지 붙여넣기
paste_image_from_clipboard()
