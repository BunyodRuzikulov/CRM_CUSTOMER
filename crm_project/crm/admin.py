from django.contrib import admin
from .models import Client, Notification, Activity

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'status', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('status', 'created_at')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    search_fields = ('title', 'description')

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('client', 'description', 'created_at')
    search_fields = ('description',)
    list_filter = ('created_at',)