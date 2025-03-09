from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.utils.timezone import now  # Importa la función now para obtener la fecha y hora actuales
from .models import Evento, Noticia, Integrante, Obra, Institucion


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
        todos_integrantes = Integrante.objects.all()
        context = {
            'actuales': actuales,
            'invitados': invitados,
            'memorables': memorables,
            'todos_integrantes': todos_integrantes,
        }
        return render(request, 'integrantes.html', context)

class PaginaPrincipal(View):
    def get(self, request):
        # Filtra los eventos para mostrar solo aquellos con fecha igual o posterior a hoy
        eventos = Evento.objects.filter(fecha__gte=now().date()).order_by('fecha')
        noticias = Noticia.objects.order_by('-fecha')  # Obtén todas las novedades ordenadas por fecha descendente
        context = {
            'eventos': eventos,
            'noticias': noticias,
        }
        return render(request, 'index.html', context)

class Nosotros(View):
    def get(self, request):
        todos_integrantes = Integrante.objects.all()
        nuestras_obras = Obra.objects.all()
        context = {
            'todos_integrantes': todos_integrantes,
            'nuestras_obras': nuestras_obras, 
        }
        return render(request, 'nosotros.html', context)

class NuestraHistoria(View):
    def get(self, request):
        context = {}
        return render(request, 'nuestraHistoria.html', context)

class Galeria(View):
    def get(self, request):
        obras = Obra.objects.all()  # Obtiene todas las obras de la BD
        context = {'obras': obras}  # Agrega la variable al contexto
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
        instituciones_beneficiadas = Institucion.objects.all()
        context = {
            'instituciones_beneficiadas': instituciones_beneficiadas,
        }
        return render(request, 'impactoSocial.html', context)

class Novedades(View):
    def get(self, request):
        noticias = Noticia.objects.order_by('-fecha')
        context = {
            'noticias': noticias,
        }
        return render(request, 'novedades.html', context)

class Novedad(View):
    def get(self, request,id):
        noticia = get_object_or_404(Noticia, id_noticia=id)
        context = {
            'noticia': noticia,
        }
        return render(request, 'novedad.html', context)

class ImpactoSocialInsti(View):
    def get(self, request, id):
            institucion = get_object_or_404(Institucion, id=id)
            context = {
            'institucion': institucion,
            }
            return render(request, 'impactoSocial-Insti.html', context)

class ImpactoSocialGaleria(View):
    def get(self, request):
        context = {}
        return render(request, 'impactoSocial-Galeria.html', context)

class DetalleObra(View):
    def get(self, request, id):
        obra = get_object_or_404(Obra, id=id)
        context = {
            'obra': obra,
        }
        return render(request, 'obra.html', context)
