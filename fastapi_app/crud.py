import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restpj.settings')
django.setup()





from django.apps import apps
from fastapi import HTTPException

Product=apps.get_model('product','Product')

def create_product(product_data):
    product=Product.objects.create(**product_data)
    return product
def get_product(product_id):
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise HTTPException(status_code=404,details="product not found")
def update_product(product_id,product_data):
    product=get_product(product_id)
    for attr,value in product_data.itesm():
        setattr(product,attr,value)
    product.save()
    return product


def delete_product(product_id):
    product=get_product(product_id)
    product.delete()
    return product



    

