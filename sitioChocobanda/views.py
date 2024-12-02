from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

class PaginaPrincipal(View): 
    def get(self,request):
        context={

        }
        return render(request,'home.html',context)
    
class Nosotros(View): 
    def get(self,request):
        context={

        }
        return render(request,'nosotros.html',context)

class Galeria(View): 
    def get(self,request):
        context={

        }
        return render(request,'galeria.html',context)

class Login(View): 
    def get(self,request):
        context={

        }
        return render(request,'login.html',context)
    
class ContraseñaOlvidada(View):
    def get(self,request):
        context={

        }
        return render(request,'recuperarContraseña.html',context)

class Novedades(View):
    def get(self,request):
        context={

        }
        return render(request,'novedades.html',context)