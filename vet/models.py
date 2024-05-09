from django.db import models

# Create your models here.


class Client(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    district = models.CharField(max_length=50)

    def __str__(self):
        return self.name + ' ' + self.lastname + ' - ' + self.dni


class PetSize(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size


class PetGender(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    gender = models.CharField(max_length=6)

    def __str__(self):
        return self.gender


class Specie(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Breed(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Services_Names(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Service Name'
        verbose_name_plural = 'Service Names'

    def __str__(self):
        return self.name


class Services(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.ForeignKey(Services_Names, on_delete=models.CASCADE)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
    price = models.FloatField()

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name.name + ' - ' + self.specie.name + ' - ' + self.size.size + ' - S/.' + str(self.price)


class Appointment(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    reason = models.CharField(max_length=100)
    considerations = models.CharField(max_length=100)

    def __str__(self):
        return self.client.name + ' ' + self.pet.name + ' - ' + self.date


class Pet(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=100)
    specie = models.ForeignKey(Specie, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    age = models.IntegerField()
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
    gender = models.ForeignKey(PetGender, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
