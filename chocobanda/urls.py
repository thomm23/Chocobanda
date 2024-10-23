
from django.contrib import admin
from django.urls import path
from sitioChocobanda.views import PaginaPrincipal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PaginaPrincipal.as_view(), name="home")
]
