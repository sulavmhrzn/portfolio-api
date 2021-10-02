from django.urls import path
from . import views

urlpatterns = [
    path("", views.UnderDevelopment.as_view()),
    path("api/", views.About.as_view()),
]
