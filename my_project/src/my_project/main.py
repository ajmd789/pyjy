import time
from utils import moveMouseToSearchBar
from utils import analysis_pixel
from utils import startQQ
from utils import imgToString
from utils import find_and_highlight_img
from utils import moveMouseToTargetArea
from utils import doubleClick
from utils import open_send_info
from utils import showDesktop
from utils import start_qq_from_the_taskbar
from utils import start_soft_from_none
from utils import showMaxJqka
from utils import start_chrome
from utils import get_difference_between_screen_shot
from utils import current_time

def main():
    res = get_difference_between_screen_shot()
    print(res,'<-识别',current_time())
    if res:
        send_stock_price_once(res)
    # 等待1秒钟
    else:
        time.sleep(3)
        # 再次调用main函数
        main()

def send_stock_price_once(code):
    # startQQ()
    # 从任务栏启动QQ
    start_qq_from_the_taskbar()
    # 识别图片内容
    # imgToString()
    image_path = r"C:\Users\Tom\Pictures\aiPractice\QQIcon.jpg"
    # 寻找图片区域坐标
    postion = find_and_highlight_img(image_path)
    print("移动鼠标")
    # 打开qq群
    result = moveMouseToTargetArea(postion, 200)
    if result is not None:
        print(f"鼠标成功移动到目标位置：{result}")
        doubleClick()
        # # 打开群聊天界面
        # copied_text = open_send_info()
        if code:
            showDesktop()
            start_chrome(code)
            print('本次股价发送完毕')
    time.sleep(1)
    while True:
        res = get_difference_between_screen_shot()
        print(res, '<-识别',current_time())
        if res:
            main()
            break  # 执行完main()函数后退出循环


if __name__ == "__main__":
    main()
