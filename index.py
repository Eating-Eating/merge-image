import os
import random
from ctypes.wintypes import RGB
from turtle import width
from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator, ValidationError
from prompt_toolkit.styles import Style
from io import BytesIO

from PIL import Image 

IMAGE_DIR = 'img'

mystyle = Style.from_dict({
    '':          '#00ffff',
})

class NumberValidator(Validator):
    def validate(self, document):
        text = document.text

        if text and not text.isdigit():
            i = 0

            # Get index of first non numeric character.
            # We want to move the cursor here.
            for i, c in enumerate(text):
                if not c.isdigit():
                    break

            raise ValidationError(message='This input contains non-numeric characters',
                                  cursor_position=i)


def dfs (img, index,arr,size):
    for addImg in arr[index]:
        tempImg = Image.new("RGBA", size)
        tempImg.paste(img,(0,0), img)
        tempImg.paste(Image.open(addImg), (0,0), Image.open(addImg))
        if index == len(arr) - 1:
            imageName = str(random.randint(0,100000000000000)) + '.png'
            print('output:'+ imageName)
            tempImg.save(
                os.path.join(os.getcwd() + os.sep+'output', imageName),
                format="PNG")
        else:
            dfs(tempImg, index+1,arr,size)


def main(size = [64,64]):
    path = os.path.join(os.getcwd(), IMAGE_DIR)
    arr = []
    for base_dir, sub_dir_list, sub_file_list in os.walk(path):
        temp = []
        for sub_file in sub_file_list:
            temp.append(base_dir + os.sep + sub_file)
        if len(temp) > 0:
            arr.append(temp)
    for base in arr[0]:
        dfs(Image.open(base),1,arr,size)


if __name__ == '__main__':
    width = prompt('Give me ouput width(px): ',validator=NumberValidator(),style= mystyle)
    height = prompt('Give me ouput height(px): ',validator=NumberValidator(),style= mystyle)
    main([int(width),int(height)])
