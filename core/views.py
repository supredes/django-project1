from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader

from .models import Produto

def index(request):
    """print(f"{'=' * 150}")
    print(f"Request: {request}")
    print(f"{'-' * 150}")
    print(f"DIR-REQUEST: {dir(request)}")
    print(f"{'-' * 150}")
    print(f"Method -------> [{request.method}]")
    print(f"User-Agent ---> [{request.headers['User-Agent']}]")
    print(f"Host ---------> [{request.headers['Host']}]")
    print(f"User Django --> [{request.user}]")
    print(f"User System --> [{request.environ['LOGNAME']}]")
    print(f"Path ---------> [{request.get_full_path_info}]")
    if str(request.user) != "AnonymousUser":
        status = f'User logged In: {request.user}'
        email = f"E-mail: {request.user.email}"
        contact = 'Contact: +5511997113688'
    else:
        status = "User Not Logged IN!"
        email = f"Browsing as: {request.user}"
        contact = 'Contact: +5511997113688'
    print(f"{'-' * 150}")
    context = {
        'curso': 'Web Programming with Django Framework',
        'desenvolvedor': 'Developed by: Damião Ribeiro',
        'contact': contact,
        'status': status,
        'email': email,
    }
    return render(request, 'index.html', context) # Passamos o dicionário assim como parametro para o retorno da função
                                                  # e fazemos a chamada pela chave 'curso' no template: index.html"""
    if str(request.user) != "AnonymousUser":
        status = f'User logged In: {request.user}'
        email = f"E-mail: {request.user.email}"
        contact = 'Contact: +5511997223688'
    else:
        status = "User Not Logged IN!"
        email = f"Browsing as: {request.user}"
        contact = 'Contact: +5511997223688'

    produtos = Produto.objects.all()
    separate = f"{'=' * 50}"
    context = {
        'curso': 'Web Programming with Django Framework',
        'desenvolvedor': 'Developed by: Damião Ribeiro',
        'status': status,
        'email': email,
        'contact': contact,
        'separate': separate,
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8, status=404')