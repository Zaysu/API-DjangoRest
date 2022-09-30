from django.shortcuts import render
from core.services.post_service import get_clientes
from rest_framework import viewsets
from .models import Cliente
from .utils import PDFGenerator
from .serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


def listar_dados(request):
    clientes = get_clientes()
    return render(request, 'index.html', {'clientes': clientes})


def imprimir_dados_por_data(request):
    clientes = get_clientes()
    pdf = PDFGenerator()
    return pdf.render_to_pdf('vendas_data.html', {'clientes': clientes})

def imprimir_dados_por_vendedor(request):
    clientes = get_clientes()
    pdf = PDFGenerator()
    return pdf.render_to_pdf('vendas_vendedor.html', {'clientes': clientes})

def imprimir_dados_por_cliente(request):
    clientes = get_clientes()
    pdf = PDFGenerator()
    return pdf.render_to_pdf('vendas_cliente.html', {'clientes': clientes})

