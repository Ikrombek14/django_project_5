from django.urls import path

from .views import get_inform, return_inform

urlpatterns = [
    path('inform/', get_inform, name='get_inform'),
    path('inform/return/', return_inform, name='return_inform'),
]