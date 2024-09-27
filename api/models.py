# cspell:disable
'''TBD'''
from django.db import models

class Venda(models.Model):
    '''TBD'''
    id_venda = models.CharField(max_length=50)
    cliente = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField()

    def __str__(self):
        return str(self.cliente)
