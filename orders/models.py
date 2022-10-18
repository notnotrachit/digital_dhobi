from django.db import models

# Create your models here.
class orders(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    enroll_no = models.CharField(max_length=100)
    room= models.CharField(max_length=100)
    kurta = models.IntegerField()
    pyjama = models.IntegerField()
    shirt = models.IntegerField()
    tshirt = models.IntegerField()
    pant = models.IntegerField()
    lower = models.IntegerField()
    shorts = models.IntegerField()
    bedsheet = models.IntegerField()
    pillowcover = models.IntegerField()
    towel = models.IntegerField()
    dupatta = models.IntegerField()
    total_clothes = models.IntegerField()

