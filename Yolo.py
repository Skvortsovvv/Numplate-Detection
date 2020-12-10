import cv2
import numpy as np
import glob
import random

def detection():

    net = cv2.dnn.readNet("yolov3_training_last.weights", "yolov3_testing.cfg")

    # Name custom object
    classes = ["numplate"]

    # Images path
    images_path = glob.glob(r"image.jpg")

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    # Insert here the path of your images
    random.shuffle(images_path)

    im = images_path[0]
    photo = cv2.imread(im)
    q, w, r = photo.shape
    if min(q, w) < 399:
        print(q,w)
        return -1

    def cropingg(image):

        (h, w, c) = image.shape
        center = (w/2, h/2)
        print(center, "in croping function")
        x = int(center[0])
        y = int(center[1])
        image = image[y-int(0.7*y):y+int(0.7*y), x-int(0.7*x):x+int(0.7*x)]
        return image
    # loop through all the images

    ind = 1  # for filename number
    for img_path in images_path:
        # Loading image
        img = cv2.imread(img_path)
        img = cv2.resize(img, None, fx=0.5, fy=0.5)
        hh, ww, cc = img.shape
        if min(hh,ww) < 199:
            print("image size is low")
            return -1
        restart = True
        counter = 0
        while restart:

            height, width, channels = img.shape
            print(img.shape, "in cicle")
            # Detecting objects
            blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

            net.setInput(blob)
            outs = net.forward(output_layers)

            # Showing informations on the screen
            class_ids = []  # Номер класса
            confidences = []  # Вероятность
            boxes = []   # Рамки
            for out in outs:
                for detection in out:
                    scores = detection[5:]
                    class_id = np.argmax(scores)
                    confidence = scores[class_id]
                    if confidence > 0.3:
                        # Object detected
                        center_x = int(detection[0] * width)
                        center_y = int(detection[1] * height)
                        w = int(detection[2] * width)
                        h = int(detection[3] * height)

                        # Rectangle coordinates
                        x = int(center_x - w / 2)
                        y = int(center_y - h / 2)

                        boxes.append([x, y, w, h])
                        confidences.append(float(confidence))
                        class_ids.append(class_id)

            indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
            if len(indexes) == 0:
                if (counter < 5 ):
                    counter += 1
                    print(counter, "enter for crop")
                    img = cropingg(img)
                else:
                    return -2
            else:
                restart = False
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(classes[0])
                color = (0, 250, 29)
                num_plate = img
                num_plate = num_plate[y-5:y+h+5, x-5:x+w+5]
                num_plate = cv2.cvtColor(num_plate, cv2.COLOR_BGR2GRAY)
                fxx = 2
                if counter != 0:
                    fxx *= counter * 1.4
                num_plate = cv2.resize(num_plate, None, fx=fxx, fy=fxx )
                cv2.imwrite(str(ind) + ".jpg", num_plate)
                ind += 1
        return ind
