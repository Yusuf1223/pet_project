from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings


# Create your models here.

# Models for information about company and feedback from clients model
class Feedback(models.Model):
    name = models.CharField(max_length=128,
                            validators=[MinLengthValidator(2, "Name must have more than 2 characters")])

    number = models.CharField(max_length=128)
    email = models.EmailField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Info(models.Model):
    title = models.CharField(max_length=128,
                             validators=[MinLengthValidator(2, "Title must have more than 2 characters")])
    text = models.TextField()
    key = models.CharField(max_length=128)  # it determines which of the pages we are in

    def __str__(self):
        return self.key


class Contact(models.Model):
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=256)
    number = models.CharField(max_length=16)
    email = models.EmailField()

    def __str__(self):
        return self.title


class Right(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    ogrn = models.BigIntegerField()
    inn = models.BigIntegerField()
    kpp = models.BigIntegerField()
    legal_address = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.title


# Watch Model and Models for Filtering

class Color(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class WatchStyle(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Coating(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class GlassMaterial(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


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

    buyers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    through='Order', related_name='watch_buyers')

    def __str__(self):
        return self.title


# Image Model


class Image(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='static/img')

    def __str__(self):
        return self.name


class WatchImage(Image):
    watch = models.ForeignKey('Watch', on_delete=models.CASCADE)


# Cart and Status
class Status(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True,)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.user.name

