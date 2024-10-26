
from django.contrib import admin
from django.urls import path
from sitioChocobanda.views import PaginaPrincipal, Galeria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaPrincipal.as_view(), name="home"),
    path('galeria/', Galeria.as_view(), name="galeria")
]
