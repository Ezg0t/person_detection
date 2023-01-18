import cv2
import numpy
import numpy as np
import imutils
import base64

from fastapi import UploadFile
from starlette.responses import HTMLResponse

protopath = "model/MobileNetSSD_deploy.prototxt"
modelpath = "model/MobileNetSSD_deploy.caffemodel"
detector = cv2.dnn.readNetFromCaffe(prototxt=protopath, caffeModel=modelpath)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]


def detect(zdjecie):
    image = cv2.imread(zdjecie)
    image = imutils.resize(image, width=600)
    counter = 0
    (H, W) = image.shape[:2]

    blob = cv2.dnn.blobFromImage(image, 0.007843, (W, H), 127.5)
    detector.setInput(blob)
    person_detections = detector.forward()
    for i in np.arange(0, person_detections.shape[2]):
        confidence = person_detections[0, 0, i, 2]

        if confidence > 0.5:
            idx = int(person_detections[0, 0, i, 1])

            if CLASSES[idx] != "person":
                continue

            person_box = person_detections[0, 0, i, 3:7] * np.array([W, H, W, H])
            (startX, startY, endX, endY) = person_box.astype("int")

            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            counter = counter + 1
    print("Ilość wykrytych ludzi na zdjęciu: " + str(counter))
    cv2.imshow("Results", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    _, im_arr = cv2.imencode('.jpg', image)  # im_arr: image in Numpy one-dim array format.
    im_bytes = im_arr.tobytes()
    im_b64 = base64.b64encode(im_bytes)

    html_content = """
        <div>
                <img src="data:image/png;base64, """ + im_b64.decode("utf-8") + """" alt="Red dot" />
        </div>

        """

    return {"img": im_b64.decode("utf-8"), "count": str(counter)}


