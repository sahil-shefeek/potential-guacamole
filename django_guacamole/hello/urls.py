from django.urls import path
from . import views

urlpatterns = [
    path("",views.hello,name = "hello"),
    path("<str:name>",views.greet_user,name = "greet"),
    path("greet/<str:username>",views.welcome_user,name = "welcome"),
]