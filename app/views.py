from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',)

def cadastro(request):
    if request.method == 'POST':
        # Lógica para processar o formulário de cadastro enviado

        # Exemplo de obtenção dos dados do formulário
        nome = request.POST.get('cadastro')
        email = request.POST.get('cadastro')
        emailportal = request.POST. get('cadastro')
        confirmarEmailPortal = request.POST.get('cadastro')
        senhaPortal = request.POST.get('cadastro')

        # ... obter outros dados do formulário

        # Lógica para salvar os dados do cadastro no banco de dados ou em outro lugar

        # Exemplo de redirecionamento para uma página de sucesso após o cadastro
        return HttpResponse('Cadastro realizado com sucesso!')
    else:
        # Se a requisição for GET, exibir o formulário de cadastro
        return render(request, 'cadastro.html')
    
    