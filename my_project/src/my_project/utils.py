
from PIL import ImageGrab
import pyautogui
import numpy as np


def help():
    print("Hello, World!")


def moveMouseToSearchBar():
    # 获取屏幕的宽高
    screenWidth, screenHeight = pyautogui.size()

    # 移动鼠标光标到坐标（1290, 20）
    pyautogui.moveTo(1290, 20, duration=1)  # 可选：duration参数表示鼠标移动到目标位置的时间（秒）


def analysis_pixel():
    width, height = 1920, 1080
    img = ImageGrab.grab((0, 0, width, height))
    imgData = img.getdata()
    spacing = int(width / 5)  # 两条竖线之间的间距
    
    for i in range(6):
        for j in range(height):
            place = j * width + i * spacing
            try:
                if imgData[place] == (236, 236, 236):
                    if imgData[place - width] == (245, 245, 245) and imgData[place + width] in ((245, 245, 245), (255, 255, 255)):
                        for long in range(1, 21):
                            if imgData[place + long] != (236, 236, 236):
                                break
                        else:
                            # 找到微信输入框的位置
                            x, y = place % width, int(place / width)
                            print(f"找到微信输入框位置：({x}, {y})")
                            return x, y
            except IndexError:
                # 当遍历到最后一个点的时候会超出索引范围
                return None
    print("未找到微信输入框位置")
    return None
