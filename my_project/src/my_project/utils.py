
def help():
    print("Hello, World!")

import pyautogui

def moveMouseToSearchBar():
    # 获取屏幕的宽高
    screenWidth, screenHeight = pyautogui.size()

    # 移动鼠标光标到坐标（1290, 20）
    pyautogui.moveTo(1290, 20, duration=1)  # 可选：duration参数表示鼠标移动到目标位置的时间（秒）




