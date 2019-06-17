#Views vai extrair informações do model que você criou e entregá-las a um template
from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
