from django.shortcuts import render
from django.http import HttpResponse

variable = [
    {"id":1, "nombre": "variable 1"},
    {"id":2, "nombre": "variable 2"},
    {"id":3, "nombre": "variable 3"},
    {"id":4, "nombre": "variable 4"},
]

# PAGINA PRINCIPAL (HOME.HTML)
def home(request):
    contexto = {"variable": variable}
    return render(request, "DLC/home.html", contexto)

# USO DE TEMPLATES CONDICIONALES (HTML)
def pagina1(reqest):    
    return render(reqest, "DLC/pagina1.html")

# USO DE TEMPLATES (HTML)
def pagina2(reqest):
    return render(reqest, "DLC/pagina2.html")