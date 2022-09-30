from django.urls import path
from .views import *

urlpatterns = [
    path('endpoint', listar_dados, name='listar_dados'),
    path('imprimir_dados_por_data', imprimir_dados_por_data, name='imprimir_dados_por_data'),
    path('imprimir_dados_por_vendedor', imprimir_dados_por_vendedor, name='imprimir_dados_por_vendedor'),
    path('imprimir_dados_por_cliente', imprimir_dados_por_cliente, name='imprimir_dados_por_cliente'),
]
