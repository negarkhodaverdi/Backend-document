from django.urls import path
from api import views

urlpatterns = [
    path("todo/", views.ListView.as_view()),
    path("todo/add/", views.AddView.as_view()),
    path("todo/remove/", views.RemoveView.as_view()),
]
