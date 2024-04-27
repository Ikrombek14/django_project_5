from .views import first_func,second_func
from django.urls import path


urlpatterns = [
    path('1', first_func),
    path('2', second_func),
]