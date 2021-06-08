#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time
import os
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fashion.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


# def yolo_init():
#     # YOLO 설정 파일 Path
#     labelsPath = os.getcwd()+"\\df2.names"  # Hand 라벨
#     weightsPath = os.getcwd()+"\\yolov3-df2_15000.weights"  # 가중치
#     configPath = os.getcwd()+"\\yolov3-df2.cfg"  # 모델 구성

#     # YOLO 라벨(hand) 호출
#     YOLO_LABELS = open(labelsPath).read().strip().split("\n")

#     # YOLO 모델 호출
#     yolo_net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)
#     print("실행")
#     return yolo_net, YOLO_LABELS


if __name__ == '__main__':
    main()
    # yolo_init()
