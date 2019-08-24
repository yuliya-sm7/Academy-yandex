from django.db import models


class Citizen(models.Model):
    GENDER = (('M', 'male'), ('F', 'female'))
    citizen_id = models.IntegerField(default=0, null=False)
    town = models.CharField(max_length=256, null=False)
    street = models.CharField(max_length=256, null=False)
    building = models.CharField(max_length=256, null=False)
    apartment = models.IntegerField(null=False)
    name = models.CharField(max_length=256, null=False)
    birth_date = models.CharField(max_length=10, null=False)
    gender = models.CharField(max_length=256, null=False, choices=GENDER)
    relatives = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.name


class Import(models.Model):
    citizens = models.ManyToManyField(Citizen)
