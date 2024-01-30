import cv2
import os
from PIL import Image

import numpy as np
import random

# 打开图像
img_dir = 'picture/'

def generator (option): #option 是该猫狗生成器模型的输入项，表示用户输入是1还是2.
    probability_cat=0.8 #probability表示猫的正确输出概率。
    probability_dog = 0.7 #probability表示狗的正确输出概率。

    if option == 1: #输入1时，大概率输出猫。
        ppw = probability_cat * 100
        n = random.randint(1, 100)
        if n <= ppw:
            image_path = os.path.join(img_dir, "cat.jpg")
            name = "cat"
        else:
            image_path = os.path.join(img_dir, "dog.jpg")
            name = "dog"

    elif option == 2: #输入2时，大概率输出狗。
        ppw = probability_dog * 100
        n = random.randint(1, 100)
        if n <= ppw:
            image_path = os.path.join(img_dir, "dog.jpg")
            name = "dog"
        else:
            image_path = os.path.join(img_dir, "cat.jpg")
            name = "cat"
    else:
        print("输入非法！")
        exit()

    image = cv2.imread(image_path) #读取需要输出的图像
    #cv2.imshow(name, image) #以name命名，来显示图像。这里由于这一句会阻断程序运行，所以放到下面的main函数里了。


    #cv2.destroyAllWindows()

    image = Image.open(image_path)  # 打开img_dir路径下的图片
    image = image.resize([208, 208])   # 改变图片的大小，定为宽高都为208像素
    image_array = np.array(image)            # 转成多维数组，向量的格式
    #print(type(image_array))
    return(image_array)


if __name__ == '__main__':
    # 调试猫狗机
    while 1:
        input_char = input("请输入选项(1 或 2 或 3):")
        input_num=int(input_char) #将输入的字符转化成数值。
        generator(input_num) #将数值给猫狗生成器。
    # 显示图像
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
