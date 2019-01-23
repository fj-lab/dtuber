forked  marando/pycatfd

pycatfd 🐈
==========
_Cat facial detection and landmark recognition with Python_

<img src="https://user-images.githubusercontent.com/4701701/27982869-8a7db7f4-637c-11e7-8cff-19a911fa2621.jpg" width="500" />


## Dependencies
* [dlib](https://github.com/davisking/dlib)
* [opencv](https://opencv.org)


## Python Requirements
* Pillow
* requests
* scikit-image 

+ Note: skimage.io segmentation fault

## Crop cat (experimental)
yolo.py can crop cats from original images.
If you want use, see [keras-yolo3](https://github.com/qqwweee/keras-yolo3).

1. Download YOLOv3 weights.
2. Convert YOLO model to keras model.
3. run yolo.py

