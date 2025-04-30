from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients_list, name='clients_list'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/<int:id>/', views.client_profile, name='client_profile'),
    path('clients/<int:id>/edit/', views.edit_client, name='edit_client'),
    path('clients/<int:id>/delete/', views.delete_client, name='delete_client'),
    path('notifications/', views.notifications, name='notifications'),
    path('notifications/<int:id>/delete/', views.delete_notification, name='delete_notification'),
    path('settings/', views.settings, name='settings'),
]