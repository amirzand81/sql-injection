from django.urls import path
from .views import login_view, search_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('search/', search_view, name='search'),
]
