from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

# Models for information about company and feedback from clients model
class Feedback(models.Model):
    name = models.CharField(max_length=128,
                            validators=[MinLengthValidator(2, "Name should be longer than 2 characters")])

    number = models.CharField(max_length=16)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Info(models.Model):
    title = models.CharField(max_length=128,
                             validators=[MinLengthValidator(2, "Title should be longer than 2 characters")])
    text = models.TextField()
    key = models.CharField(max_length=128)  # it determines which of the pages we are in


class Contact(models.Model):
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    number = models.CharField(max_length=16)
    email = models.EmailField()


class Right(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    ogrn = models.BigIntegerField()
    inn = models.BigIntegerField()
    kpp = models.BigIntegerField()
    legal_address = models.CharField(max_length=128)
    email = models.EmailField()

