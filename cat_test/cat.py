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
    return np.array(array, np.int32).reshape((-1, 1, 2))


def main():
    os.makedirs('original',exist_ok=True)
    os.makedirs('landmarks',exist_ok=True)
    
    color = (255,255,255)
    thickness = 3
    count = 0
    b = []
    b.append([])
    b.append([])
    b.append([])
    c = []
    c.append([])
    d = []
    d.append([])
    d.append([])
    e = []
    e.append([])
    e.append([])
    f = []
    f.append([])
    g = []
    g.append([])
    h = []
    h.append([])
    h.append([])
    j = []
    j.append([])
    j.append([])
    k = []
    k.append([])
    k.append([])
    k.append([])
    m = []
    m.append([])
    m.append([])
    m.append([])
    ago = []
    ago.append([])

    for frame in range(1,FRAME_NUM+1):
        img = cv2.imread(str(frame) + '.jpg')
        df = pd.read_csv(str(frame) + '.csv',header=None)
        black_image = np.zeros(img.shape,np.uint8)
        print(df)
        b[0].append(int(df[0][0].split(",")[0]))
        b[0].append(int(df[0][0].split(",")[1]))
        b[1].append(int(df[1][0].split(",")[0]))
        b[1].append(int(df[1][0].split(",")[1]))
        b[2].append(int(df[0][1].split(",")[0]))
        b[2].append(int(df[0][1].split(",")[1]))

        c[0].append(int(df[0][2].split(",")[0]))
        c[0].append(int(df[0][2].split(",")[1]))

        d[0].append(int(df[0][0].split(",")[0]))
        d[0].append(int(df[0][0].split(",")[1]))
        d[1].append(int(df[0][3].split(",")[0]))
        d[1].append(int(df[0][3].split(",")[1]))

        e[0].append(int(df[1][0].split(",")[0]))
        e[0].append(int(df[0][0].split(",")[1]))
        e[1].append(int(df[0][4].split(",")[0]))
        e[1].append(int(df[0][4].split(",")[1]))

        f[0].append(int(df[0][5].split(",")[0]))
        f[0].append(int(df[0][5].split(",")[1]))

        g[0].append(int(df[0][6].split(",")[0]))
        g[0].append(int(df[0][6].split(",")[1]))

        h[0].append(int(df[0][0].split(",")[0]))
        h[0].append(int(df[0][0].split(",")[1]))
        h[1].append(int(df[0][7].split(",")[0]))
        h[1].append(int(df[0][7].split(",")[1]))

        j[0].append(int(df[1][0].split(",")[0]))
        j[0].append(int(df[0][0].split(",")[1]))
        j[1].append(int(df[0][8].split(",")[0]))
        j[1].append(int(df[0][8].split(",")[1]))
        
        k[0].append(int(df[0][3].split(",")[0]))
        k[0].append(int(df[0][3].split(",")[1]))
        k[1].append(int(df[0][3].split(",")[0]))
        k[1].append(int(df[0][5].split(",")[1]))
        k[2].append(int(df[0][1].split(",")[0]))
        k[2].append(int(df[0][1].split(",")[1]))

        m[0].append(int(df[0][8].split(",")[0]))
        m[0].append(int(df[0][8].split(",")[1]))
        m[1].append(int(df[0][8].split(",")[0]))
        m[1].append(int(df[0][5].split(",")[1]))
        m[2].append(int(df[0][1].split(",")[0]))
        m[2].append(int(df[0][1].split(",")[1]))

        ago[0].append(int(df[0][1].split(",")[0]))
        ago[0].append(int(df[0][1].split(",")[1]))

        jaw = reshape_for_polyline(b)
        Left_Eye = reshape_for_polyline(c)
        Nose = reshape_for_polyline(f)
        Right_Eye = reshape_for_polyline(g)
        Left_of_Left_Ear = reshape_for_polyline(d)
        Right_of_Left_Ear = reshape_for_polyline(h)
        Left_of_Right_Ear = reshape_for_polyline(e)
        Right_of_Right_Ear = reshape_for_polyline(j)
        Left_to_Chin = reshape_for_polyline(k)
        Right_to_Chin = reshape_for_polyline(m)
        
        #cv2.polylines(black_image,[jaw],False,color,thickness)
        #cv2.polylines(black_image,[Left_Eye],True,color,thickness)
        cv2.circle(black_image,tuple(flatten for inner in c for flatten in inner),20,color,thickness)
        cv2.polylines(black_image,[Nose],True,color,thickness)
        cv2.polylines(black_image,[Left_of_Left_Ear],True,color,thickness)
        cv2.polylines(black_image,[Right_of_Left_Ear],True,color,thickness)
        cv2.polylines(black_image,[Left_of_Right_Ear],True,color,thickness)
        cv2.polylines(black_image,[Right_of_Right_Ear],True,color,thickness)
        cv2.polylines(black_image,[Left_to_Chin],False,color,thickness)
        cv2.polylines(black_image,[Right_to_Chin],False,color,thickness)
        cv2.circle(black_image,tuple([flatten for inner in g for flatten in inner]),20,color,thickness)
        

        cv2.rectangle(black_image,(69,539),(967,497),color,thickness)
        
    #cv2.imshow("asdf",black_image)
    cv2.imwrite("bbb.png",black_image)
    cv2.waitKey(0)


if __name__ == '__main__':

    main()
