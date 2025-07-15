import torch
import cv2
from pathlib import Path
import logging
import subprocess
import os

subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5.git"], check=True)
os.chdir("yolov5")
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

print("YOLOv5 cloned and ready.")
image_path = "tikvahpharma"
subprocess.run([
    "python", "detect.py",
    "--source", image_path,
    "--save-txt",
    "--save-conf",
    "--project", "results",
    "--name", "run1"
], check=True)

