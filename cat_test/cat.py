import os
import cv2
import dlib 
import time
import argparse
import numpy as np
from imutils import video
from PIL import Image
import pandas as pd

DOWNSAMPLE_RATIO = 4
FRAME_NUM = 1

def reshape_for_polyline(array):
    return 0#np.array(array, np.int32).reshape((-1, 1, 2))


def main():
    os.makedirs('original',exist_ok=True)
    os.makedirs('landmarks',exist_ok=True)
    
    color = (255,255,255)
    thickness = 3
    count = 0
       
    for frame in range(1,FRAME_NUM+1):
        img = cv2.imread(str(frame) + '.jpg')
        df = pd.read_csv(str(frame) + '.csv',header=None)
        black_image = np.zeros(img.shape,np.uint8)
        print(df[0][0].split(','))
        jaw = reshape_for_polyline(df[0][0].split(','))
        cv2.polylines(black_image,[jaw],False,color,thickness)
        
    cv2.imshow("asdf",black_image)


if __name__ == '__main__':

    main()
