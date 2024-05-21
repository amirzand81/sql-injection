from django.urls import path
from .views import login_view, search_view, admin_panel

urlpatterns = [
    path('login/', login_view, name='login'),
    path('search/', search_view, name='search'),
    path('panel/', admin_panel, name='admin_panel'),
]
