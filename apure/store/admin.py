from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import (
    Category,
    Product,
    Product_Specification,
    ProductType,
    ProductSpecificationValue,
    ProductImage,
)


# Register your models here.
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Product, MPTTModelAdmin)
admin.site.register(Product_Specification, MPTTModelAdmin)
admin.site.register(ProductType, MPTTModelAdmin)
admin.site.register(ProductSpecificationValue, MPTTModelAdmin)
admin.site.register(ProductImage, MPTTModelAdmin)