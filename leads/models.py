from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
