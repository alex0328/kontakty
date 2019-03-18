from django.db import models

# Create your models here.

PHONE_TYPE = (
    (1, "Domowy"),
    (2, "Kom"),
    (3, "Praca"),
    (4, "Inny")
)


EMAIL_TYPE = (
    (1, "Domowy"),
    (2, "Praca"),
    (3, "Inny"),
)


class Person(models.Model):
    name = models.CharField(max_length=64, unique=False)
    surname = models.CharField(max_length=64, unique=False)
    remarks = models.TextField()
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        str = 'id: {}, name: {}, surname: {}, remarks: {}'.format(self.id,self.name, self.surname, self.remarks)
        return str

class Adress(models.Model):
    city = models.CharField(max_length=64, unique=False)
    street = models.CharField(max_length=64, unique=False)
    house_number = models.IntegerField(unique=False)
    flat_number = models.IntegerField(unique=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        str = 'id: {}, city: {}, street: {}, house_number: {}'.format(self.id,self.city, self.street, self.house_number)
        return str

class Telephone(models.Model):
    tel_number = models.IntegerField()
    tel_type = models.IntegerField(choices=PHONE_TYPE, default=1)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        str = 'id: {}, tel_number: {}, tel_type: {}, person: {}'.format(self.id,self.tel_number, self.tel_type, self.person)
        return str


class Email(models.Model):
    email_type = models.IntegerField(choices=EMAIL_TYPE, default=1)
    email_address = models.CharField(max_length=64)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        str = 'id: {}, email_type: {}, email_address: {}, person: {}'.format(self.id,self.email_type, self.email_address, self.person)
        return str

class Groups(models.Model):
    group_name = models.CharField(max_length=64)
    group_desc = models.CharField(max_length=64)
    person = models.ManyToManyField(Person)

    def __str__(self):
        str = 'id: {}, group_name: {}, group_desc: {}, person: {}'.format(self.id,self.group_name, self.group_desc, self.person)
        return str
