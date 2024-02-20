from django.db import models
from django.contrib.auth.models import User
 
class Tags(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Apostila(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    titulo = models.CharField(max_length=100)
    arquivo = models.FileField(upload_to='apostilas')
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return self.titulo
    
class ViewApostila(models.Model):
    ip = models.GenericIPAddressField()
    apostila = models.ForeignKey(Apostila, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.ip