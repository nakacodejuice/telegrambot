from django.db import models
import datetime

class Request(models.Model):
    requesttext = models.TextField()
    DateTimeField = models.DateTimeField('date created', auto_now_add=True)
    Messanger = models.CharField(max_length=20,default='telegram')

class AccountLinkToId(models.Model):
    lschet = models.CharField(max_length=24,primary_key=True)
    id = models.IntegerField()
    current = models.BooleanField(default=True)
    datetimelastmesg = models.DateTimeField('date created', auto_now_add=True)
    NumTreeMesg = models.IntegerField(default=0)
    def __str__(self):
        return self.lschet