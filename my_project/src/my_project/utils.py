
from PIL import ImageGrab
import pyautogui
import numpy as np
import subprocess
import time
import pytesseract
import cv2
from PIL import Image
import pyscreeze
import pyperclip
import re
import PIL.ImageGrab
import datetime
import itertools

def help():
    print("Hello, World!")

def current_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前北京时间
    return  current_time
def doubleClick():
    """
    Perform a double click at the current mouse cursor location.
    """
    pyautogui.doubleClick()  # 执行鼠标双击操作

# 移动到同花顺搜索框位置


def moveMouseToSearchBar():
    # 获取屏幕的宽高
    screenWidth, screenHeight = pyautogui.size()

    # 移动鼠标光标到坐标（1290, 20）
    pyautogui.moveTo(1290, 20, duration=1)  # 可选：duration参数表示鼠标移动到目标位置的时间（秒）

# 移动鼠标到指定区域


def moveMouseToTargetArea(coordinates, widthRight=None):
    try:
        # 检查输入参数是否为空或者长度不为2
        if coordinates is None or len(coordinates) != 2:
            raise ValueError("Error: 不合法的坐标元组.")

        # 解构输入的元组，获取目标区域的左上角坐标和右下角坐标
        top_left, bottom_right = coordinates

        # 检查左上角和右下角坐标是否为空
        if top_left is None or bottom_right is None:
            raise ValueError("Error: Invalid input coordinates.")

        # 计算目标区域的中心坐标
        target_center_x = (top_left[0] + bottom_right[0]) // 2
        target_center_y = (top_left[1] + bottom_right[1]) // 2

        # 计算横向平移后的新坐标
        if (widthRight):
            new_x = target_center_x + widthRight
            new_y = target_center_y
        else:
            new_x = target_center_x
            new_y = target_center_y
        # 移动鼠标到新坐标位置
        # duration参数表示鼠标移动到目标位置的时间（秒）
        pyautogui.moveTo(new_x, new_y, duration=1)

        # 返回新的坐标值
        return new_x, new_y

    except Exception as e:
        print(f"出错：{e}")
        # 返回None表示出错
        return None


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


def start_qq_from_the_taskbar():
    print('start')
    image_path = r"C:\Users\Tom\Pictures\aiPractice\qqSoftIcon.jpg"
    # 寻找图片区域坐标
    postion = find_and_highlight_img(image_path)
    print("移动鼠标")
    # 打开qq群
    result = moveMouseToTargetArea(postion)
    if result is not None:
        pyautogui.click()
        time.sleep(1)
# 根据图片url调用


def start_soft_from_none(image_path):
    # 寻找图片区域坐标
    postion = find_and_highlight_img(image_path)
    result = moveMouseToTargetArea(postion)
    if result is not None:
        return True
    else:
        return False


def startQQ():
    # 定义要执行的命令
    command = 'start "" "C:\\Program Files (x86)\\Tencent\\QQ\\Bin\\QQScLauncher.exe"'
    # 执行命令
    subprocess.run(command, shell=True)
    # 等待3秒钟（可以根据实际情况调整等待时间）
    time.sleep(3)
    # 模拟按下Enter键
    pyautogui.press('enter')
    time.sleep(10)


def imgToString():
    img_path = r'C:\Users\Tom\Pictures\ai训练\Snipaste_2023-01-25_18-01-37.jpg'
    try:
        image = Image.open(img_path)
        text = pytesseract.image_to_string(image, lang='chi_sim')
        print(text)
    except FileNotFoundError:
        print(f"Error: File '{img_path}' not found.")
    except Exception as e:
        print(f"Error: {e}")


def find_and_highlight_img(target_image_path):
    # 读取目标图像
    target_img = cv2.imread(target_image_path)

    # 获取屏幕截图
    screen_img = pyscreeze.screenshot()

    # 将截图转换为OpenCV格式
    screen_img = np.array(screen_img)
    screen_img = cv2.cvtColor(screen_img, cv2.COLOR_RGB2BGR)

    # 在屏幕图像中寻找目标图像的匹配位置
    result = cv2.matchTemplate(screen_img, target_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_val, max_val, min_loc, max_loc)
    # 获取目标图像的宽度和高度
    target_width, target_height = target_img.shape[1], target_img.shape[0]

    # 如果匹配度足够高（这里可以根据需要调整阈值），则标记并返回匹配区域的坐标
    if max_val > 0.4:
        top_left = max_loc
        bottom_right = (top_left[0] + target_width,
                        top_left[1] + target_height)

        # # 在屏幕图像上绘制匹配区域的边框
        # cv2.rectangle(screen_img, top_left, bottom_right, (0, 0, 255), 2)

        # # 显示标记了匹配区域的图像
        # cv2.imshow('Highlighted Image', screen_img)
        # cv2.waitKey(0)  # 等待用户按下任意键
        # cv2.destroyAllWindows()  # 关闭所有OpenCV窗口

        # 返回匹配区域的坐标信息
        return top_left, bottom_right
    else:
        print("Error: Target image not found on the screen.")
        return None


