from django.test import TestCase
from ..models import *


class TesteModelsCase(TestCase):
    
    def setUp(self):
        Cliente.objects.create(
            clientes='Cliente 2',
            produto='Produto 2',
            grupo='Grupo 2',
            pedido='Pedido 2',
            vendedor='Vendedor 2',
            itens='Itens 2',
            data='2020-01-01'
        )
    
    def test_retorno_cliente(self):
        t1 = Cliente.objects.get(clientes='Cliente 2')
        self.assertEquals(t1.__str__(), 'Cliente 2')
    
    
        
        
