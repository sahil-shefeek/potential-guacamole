from django.urls import path
from . import views

urlpatterns = [
    path("",views.hello,name = 'hello'),
    path("<str:name>",views.greetUser,name = 'greet')
]