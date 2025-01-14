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

class NuestraHistoria(View):
    def get(self,request):
        context={

        }
        return render(request,'nuestraHistoria.html',context)

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
    

class contacto(View):
    def get(self,request):
        context={

        }
        return render(request,'contacto.html',context)


class impactosocial(View):
    def get(self,request):
        context={
            
        }   
        return render(request,'impactoSocial.html',context)
class novedades(View):
    def get(self,request):
        context={

        }
        return render(request,'novedades.html',context)

class novedad(View):
    def get(self,request):
        context={

        }
        return render(request,'novedad.html',context)
    
class impactoSocialInsti(View):
    def get(self,request):
        context={

        }
        return render(request,'impactoSocial-Insti.html',context)


class impactoSocialGaleria(View):
    def get(self,request):
        context={

        }
        return render(request,'impactoSocial-Galeria.html',context)

class integrantes(View):
    def get(self,request):
        context={

        }
        return render(request,'integrantes.html',context)
    
class detalleIntegrante(View):
    def get(self,request):
        context={

        }
        return render(request,'detalleIntegrante.html',context)