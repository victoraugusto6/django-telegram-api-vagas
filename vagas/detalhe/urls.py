from django.urls import path
from vagas.detalhe import views

app_name = 'detalhe'
urlpatterns = [
    path('', views.home, name='home'),
]
