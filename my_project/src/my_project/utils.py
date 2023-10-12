
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
    # imgDataNp = np.array(imgData).reshape((1920,1080,3))  # 转换成三维数组

    spacing = int(width / 5)  # 两条竖线之间的间距
    for i in range(6):  # 遍历6条竖线
        for j in range(height):  # 遍历竖线上的像素点
            place = j*width + i*spacing  # 第i列第j行在imgData的位置
            try:
                if imgData[place] == (236, 236, 236):  # 找到(236,236,236)这个颜色值
                    if imgData[place-width] == (245, 245, 245) and imgData[place+width] in ((245, 245, 245), (255, 255, 255)):
                        # 判断分割线上面一个像素点和下面一个像素点的RGB值是否符合，防止误判

                        for long in range(1, 21):  # 判断分割线连续20个像素点是否都为(236,236,236)，防止误判
                            if imgData[place+long] != (236, 236, 236):
                                break
                        else:
                            # 返回正确的位置(微信输入框分割线上某个点的位置）
                            return place % width, int(place/width)
            except IndexError:
                # 当遍历到最后一个点的时候会超出索引范围
                return 0
    return 0
