from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


app_name = "users"

urlpatterns = [
    path("register", views.register, name="register"),
    path("update_profile", views.update_profile, name="update_profile")

]
