from django.urls import path
from blogserver import views

urlpatterns = [
    path("", views.home, name="home"),
]
