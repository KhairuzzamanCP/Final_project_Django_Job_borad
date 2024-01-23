from django.db import models

# Create your models here.
class ServiceModel(models.Model):
    slug = models.SlugField(max_length = 50, blank=True , null= True)
    service = models.CharField(max_length = 50)

    def __str__(self):
        return self.service