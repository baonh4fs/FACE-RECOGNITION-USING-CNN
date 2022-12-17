import os
import cv2
import numpy as np
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import matplotlib as plt


def make_folder(dataset_folder):
    if not os.path.exists(dataset_folder):
        os.makedirs(dataset_folder)
    else:
        print("Folder {} is existed !".format(str(dataset_folder)))
    return dataset_folder


def load_datasets(dataset="datasets/", max_sample=100):
    names = []
    images = []

    for folder in os.listdir(dataset):
        files = os.listdir(os.path.join(dataset, folder))[:max_sample]

        for file in files:
            images.append(file)
            names.append(folder)

    return names, images


def convert_categorical(names):
    le = LabelEncoder()
    le.fit(names)
    labels = le.classes_
    print("List labels: {}".format(labels))

    name_vector = le.transform(names)
    label_name_vector = to_categorical(name_vector)
    return label_name_vector, labels


def split_dataset(images, label_name_vector, test_size=0.2):
    x_train, x_test, y_train, y_test = train_test_split(np.array(images, dtype=np.float32),
                                                        np.array(label_name_vector),
                                                        test_size=test_size,
                                                        random_state=42)
    return x_train, x_test, y_train, y_test


def detector_face():
    img = cv2.imread("datasets/baonh/baonh.1.jpg")
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces = face_detector.detectMultiScale(image=img, scaleFactor=1.1, minNeighbors=5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img=img,
                      pt1=(x, y),
                      pt2=(x + w, y + h),
                      color=(255, 0, 0),
                      thickness=2)
    img = cv2.resize(img, (600, 600))
    cv2.imshow(winname="Camera", mat=img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
