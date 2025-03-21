from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from sitioChocobanda.views import *
from sitioChocobanda import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaPrincipal.as_view(), name="home"),
    path('nosotros/', Nosotros.as_view(), name="nosotros"),
    path('nuestraHistoria/', NuestraHistoria.as_view(), name="nuestraHistoria"),
    path('galeria/', Galeria.as_view(), name="galeria"),
    # path('login/', Login.as_view(), name="login"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('contraseñaOlvidada/', ContraseñaOlvidada.as_view(), name="contraseñaOlvidada"),
    path('contacto/', Contacto.as_view(), name="contacto"),
    path('impactoSocial/', ImpactoSocial.as_view(), name='impactoSocial'),
    path('novedades/', Novedades.as_view(), name="novedades"),
    path('novedades/<int:id>/', Novedad.as_view(), name="novedad"),
    path('impactoSocial/', ImpactoSocial.as_view(), name='impactoSocial'),
    path('impactoSocialInsti/<int:id>/', ImpactoSocialInsti.as_view(), name='impactoSocialInsti'),
    path('impactoSocialGaleria/', ImpactoSocialGaleria.as_view(), name="impactoSocialGaleria"),
    path('integrantes/', Integrantes.as_view(), name='integrantes'),
    path('integrantes/<int:id>/', detalleIntegrante.as_view(), name="detalleIntegrante"),
    path('obra/<int:id>/', DetalleObra.as_view(), name='detalle_obra')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)