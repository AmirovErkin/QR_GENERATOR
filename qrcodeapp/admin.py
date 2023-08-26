from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.QRCode)
admin.site.register(models.WifiCode)
admin.site.register(models.LinkCode)
admin.site.register(models.SocialCode)

