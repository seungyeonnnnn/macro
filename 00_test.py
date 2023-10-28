import pyautogui
import time

# 타이핑할 문자열
text_to_type = "안녕하세요, 파이썬으로 타이핑 중입니다.adsfadsfasdf"

# 포커스를 타이핑 대상으로 이동 (예: 텍스트 편집기)
# 이 부분은 타겟 애플리케이션 및 운영 체제에 따라 다를 수 있습니다.
# 만약 다른 애플리케이션에 타이핑하려면 해당 애플리케이션으로 포커스를 전환해야 합니다.

# 문자열을 타이핑
pyautogui.typewrite(text_to_type, interval=0.3)  # 각 키 사이의 간격을 조절할 수 있음

# 작업이 완료될 때까지 잠시 기다릴 수 있습니다.
time.sleep(2)  # 2초 동안 대기

# 필요에 따라 화면 스크린샷을 찍거나 다른 동작을 수행할 수 있습니다.
,   .adsfadsfasdf