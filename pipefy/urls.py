from django.urls import path
from pipefy.views import index, submit

urlpatterns = [
    path('', index, name="index" ),
    path('submit', submit, name="submit")
]