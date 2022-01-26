from ctypes.wintypes import RGB
from PIL import Image 
from io import BytesIO
import random
import os
path = os.getcwd() + os.sep + 'img'
arr = []
for main_dir, sub_dir_list, subFile_list in os.walk(path):
  temp = []
  for p in subFile_list:
    temp.append(main_dir + os.sep + p)
  if len(temp) > 0 :
    arr.append(temp)


def dfs (img,index):
  for addImg in arr[index]:
    tempImg = Image.new("RGBA",[64,64])
    tempImg.paste(img,(0,0),img)
    tempImg.paste(Image.open(addImg),(0,0),Image.open(addImg))
    if index == len(arr) - 1 :
      tempImg.save(os.path.join(os.getcwd()+os.sep+'output',str(random.randint(0,100000000000000))+'.png'), format="PNG")
    else :
      dfs(tempImg,index+1)

  
for base in arr[0]:
  dfs(Image.open(base),1)