import numpy as np
from flask import Flask, request, jsonify, Response, render_template
import pickle
# from detect_mask_video import *
import threading
from imutils.video import VideoStream
from imutils.video import FileVideoStream
from flask_cors import CORS, cross_origin
# import the necessary packages
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2
import os
import uuid
import face_recognition
from face_matching import get_names
outputFrame = None
lock = threading.Lock()

app = Flask(__name__)

cors = CORS(app, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/")
@cross_origin()
def index():
    # return the rendered template
    return render_template("index.html")


def detect_and_predict_mask(frame, faceNet, maskNet, args):
    # global vs, outputFrame, lock
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detections
    faceNet.setInput(blob)
    detections = faceNet.forward()

    # initialize our list of faces, their corresponding locations,
    # and the list of predictions from our face mask network
    faces = []
    locs = []
    preds = []

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with
        # the detection
        confidence = detections[0, 0, i, 2]

        if confidence > args["confidence"]:
            # compute the (x, y)-coordinates of the bounding box for
            # the object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # ensure the bounding boxes fall within the dimensions of
            # the frame
            (startX, startY) = (max(0, startX), max(0, startY))
            (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

            # extract the face ROI, convert it from BGR to RGB channel
            # ordering, resize it to 224x224, and preprocess it
            face = frame[startY:endY, startX:endX]
            face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            face = cv2.resize(face, (224, 224))
            face = img_to_array(face)
            face = preprocess_input(face)
            face = np.expand_dims(face, axis=0)

            # add the face and bounding boxes to their respective
            # lists
            faces.append(face)
            locs.append((startX, startY, endX, endY))

    # only make a predictions if at least one face was detected
    if len(faces) > 0:
        # for faster inference we'll make batch predictions on *all*
        # faces at the same time rather than one-by-one predictions
        # in the above `for` loop
        preds = maskNet.predict(faces)

    # return a 2-tuple of the face locations and their corresponding
    # locations
    return (locs, preds)


def video_mask_detection():
    # construct the argument parser and parse the arguments

    global vs, outputFrame, lock
    # load our serialized face detector model from disk
    print("[INFO] loading face detector model...")
    prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
    weightsPath = os.path.sep.join([args["face"],
                                    "res10_300x300_ssd_iter_140000.caffemodel"])
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    # load the face mask detector model from disk
    print("[INFO] loading face mask detector model...")
    maskNet = load_model(args["model"])

    # initialize the video stream and allow the camera sensor to warm up
    print("[INFO] starting video stream...")
    vs = VideoStream(src=0).start()
    # vs = FileVideoStream("video_mri.mov").start()
    # fileStream = True
    time.sleep(2.0)

    val = [1]
    temp_frame = []
    person_name = ' '
    # loop over the frames from the video stream
    while True:
        
        # if fileStream and not vs.more():
        #     break
        
        try:
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
        except Exception as e:
            break
        
    
        (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet, args)
        if temp_frame != []:
            frame_encodings = face_recognition.face_encodings(frame)
            temp_frame_encodings = face_recognition.face_encodings(temp_frame)
            if len(frame_encodings) > 0:
                frame_encodings = frame_encodings[0]
                if len(temp_frame_encodings) > 0:
                    temp_frame_encodings = temp_frame_encodings[0]
                    val = face_recognition.face_distance([frame_encodings], temp_frame_encodings)
                    print(val)
            else:
                val = [0]

        for (box, pred) in zip(locs, preds):
            # unpack the bounding box and predictions
            (startX, startY, endX, endY) = box
            if locs != [] and preds != [] and val[0] > 0.60:
                print(val)
                person_name = " "
                if pred[1] > 0.97:
                    frame2 = frame[startY:endY+5, startX:endX+5]
                    filename = str(uuid.uuid1()) + '.png'
                    filepath = './cropped_images/' + str(filename)
                    cv2.imwrite(filepath, frame2)
                    temp_frame = frame
                    person_name = get_names()
                    if person_name == 'not_ available':
                        person_name = " "
                        temp_frame = []
                        val[0] = 1

            (mask, withoutMask) = pred

            # determine the class label and color we'll use to draw
            # the bounding box and text
            label = "Mask" if mask > withoutMask else "No Mask"
            color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
            if person_name == 'not available':
                person_name = ' '

            label2 = person_name if mask < withoutMask else " "
            # color = (0, 255, 0) if label2 == " " else (0, 0, 255)

            # include the probability in the label
            label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

            # display the label and bounding box rectangle on the output
            # frame
            cv2.putText(frame, label, (startX, startY - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.putText(frame, label2, (startX, endY + 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
            cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)




        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

        with lock:
            outputFrame = frame.copy()

    # do a bit of cleanup
    cv2.destroyAllWindows()
    vs.stop()

    # # grab the frame from the threaded video stream and resize it
        # # to have a maximum width of 400 pixels
        # frame = vs.read()
        # frame = imutils.resize(frame, width=400)
        #
        # # detect faces in the frame and determine if they are wearing a
        # # face mask or not
        # (locs, preds) = detect_and_predict_mask(frame, faceNet, maskNet, args)
        #
        # # loop over the detected face locations and their corresponding
        # # locations
        # for (box, pred) in zip(locs, preds):
        #     # unpack the bounding box and predictions
        #     (startX, startY, endX, endY) = box
        #     (mask, withoutMask) = pred
        #
        #     # determine the class label and color we'll use to draw
        #     # the bounding box and text
        #     label = "Mask" if mask > withoutMask else "No Mask"
        #     color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        #
        #     # include the probability in the label
        #     label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)
        #
        #     # display the label and bounding box rectangle on the output
        #     # frame
        #     cv2.putText(frame, label, (startX, startY - 10),
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        #     cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
        # # show the output frame
        # # cv2.imshow("Frame", frame)
        #
        # # print("till here?")
        # key = cv2.waitKey(1) & 0xFF
        #
        # # if the `q` key was pressed, break from the loop
        # if key == ord("q"):
        #     break

        # with lock:
        #     outputFrame = frame.copy()



def generate():
    # grab global references to the output frame and lock variables
    # global outputFrame, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if outputFrame is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')


@app.route("/video_feed")
@cross_origin()
def video_feed():
    # return the response generated along with the specific media
    # type (mime type)
    return Response(generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--face", type=str, default="face_detector", help="path to face detector model directory")
    ap.add_argument("-m", "--model", type=str, default="mask_detector.model",
                    help="path to trained face mask detector model")
    ap.add_argument("-c", "--confidence", type=float, default=0.50,
                    help="minimum probability to filter weak detections")
    args = vars(ap.parse_args())

    t = threading.Thread(target=video_mask_detection)
    t.daemon = True
    t.start()
    app.run("0.0.0.0", 5000, debug=True, threaded=True, use_reloader=False)
