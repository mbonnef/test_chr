from django.urls import path
from seia import views

urlpatterns = [
    path('seia/', views.ver_proyectos, name='ver_proyectos'),
    path('seia/actualizar_proyectos',
         views.actualizar_proyectos, name='actualizar_proyectos')
]
