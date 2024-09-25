import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restpj.settings')
django.setup()




from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from . import crud,schemas


app= FastAPI()


app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])


@app.post("/product",response_model=schemas.Product)
def create_product(product:schemas.ProductCreate):
    return crud.create_product(product.dict())

@app.get("/product/{product_id}",response_model=schemas.Product)
def read_product(product_id:int):
    return crud.get_product(product_id)


@app.get("/product/",response_model=list[schemas.Product])
def read_product(skip:int=0,limit:int=10):
    return crud.get_product(skip=skip,limit=limit)

@app.put("/product/{product_id}",response_model=schemas.Product)
def update_product(product_id:int,product:schemas.ProductUpdate):
    return crud.update_product(product_id,product.dict())


@app.delete("/product/{product_id}",response_model=schemas.Product)
def delete_product(product_id:int):
    return crud.delete_product(product_id)



