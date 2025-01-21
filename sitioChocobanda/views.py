from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class detalleIntegrante(View):
    def get(self, request, id):
        integrante = get_object_or_404(Integrante, id=id)
        context = {
            'integrante': integrante,
        }
        return render(request, 'detalleIntegrante.html', context)

class Integrantes(View):
    def get(self, request):
        actuales = Integrante.objects.filter(estado='actuales')
        print(actuales)
        invitados = Integrante.objects.filter(estado='invitados')
        memorables = Integrante.objects.filter(estado='memorables')
        context = {
            'actuales': actuales,
            'invitados': invitados,
            'memorables': memorables,
        }
        return render(request, 'integrantes.html', context)

class PaginaPrincipal(View):
    def get(self, request):
        context = {}
        return render(request, 'home.html', context)

class Nosotros(View):
    def get(self, request):
        context = {}
        return render(request, 'nosotros.html', context)

class NuestraHistoria(View):
    def get(self, request):
        context = {}
        return render(request, 'nuestraHistoria.html', context)

class Galeria(View):
    def get(self, request):
        context = {}
        return render(request, 'galeria.html', context)

class Login(View):
    def get(self, request):
        context = {}
        return render(request, 'login.html', context)

class ContraseñaOlvidada(View):
    def get(self, request):
        context = {}
        return render(request, 'recuperarContraseña.html', context)

class Contacto(View):
    def get(self, request):
        context = {}
        return render(request, 'contacto.html', context)

class ImpactoSocial(View):
    def get(self, request):
        context = {}
        return render(request, 'impactoSocial.html', context)

class Novedades(View):
    def get(self, request):
        context = {}
        return render(request, 'novedades.html', context)

class Novedad(View):
    def get(self, request):
        context = {}
        return render(request, 'novedad.html', context)

class ImpactoSocialInsti(View):
    def get(self, request):
        context = {}
        return render(request, 'impactoSocial-Insti.html', context)

class ImpactoSocialGaleria(View):
    def get(self, request):
        context = {}
        return render(request, 'impactoSocial-Galeria.html', context)

class Obra(View):
    def get(self, request):
        context = {}
        return render(request, 'obra.html', context)
