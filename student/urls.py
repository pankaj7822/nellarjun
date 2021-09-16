from .views import getnotice
from django.urls import include, path
urlpatterns = [
    path('getnotice', getnotice),
]