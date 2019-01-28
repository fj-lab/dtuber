import keras
from keras.preprocessing.image import ImageDataGenerator

num_fakeimg = 1000
img_path = './image_dir'
save_path = './image_dir'


if __name__ == "__main__":
    
    # Data augmentation
    gen = ImageDataGenerator(
        rotation_range=10,
        zoom_range=0.2,
        horizontal_flip=True,
    )
    
    data_generator = gen.flow_from_directory(
        img_path,
        target_size=(1080, 1920),
        batch_size=1,
        class_mode=None,
        save_to_dir=save_path,
        save_format='jpg'
    )

    # Generate fake images
    i=0
    for d in data_generator:
        i+=1
        if (i == num_fakeimg):
            break
