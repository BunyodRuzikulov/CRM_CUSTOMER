from django.db import models

class Client(models.Model):
    STATUS_CHOICES = [
        ('faol', 'Faol'),
        ('passiv', 'Passiv'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    company = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='faol')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Notification(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    
    def __str__(self):
        return self.title

class Activity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='activities')
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.client} - {self.description}"