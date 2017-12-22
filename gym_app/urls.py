from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logged/', views.ficha, name="index_logged"),
    path('logged/reservas', views.reservas, name="reservas"),
    path('logged/horario', views.horario, name="horario"),
    path('logged/asistencias', views.asistencias, name="asistencias")
]