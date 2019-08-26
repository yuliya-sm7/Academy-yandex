from django.db import models


class Citizen(models.Model):
    GENDER = (('M', 'male'), ('F', 'female'))
    citizen_id = models.IntegerField(default=0, null=False, blank=False,)
    town = models.CharField(max_length=256, null=False, blank=False,)
    street = models.CharField(max_length=256, null=False, blank=False,)
    building = models.CharField(max_length=256, null=False, blank=False,)
    apartment = models.IntegerField(null=False, blank=False,)
    name = models.CharField(max_length=256, null=False, blank=False,)
    birth_date = models.CharField(max_length=256, null=False, blank=False,)
    gender = models.CharField(max_length=256, null=False, blank=False, choices=GENDER)
    relatives = models.ManyToManyField('self')

    def __str__(self):
        return self.name

    def __int__(self):
        return self.citizen_id

class Import(models.Model):
    citizens = models.ManyToManyField(Citizen)
