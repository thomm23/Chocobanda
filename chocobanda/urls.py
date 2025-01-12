
from django.contrib import admin
from django.urls import path
from sitioChocobanda.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaPrincipal.as_view(), name="home"),
    path('nosotros/', Nosotros.as_view(), name="nosotros"),
    path('nuestraHistoria/', NuestraHistoria.as_view(), name="nuestraHistoria"),
    path('galeria/', Galeria.as_view(), name="galeria"),
    path('login/', Login.as_view(), name="login"),
    path('contraseñaOlvidada/', ContraseñaOlvidada.as_view(), name="contraseñaOlvidada"),  
    path('contacto/', contacto.as_view(), name="contacto"),
    path ('impactoSocial/',impactosocial.as_view(),name='impactoSocial'),
    path('novedades/', novedades.as_view(), name="novedades"),
    path('novedad/', novedad.as_view(), name="novedad"),
    path('impactoSocialInsti', impactoSocialInsti.as_view(),name="impactoSocialInsti"),
    path('impactoSocialGaleria', impactoSocialGaleria.as_view(),name="impactoSocialGaleria"),
    path('obra/', Obra.as_view(),name="obra"),

]
