from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("create/", views.board_create, name="create"),  
    path("<int:board_id>/", views.detail, name="detail"),
]