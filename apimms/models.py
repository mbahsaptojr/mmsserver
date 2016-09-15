from django.db import models
import uuid
from django.contrib.auth.models import User


class Donator(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    CATEGORIES = (
        ('i','individu'),
        ('c', 'company')
    )

    category = models.CharField(max_length=1, choices=CATEGORIES)

    user = models.ForeignKey(User, on_delete=models.CASCADE)



# Create your models here.
