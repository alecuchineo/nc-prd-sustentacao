from django.urls import path
from pipefy.views import index

urlpatterns = [
    path('', index )
]