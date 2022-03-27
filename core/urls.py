from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='pagina_principal'), # Cria rota para a função index da "views" e nomeia a rota de pagina_principal
    path('contato', contato, name='contato'), # Cria rota para a função contato da "views" e nomeia a rota de contato
    path('produto/<int:pk>', produto, name='produto'), # Cria rota para a função produto da "views" e nomeia a rota de produto
    ]

    # ---------------------------INDEX.HTML--------------------------
    # <a href="{% url 'produto' produto.id %}">{{ produto.nome }}</a>
    #
    # Na função