from django.db import models

class Receipe(models.Model):
    receipe = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to="receipe")