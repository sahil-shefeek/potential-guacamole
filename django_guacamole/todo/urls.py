from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.show, name = "index"),
    path("new", views.new, name="new"),
]