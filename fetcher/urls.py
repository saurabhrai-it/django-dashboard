from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('save/<int:buildNumber>/<loadtestPurpose>', views.savedata, name='savedata'),
    path('saveBaselineBuild/<int:buildNumber>/<int:baselineBuildNumber>', views.saveBaselineBuild, name='saveBaselineBuild'),
]