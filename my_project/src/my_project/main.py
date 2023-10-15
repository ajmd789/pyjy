from utils import moveMouseToSearchBar
from utils import analysis_pixel
from utils import startQQ
from utils import imgToString
from utils import find_and_highlight_img
from utils import moveMouseToTargetArea
from utils import doubleClick
from utils import open_send_info
def main():
    # startQQ()
    # 识别图片内容
    # imgToString()
    image_path = r"C:\Users\Tom\Pictures\aiPractice\QQIcon.jpg"
    # 寻找图片区域坐标
    postion = find_and_highlight_img(image_path)
    print("移动鼠标")
    # 打开qq群
    result = moveMouseToTargetArea(postion,200)
    if result is not None:
        print(f"鼠标成功移动到目标位置：{result}")
        doubleClick()
        open_send_info()
    else:
        print("鼠标移动失败")
if __name__ == "__main__":
    main()