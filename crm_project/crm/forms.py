from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone', 'email', 'company', 'status', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
            'status': forms.Select(choices=Client.STATUS_CHOICES),
        }