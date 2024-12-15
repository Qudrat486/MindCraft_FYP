from django.db import models

class Categories(models.Model):
    icon = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name