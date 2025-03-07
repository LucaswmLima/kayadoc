from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_medicos, name='lista_medicos'),
    path('<int:id>/perfil/', views.perfil_medico, name='perfil_medico'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
