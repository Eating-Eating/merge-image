import os
import random
from ctypes.wintypes import RGB
from io import BytesIO

from PIL import Image 

IMAGE_DIR = 'img'


def dfs (img, index):
    for addImg in arr[index]:
        tempImg = Image.new("RGBA", [64,64])
        tempImg.paste(img,(0,0), img)
        tempImg.paste(Image.open(addImg), (0,0), Image.open(addImg))
        if index == len(arr) - 1:
            tempImg.save(
                os.path.join(os.getcwd() + os.sep+'output', str(random.randint(0,100000000000000)) + '.png'),
                format="PNG")
        else:
            dfs(tempImg, index+1)


def main():
    path = os.path.join(os.getcwd(), IMAGE_DIR)
    arr = []
    for base_dir, sub_dir_list, sub_file_list in os.walk(path):
        temp = []
        for sub_file in sub_file_list:
            temp.append(base_dir + os.sep + sub_file)
        if len(temp) > 0:
            arr.append(temp)
    for base in arr[0]:
        dfs(Image.open(base),1)


if __name__ == '__main__':
    main()
