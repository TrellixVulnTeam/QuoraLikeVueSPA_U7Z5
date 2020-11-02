from django.urls import path, include
from .views import UserList,AuthenticatedUser

app_name = "users-api"
urlpatterns = [
    path("user_list/", UserList.as_view(), name="user-list"),
    path("authenticated_user/", AuthenticatedUser.as_view(), name="authenticated-user"),


]
