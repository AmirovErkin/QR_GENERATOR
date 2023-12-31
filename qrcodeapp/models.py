from django.db import models

# Create your models here.

class WifiCode(models.Model):
    wifi_name = models.CharField(max_length=100)
    encryiption = models.TextField()
    password = models.CharField(max_length=30)



class LinkCode(models.Model):
    link = models.TextField()

class SocialCode(models.Model):
    username = models.CharField(max_length=40)


class QRCode(models.Model):
    image = models.ImageField(upload_to='qrcodes/')
    created_at = models.DateTimeField(auto_now_add=True)
