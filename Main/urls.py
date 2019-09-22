
from django.urls import path
from . import views as view

urlpatterns = [
    path('', view.show, name='home'),
]
