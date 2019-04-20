from keras.layers import Activation,Convolution2D,Dropout,Conv2D
from keras.layers import AveragePooling2D,BatchNormalization
from keras.layers import GlobalAveragePooling2D
from keras.models import Sequential
from keras.layers import Flatten
from keras.models import Model
from keras.layers import Input
from keras.layers import MaxPooling2D
from keras.layers import SeparableConv1D
from keras import layers
# from keras.regularizers import 12

def simple_CNN(input_shape ,num_classes):
    model = Sequential()
    # 第一层卷积层
    model.add(Convolution2D(filters = 16,kernel_size = (7,7),padding = 'same',name = 'image_array',input_shape = 'input_shape'))
    model.add(BatchNormalization())
    model.add(Convolution2D(filters = 16,kernel_size = (7,7),padding = 'same'))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(AveragePooling2D(pool_size = (2,2),padding =  'same'))
    model.add(Dropout(.5))
    # 第二层卷积层
    model.add(Convolution2D(filters=32, kernel_size=(5, 5), padding='same'))
    model.add(BatchNormalization())
    model.add(Convolution2D(filters=32, kernel_size=(5, 5), padding='same'))
    # 把彩色图像转换为灰色图像
