from django.urls import path
from .views import create_user , read_user , update_user , delete_user

urlpatterns = [
    path("create/", create_user),
    path("read/" , read_user),
    path("update/", update_user),
    path("delete/" , delete_user),
]