from django.db import models

# Create your models here.
class Card(models.Model):
    name=models.CharField(max_length=150)
    condition=models.DecimalField(max_digits=3, decimal_places=1)
    year=models.IntegerField()

    def __str__(self):
        return self.name