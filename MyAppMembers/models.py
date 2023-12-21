from django.db import models

class Membros(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    telefone = models.IntegerField(null=True)
    data_entrada = models.DateField(null=True)

    # def __str__(self):
    #     return f"{self.firstname} {self.lastname}"