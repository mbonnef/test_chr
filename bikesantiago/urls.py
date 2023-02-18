from django.urls import path
from bikesantiago import views

urlpatterns = [
    path('bikesantiago/', views.ver_estaciones, name='ver_estaciones'),
    path('bikesantiago/actualizar_estaciones/',
         views.actualizar_estaciones, name='actualizar_estaciones')

]
