import os
import cv2 as cv

from py.person_detection_image import detect
from typing import Union
from fastapi import FastAPI, UploadFile, File
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/test")
def read_root():
    return {"Hello": "World"}


@app.get("/")
async def root():
    return FileResponse('index.html')


@app.get("/ml")
def main():
    return detect("img/zdj_1.jpg")


@app.post("/upload-test/")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        with open("uploaded_" + file.filename, "wb") as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    #finally:
        #file.file.close()
    return detect(file.filename)












    #return {"message": f"Successfuly uploaded {file}"}
    #return detect(file.filename)
'''async def image(image: UploadFile = File(...)):
    print(image.file)

    try:
        os.mkdir("images")
        print(os.getcwd())
    except Exception as e:
        print(e)
    file_name = os.getcwd() + "/images/" + image.filename.replace(" ", "-")

    with open(file_name, 'wb+') as f:
        f.write(image.file.read())
        f.close()

    img = cv.imread(file_name)
    return img
    #return detect(img)'''



'''async def form_post(request: Request,
                    file: UploadFile = File(...)
                    ):
    """Uploads the file and processes it in Pandas"""
    contents = await file.read()
    test_data = io.BytesIO(contents)
    df = pd.read_csv(test_data, sep=";")
    df.to_sql("alert_test", if_exists="replace", con=database.SQLALCHEMY_DATABASE_URL, index=False)
    return {"filename":file.filename}'''