def open_send_info():
    send_path = r"C:\Users\Tom\Pictures\aiPractice\qqSendButton.jpg"
    time.sleep(1)
    send_position = find_and_highlight_img(send_path)
    send_button_result = moveMouseToTargetArea(send_position, -200)
    if send_button_result is not None:
        print(f"鼠标成功移动到目标位置：{send_button_result}")
        time.sleep(1)
        moveMouseToNewMessage(660, 590)
        doubleClick()
        time.sleep(0.5)

        # 模拟鼠标点击和复制操作（Ctrl + C）
        pyautogui.hotkey('ctrl', 'c')

        # 获取剪贴板的内容
        copied_text = pyperclip.paste()

        # 输出复制的文本
        print("复制的文本：", copied_text)
        return copied_text


#   根据入参移动鼠标到指定坐标；入参非元组
def moveMouseToNewMessage(wdith, height):
    # 获取屏幕的宽高
    screenWidth, screenHeight = pyautogui.size()

    # 移动鼠标光标到坐标（1290, 20）
    # 可选：duration参数表示鼠标移动到目标位置的时间（秒）
    pyautogui.moveTo(wdith, height, duration=0)

# 移动鼠标到指定区域


def showDesktop():
    time.sleep(1)
    try:
        # 使用Win + D组合键最小化所有窗口显示桌面
        pyautogui.hotkey('win', 'd')
    except Exception as e:
        print(f"出错：{e}")


def start_jqka_from_none(image_path):
    # 寻找图片区域坐标
    postion = find_and_highlight_img(image_path)
    result = moveMouseToTargetArea(postion)
    if result is not None:
        pyautogui.click()
        return True
    else:
        return False


def showMaxJqka(copied_text):
    moveMouseToNewMessage(1042, 532)
    pyautogui.doubleClick()
    time.sleep(10)
    interval = 0.1  # 设置输入速度，以秒为单位
    pyautogui.typewrite(copied_text, interval=interval)
    time.sleep(2)
    # 模拟按下Enter键
    pyautogui.press('enter')


def start_chrome(code):
    can_start_chrome = start_chrome_from_none(
        r"C:\Users\Tom\Pictures\aiPractice\chromeIcon.jpg")
    if can_start_chrome:
        pyautogui.click()
        moveMouseToNewMessage(1052, 80)
        pyautogui.click()
        copied_text = 'https://xueqiu.com/S/SZ002567'
        interval = 0.03  # 设置输入速度，以秒为单位
        # 模拟按下Ctrl + A（全选）
        pyautogui.sleep(1)  # 例如等待1秒
        pyautogui.hotkey('ctrl', 'a')

        # 等待一些时间，以确保全选操作完成（可以根据实际情况调整等待时间）
        pyautogui.sleep(1)  # 例如等待1秒

        # 模拟按下Delete键（删除选中的内容）
        pyautogui.press('delete')
        pyautogui.typewrite(copied_text, interval=interval)
        pyautogui.sleep(0.5)  # 例如等待1秒
        pyautogui.press('enter')

        pyautogui.sleep(3)  # 例如等待1秒
        moveMouseToNewMessage(990, 133)
        pyautogui.click()
        copied_text = code
        pyautogui.click()
        pyautogui.typewrite(copied_text, interval=interval)
        pyautogui.sleep(3)
        moveMouseToNewMessage(874, 230)
        pyautogui.click()
        pyautogui.sleep(3)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        # 模拟鼠标点击和复制操作（Ctrl + C）
        pyautogui.hotkey('ctrl', 'c')
        # 获取剪贴板的内容
        copied_text = pyperclip.paste()
        # 定义正则表达式模式
        pattern = r'¥.*?%'

        # 使用正则表达式进行匹配
        matches = re.findall(pattern, copied_text)
        print(matches)
        # 输出匹配到的结果
        showDesktop()
        for match in matches:
            print("".join(match))

            start_qq_from_the_taskbar()
            # 识别图片内容
            # imgToString()
            image_path = r"C:\Users\Tom\Pictures\aiPractice\QQIcon.jpg"
            # 寻找图片区域坐标
            postion = find_and_highlight_img(image_path)
            print("移动鼠标")
            # 打开qq群
            result = moveMouseToTargetArea(postion, 200)
            if result:
                doubleClick()
                open_send_info_type_stock_price()
                pyautogui.typewrite(match, interval=interval)
                # 模拟按下Enter键
                pyautogui.press('enter')

                # 在操作之后清空剪切板的内容
                pyperclip.copy('')


def start_chrome_from_none(image_path):
    # 寻找图片区域坐标
    postion = find_and_highlight_img(image_path)
    result = moveMouseToTargetArea(postion, 80)
    if result is not None:
        return True
    else:
        return False


def open_send_info_type_stock_price():
    send_path = r"C:\Users\Tom\Pictures\aiPractice\qqSendButton.jpg"
    time.sleep(1)
    send_position = find_and_highlight_img(send_path)
    send_button_result = moveMouseToTargetArea(send_position, -200)
    if send_button_result is not None:
        print(f"鼠标成功移动到目标位置：{send_button_result}")
        time.sleep(1)


def get_difference_between_screen_shot():
    # 562.484,1144,633
    # Set the region you want to monitor (left, top, width, height)
    time.sleep(5)
    monitoring_region = (562, 484, 1144, 633)
    values = pytesseract.image_to_string(
        ImageGrab.grab().crop(monitoring_region))
    
    # 使用正则表达式查找5或6位连续数字
    pattern = r'\b\d{5,6}\b'  # 匹配5或6位连续数字的正则表达式
    matches = re.findall(pattern, values)

    # 如果找到匹配项，则打印出来，否则返回None
    if matches:
        print(matches[0])
        return matches[0]
    else:
        return None