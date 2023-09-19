from django.db import models

class new_model(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    age = models.IntegerField()


class new_class(models.Model):
    name = models.CharField(max_length=100)