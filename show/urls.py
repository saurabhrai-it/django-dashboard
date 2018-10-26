from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:buildNumber>', views.showdata, name='showdata'),
]