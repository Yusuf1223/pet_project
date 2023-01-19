from django.db import models
from django.core.validators import MinLengthValidator


# Create your models here.

# Models for information about company and feedback from clients model
class Feedback(models.Model):
    name = models.CharField(max_length=128,
                            validators=[MinLengthValidator(2, "Name must have more than 2 characters")])

    number = models.CharField(max_length=16)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Info(models.Model):
    title = models.CharField(max_length=128,
                             validators=[MinLengthValidator(2, "Title must have more than 2 characters")])
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


# Watch Model and Models for Filtering

class Color(models.Model):
    title = models.CharField(max_length=128)


class Material(models.Model):
    title = models.CharField(max_length=128)


class WatchStyle(models.Model):
    title = models.CharField(max_length=128)


class Coating(models.Model):
    title = models.CharField(max_length=128)


class GlassMaterial(models.Model):
    title = models.CharField(max_length=128)


class Watch(models.Model):
    title = models.CharField(max_length=128,
                             validators=[MinLengthValidator(2, "Title must have more than 2 characters")])
    article = models.CharField(max_length=128,
                               validators=[MinLengthValidator(2, "Title must have more than 2 characters")])
    watch_size = models.IntegerField()

    watch_color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True, related_name='watch_color')
    watch_material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True, related_name='watch_material')
    bracelet_size = models.IntegerField()

    bracelet_color = models.ForeignKey('Color', on_delete=models.SET_NULL, null=True, related_name='bracelet_color')
    bracelet_material = models.ForeignKey('Material', on_delete=models.SET_NULL, null=True, related_name='bracelet_material')
    glass_material = models.ForeignKey('GlassMaterial', on_delete=models.SET_NULL, null=True)

    style = models.ForeignKey('WatchStyle', on_delete=models.SET_NULL, null=True)
    coating = models.ForeignKey('Coating', on_delete=models.SET_NULL, null=True)

    water_resistance = models.IntegerField()
    price = models.FloatField()
    count = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Image Model


class Image(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='static/img')


class WatchImage(Image):
    watch = models.ForeignKey('Watch', on_delete=models.CASCADE)
