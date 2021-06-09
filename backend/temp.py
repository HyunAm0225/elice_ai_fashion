import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import os
# color boundaries

LOWER_HSV = {
    'red': np.array([0, 100, 20], np.uint8),
    "orange": np.array([10, 100, 20], np.uint8),
    'yellow': np.array([17, 100, 20], np.uint8),
    'green': np.array([60, 100, 20], np.uint8),
    'blue': np.array([90, 100, 20], np.uint8),
    "navy": np.array([110, 100, 20], np.uint8),
    "purple": np.array([125, 100, 20], np.uint8),
    "pink": np.array([135, 100, 20], np.uint8),

    "black": np.array([0, 0, 0], np.uint8),
    "white": np.array([0, 30, 200], np.uint8),
    "grey": np.array([0, 0, 0], np.uint8),
    "beige": np.array([0, 0, 0], np.uint8),
    "brown": np.array([0, 0, 0], np.uint8),
}

UPPER_HSV = {
    'red': np.array([10, 255, 255], np.uint8),
    "orange": np.array([20, 255, 255], np.uint8),
    'yellow': np.array([35, 255, 255], np.uint8),
    'green': np.array([90, 255, 255], np.uint8),
    'blue': np.array([110, 255, 255], np.uint8),
    "navy": np.array([125, 255, 255], np.uint8),
    "purple": np.array([135, 255, 255], np.uint8),
    "pink": np.array([170, 255, 255], np.uint8),

    "black": np.array([180, 30, 30], np.uint8),
    "white": np.array([0, 30, 200], np.uint8),
    "grey": np.array([0, 0, 0], np.uint8),
    "beige": np.array([0, 0, 0], np.uint8),
    "brown": np.array([0, 0, 0], np.uint8)
}


def yolo_init():
    # YOLO 설정 파일 Path
    labelsPath = os.getcwd()+"/df2.names"  # Hand 라벨
    weightsPath = os.getcwd()+"/yolov3-df2_15000.weights"  # 가중치
    configPath = os.getcwd()+"/yolov3-df2.cfg"  # 모델 구성

    # YOLO 라벨(hand) 호출
    YOLO_LABELS = open(labelsPath).read().strip().split("\n")

    # YOLO 모델 호출
    yolo_net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
    return yolo_net, YOLO_LABELS


def calculate_area(image, image_area, color):
    result = 0
    kernal = np.ones((5, 5), 'uint8')

    # Convert BGR color space to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define masks for each color
    mask = cv2.inRange(hsv_image,
                       LOWER_HSV[color], UPPER_HSV[color])

    # Create contour
    mask = cv2.dilate(mask, kernal)
    cv2.bitwise_and(image, image, mask=mask)
    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Track color
    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > image_area * 0.001):
            _, _, w, h = cv2.boundingRect(contour)
            result += w*h

    return result


def detect_color(image, leftup=None, rightdown=None):
    # Get image
    height, width, _ = image.shape
    image_area = height * width

    # Calcuate color areas
    white_area = calculate_area(image, image_area, 'white')
    red_area = calculate_area(image, image_area, 'red')
    green_area = calculate_area(image, image_area, 'green')
    blue_area = calculate_area(image, image_area, 'blue')
    yellow_area = calculate_area(image, image_area, 'yellow')
    orange_area = calculate_area(image, image_area, 'orange')
    black_area = calculate_area(image, image_area, 'black')
    grey_area = calculate_area(image, image_area, 'grey')
    beige_area = calculate_area(image, image_area, 'beige')
    brown_area = calculate_area(image, image_area, 'brown')
    navy_area = calculate_area(image, image_area, 'navy')
    purple_area = calculate_area(image, image_area, 'purple')
    pink_area = calculate_area(image, image_area, 'pink')

    areas = {'white': white_area, 'grey': grey_area, 'black': black_area, 'beige': beige_area, 'brown': brown_area,
             'blue': blue_area, 'navy': navy_area, 'purple': purple_area, 'green': green_area, 'red': red_area,
             'orange': orange_area, 'yellow': yellow_area, 'pink': pink_area}

    return max(areas, key=lambda x: areas[x])


def get_feature(yolo_net, image_path, YOLO_LABELS):

    # YOLO 출력층 설정
    layer_names = yolo_net.getLayerNames()
    output_layers = [layer_names[i[0] - 1] for i in yolo_net.getUnconnectedOutLayers()]
    colors = np.random.uniform(0, 255, size=(len(YOLO_LABELS), 3))

    frame_id = 0
    count = 0

    # img = cv2.imread('./test\\1.jpg', cv2.IMREAD_COLOR)
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img_height, img_width, channels = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416),  swapRB=True, crop=False)  # mean=(0,0,0)

    yolo_net.setInput(blob)
    outs = yolo_net.forward(output_layers)

    # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.6:
                # Object detected
                center_x = int(detection[0] * img_width)
                center_y = int(detection[1] * img_height)
                width = int(detection[2] * img_width)
                height = int(detection[3] * img_height)

                # Rectangle coordinates
                xx = int(center_x - width / 2)
                yy = int(center_y - height / 2)

                boxes.append([xx, yy, width, height])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    # NMS 처리하기
    conf_threshold = 0.1
    nms_threshold = 0.4
    idxs = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    draw_img = img.copy()
    count = 0
    feature_list = []

    if len(idxs) > 0:
        for i in idxs.flatten():
            feature = {}
            box = boxes[i]
            if box[1] < 0:
                box[1] = 0
            if box[0] < 0:
                box[0] = 0
            left = box[0]
            top = box[1]
            width = box[2]
            height = box[3]
            # labels_to_names 딕셔너리로 class_id값을 클래스명으로 변경. opencv에서는 class_id + 1로 매핑해야함.
            caption = "{}: {:.4f}".format(YOLO_LABELS[class_ids[i]], confidences[i])
            feature[YOLO_LABELS[class_ids[i]]] = "N/A"
            # cv2.rectangle()은 인자로 들어온 draw_img에 사각형을 그림. 위치 인자는 반드시 정수형.
            cv2.rectangle(draw_img, (int(left), int(top)), (int(left+width), int(top+height)), color=(0, 255, 0), thickness=2)

            crop_img = img[top:top + height, left:left + width]
            feature[YOLO_LABELS[class_ids[i]]] = detect_color(crop_img)
            count += 1
            feature_list.append(feature)
    else:
        feature["N/A"] = "N/A"
        feature_list.append(feature)

    return feature_list


if __name__ == "__main__":
    print("실행")
