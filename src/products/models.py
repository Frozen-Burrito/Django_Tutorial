from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=60) # max_length is required for CharField
	description = models.TextField(blank=True, null=True)
	price = models.DecimalField(decimal_places=2, max_digits=10000)
	summary = models.TextField()
	featured = models.BooleanField()