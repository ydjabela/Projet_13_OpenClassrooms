from django.urls import path
from . import views

app_name = 'homes'

urlpatterns = [
    path('', views.index, name='homes_index'),
]
