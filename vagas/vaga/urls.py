from django.urls import path
from vagas.vaga import views

app_name = 'vaga'
urlpatterns = [
    path('<int:pk>', views.vaga, name='vaga'),
    path('', views.vagas, name='vagas'),
]
