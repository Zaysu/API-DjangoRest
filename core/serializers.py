from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'clientes', 'produto', 'grupo', 'pedido', 'vendedor', 'itens', 'data')
