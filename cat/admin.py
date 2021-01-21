from django.contrib import admin
from .models import electronics
from .models import cloths,vehical,camera
from .models import furnitures

# Register your models here.
admin.site.register(electronics)
admin.site.register(cloths)
admin.site.register(furnitures)
admin.site.register(vehical)
admin.site.register(camera)