from django.db import models

# Create your models here.
from django.db import models

class Todo(models.Model):
    name = models.CharField(max_length=80)
    id = models.IntegerField(primary_key=True)
    status = models.BooleanField(False)