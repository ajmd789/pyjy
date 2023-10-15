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


def main():
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
        # 打开群聊天界面
        copied_text = open_send_info()
        if copied_text:
            showDesktop()
            # "C:\Users\Tom\Pictures\aiPractice\jqkaIcon.jpg"
            can_start_jqka = start_soft_from_none(
                r"C:\Users\Tom\Pictures\aiPractice\jqkaIcon.jpg")
            if can_start_jqka:
                doubleClick()
                showDesktop()
                can_start_jqka = start_soft_from_none(
                r"C:\Users\Tom\Pictures\aiPractice\jqkaIcon.jpg")
                doubleClick()
                showMaxJqka(copied_text)
    else:
        print("鼠标移动失败")


if __name__ == "__main__":
    main()
