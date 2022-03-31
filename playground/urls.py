from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('wish/', views.wish_birthday),
]