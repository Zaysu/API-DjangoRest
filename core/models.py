from django.db import models

class Cliente(models.Model):
    clientes = models.CharField(max_length=50)
    produto = models.CharField(max_length=50)
    grupo = models.CharField(max_length=50)
    pedido = models.CharField(max_length=50)
    vendedor = models.CharField(max_length=50)
    itens = models.CharField(max_length=50)
    data = models.DateTimeField()

    def __str__(self):
        return self.clientes
