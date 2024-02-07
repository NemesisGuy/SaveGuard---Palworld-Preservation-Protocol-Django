# saveguard_app/urls.py

from django.urls import path
from . import views
from .views import backup_now  # Import the backup_now view
from .views import backup_status


urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),  # Example settings URL
    path('backup-status/', views.backup_status, name='backup_status'),  # Define the backup_status URL pattern
    path('backup/', backup_now, name='backup_now'),
    

    # Add other URL patterns here
]
