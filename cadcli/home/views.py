from django.shortcuts import render, redirect
from .models import Cliente

# Create your views here.
def home(request):
    return render(request, 'index.html')

def consultar(request):
    clientes = Cliente.objects.all()
    return render(request, 'consultar.html', {'clientes': clientes})

def cadastro(request):
    return render(request, 'cadastro.html')

def salvar(request):
    vnome = request.POST.get('nome')
    vdtnasc = request.POST.get('dtnasc')
    vtelefone = request.POST.get('telefone')
    vestado = request.POST.get('estado')
    vgenero = request.POST.get('genero')
    vemail = request.POST.get('email')
    Cliente.objects.create(nome=vnome, dtnasc=vdtnasc, telefone=vtelefone, estado=vestado, genero=vgenero, email=vemail)
    clientes = Cliente.objects.all()
    return render (request, 'cadastro.html', {'clientes': clientes})

def excluir(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('consultar')

def editar(request, id):
    cliente= Cliente.objects.get(id=id)
    return render(request, 'update.html', {'cliente': cliente})

def atualizar(request, id):
    vnome = request.POST.get('nome')
    vdtnasc = request.POST.get('dtnasc')
    vtelefone = request.POST.get('telefone')
    vestado = request.POST.get('estado')
    vgenero = request.POST.get('genero')
    vemail = request.POST.get('email')
    cliente= Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.dtnasc = vdtnasc
    cliente.telefone = vtelefone
    cliente.estado = vestado
    cliente.genero = vgenero
    cliente.email = vemail
    cliente.save()
    return redirect(consultar)

def buscar(request):
    clientes = Cliente.objects.all()
    return render(request, 'buscar.html')

def busca(request):
    if 'nome' in request.POST:
        nome = request.POST['nome']
        clientes = Cliente.objects.filter(nome__icontains=nome)
    else:
        clientes = Cliente.objects.all()
    return render(request, 'buscar.html', {'clientes':clientes})        