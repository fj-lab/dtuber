import glob
import os
import cv2


def main():

    #os.makedirs('fliped',exist_ok=True)
    img_list = glob.glob('./image_dir/*.jpg')

    # Flip images and save
    for path in img_list:
        name, ext = os.path.splitext(os.path.basename(path))
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        flip = cv2.flip(img, 1)
        cv2.imwrite('./image_dir/fliped_{}.jpg'.format(name), flip)


if __name__ == "__main__":
    main()
