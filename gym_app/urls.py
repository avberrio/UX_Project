from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('logged/', views.ficha, name="index_logged")
]