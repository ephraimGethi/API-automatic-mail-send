from django.urls import path
from .views import MyView
urlpatterns = [
    path('',MyView),
]