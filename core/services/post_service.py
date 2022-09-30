from ..models import Cliente

def get_clientes():
    clientes_post = Cliente.objects.all()
    return clientes_post