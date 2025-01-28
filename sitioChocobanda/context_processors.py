from .models import AjustesPagina

def ajustes_pagina(request):
    ajustes = AjustesPagina.objects.first()
    return {'ajustes': ajustes}