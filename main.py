import os

from py.person_detection_image import detect
from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def read_root():
    return {"Hello": "World"}

@app.get("/")
def main():
    return detect("img/zdj_1.jpg")
#    format = [".jpg", ".png", ".jpeg"]
    #path = 'img/'

'''    for (path, dirs, files) in os.walk(path):
        for file in files:
            if file.endswith(tuple(format)):
                print(file)
                zdjecie = path + file
                test.append(detect(zdjecie))'''

