from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=64, unique=False)
    surname = models.CharField(max_length=64, unique=False)
    remarks = models.TextField()

class Adress(models.Model):
    city = models.CharField(max_length=64, unique=False)
    street = models.CharField(max_length=64, unique=False)
    house_number = models.IntegerField(max_length=5, unique=False)
    flat_number =  models.IntegerField(max_length=5, unique=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Telephone(models.Model):
    phone_type = (
        (1, "Domowy"),
        (2, "Kom"),
        (3, "Praca"),
        (4, "Inny")
    )
    tel_number = models.IntegerField(max_length=10)
    tel_type = models.IntegerField(choices=phone_type)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Email(models.Model):
    email_type = (
        (1, "Domowy"),
        (2, "Praca"),
        (3, "Inny"),
    )
    email_address = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Groups(models.Model):
    group_name = models.CharField(max_length=64)
    group_desc = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)