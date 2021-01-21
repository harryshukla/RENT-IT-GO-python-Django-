from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    message = models.CharField(max_length=1200)
    phone = models.CharField(max_length=111, default="")
    def __str__(self):
        return self.name