import numpy as np
from PIL import Image, ImageDraw
import random

def wwwqq() :
    # 创建一个白色背景的图像
    # width, height = 400, 400
    width, height = 800, 460
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # 随机生成头形
    head_shape = random.choice(["circle", "square", "triangle"])
    if head_shape == "circle":
        draw.ellipse((50, 50, 350, 350), fill="lightblue")
    elif head_shape == "square":
        draw.rectangle((50, 50, 350, 350), fill="lightblue")
    else:
        draw.polygon([(200, 50), (50, 350), (350, 350)], fill="lightblue")

    # 随机生成眼睛
    eye_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    eye_size = random.randint(10, 30)
    eye_spacing = random.randint(50, 100)
    eye_y = random.randint(150, 250)
    draw.ellipse((150 - eye_spacing // 2 - eye_size, eye_y - eye_size // 2, 150 - eye_spacing // 2 + eye_size, eye_y + eye_size // 2), fill=eye_color)
    draw.ellipse((250 + eye_spacing // 2 - eye_size, eye_y - eye_size // 2, 250 + eye_spacing // 2 + eye_size, eye_y + eye_size // 2), fill=eye_color)

    # 随机生成鼻子
    nose_size = random.randint(10, 20)
    nose_color = (random.randint(150, 255), random.randint(100, 150), random.randint(50, 100))
    draw.polygon([(200 - nose_size // 2, 200), (200 + nose_size // 2, 200), (200, 200 + nose_size)], fill=nose_color)

    # 随机生成嘴巴
    mouth_width = random.randint(50, 100)
    mouth_height = random.randint(20, 40)
    mouth_color = (random.randint(150, 255), random.randint(50, 100), random.randint(50, 100))
    draw.rectangle((200 - mouth_width // 2, 250, 200 + mouth_width // 2, 250 + mouth_height), fill=mouth_color)

    # 随机生成发型
    hair_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(1000):
        x = random.randint(50, 350)
        y = random.randint(50, 150)
        radius = random.randint(1, 5)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=hair_color)

    # 显示头像
    image.show()



if __name__ == '__main__':

    for i in range(6):
     wwwqq()

