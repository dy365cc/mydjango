from django.db import models

# Create your models here.
class userinfo(models.Model):
    userID = models.CharField(max_length = 10)
    name = models.CharField(max_length = 50)
    pwd = models.CharField(max_length = 100)
    userlevel = models.IntegerField()

class xm_xmjbxx(models.Model):
    xmbm = models.CharField(max_length = 50)
    xmnc = models.CharField(max_length=20)