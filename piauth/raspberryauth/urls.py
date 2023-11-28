from django.urls import path
from . import views

urlpatterns = [
    path("", views.submit_code, name="submit_code"),
]
