import  time
from PIL import ImageGrab
import numpy as np
import cv2

# print("5s将截图")
#
# time.sleep(5)
# tm = int(time.time()*1000) # 获得时间戳并取整
# img = ImageGrab.grab()
# img.save("D:\\.%s.png"%tm)
# print("截图已经保存")
# time.sleep(1)
# img.show()


img = ImageGrab.grab(bbox=(500,225,883,525))#设置窗口大小
img_np = np.array(img)
cv2.imshow('img',img_np)
if 0xFF & cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
