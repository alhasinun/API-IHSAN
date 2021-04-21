# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import Optional
from fastapi import FastAPI, File, UploadFile
import json
from fastapi.responses import HTMLResponse

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/')
def read_root():
    return {"Hello":"World"}

# @app.get('/items/{items_id}')
# def read_item(item_id:int,q:Optional[str]=None):
#     return {"item_id":item_id, "q":q}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Optional[str] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# @app.post("/uploadcsv/")
# def upload_csv(csv_file: UploadFile = File(...)):
#     df = pd.read_csv(csv_file.file)
#     # do something with dataframe here (?)
#     return {"filename": file.filename}

@app.get("/tampilangka/")
def tampilangka():
    a = 1+2+3
    return {"tes":a}

@app.post("/uploadfiles/")
def create_upload_files(upload_file: UploadFile = File(...)):
    json_data = json.load(upload_file.file)
#     print(upload_file.file)
    return {"data_in_file": json_data}

# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/files/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
# <input name="files" type="file" multiple>
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)