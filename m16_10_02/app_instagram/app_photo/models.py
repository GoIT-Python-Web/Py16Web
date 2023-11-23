from pathlib import Path
from uuid import uuid4

from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError


def validate_file_size(value):
    filesize = value.size

    if filesize > 1_000_000:
        raise ValidationError('Максимальний розмір файлу 1Мб')
    return value


def upload_image(instance, filename):
    upload_to = Path(instance.user.username) if instance.user else Path('images')
    ext = Path(filename).suffix
    new_filename = f"{uuid4().hex}{ext}"
    return str(upload_to / new_filename)


# Create your models here.
class Picture(models.Model):
    description = models.CharField(max_length=300)
    path = models.ImageField(upload_to=upload_image, validators=[validate_file_size])
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, default=None)
