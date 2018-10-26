from django.urls import path

from . import views

urlpatterns = [
    path('<int:currBuildNumber>/<int:baseBuildNumber>', views.compareData, name='compareData'),
]