from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Client, Notification, Activity
from django.db.models import Q
from datetime import datetime
from .forms import ClientForm

def index(request):
    total_clients = Client.objects.count()
    active_clients = Client.objects.filter(status='faol').count()
    new_clients = Client.objects.filter(created_at__gte=datetime.now().date()).count()
    recent_clients = Client.objects.order_by('-created_at')[:5]
    return render(request, 'index.html', {
        'total_clients': total_clients,
        'active_clients': active_clients,
        'new_clients': new_clients,
        'recent_clients': recent_clients
    })

def clients_list(request):
    search_term = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    date_filter = request.GET.get('date', '')
    
    clients = Client.objects.all()
    
    if search_term:
        clients = clients.filter(
            Q(first_name__icontains=search_term) |
            Q(last_name__icontains=search_term)
        )
    if status_filter:
        clients = clients.filter(status=status_filter)
    if date_filter:
        clients = clients.filter(created_at__date=date_filter)
    
    return render(request, 'clients.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        client = Client(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            company=request.POST.get('company', ''),
            status=request.POST['status'],
            notes=request.POST.get('notes', '')
        )
        client.save()
        Activity.objects.create(client=client, description="Mijoz ro‘yxatga qo‘shildi")
        messages.success(request, "Mijoz muvaffaqiyatli qo‘shildi!")
        return redirect('clients_list')
    return render(request, 'add_client.html')

def client_profile(request, id):
    client = get_object_or_404(Client, id=id)
    return render(request, 'client-profile.html', {'client': client})

def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.first_name = request.POST['first-name']
        client.last_name = request.POST['last-name']
        client.phone = request.POST['phone']
        client.email = request.POST['email']
        client.company = request.POST.get('company', '')
        client.status = request.POST['status']
        client.notes = request.POST.get('notes', '')
        client.save()
        Activity.objects.create(client=client, description="Mijoz ma'lumotlari yangilandi")
        messages.success(request, "Mijoz ma'lumotlari yangilandi!")
        return redirect('client_profile', id=id)
    return render(request, 'edit_client.html', {'client': client})

def delete_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.delete()
        messages.success(request, "Mijoz o‘chirildi!")
        return redirect('clients_list')
    return JsonResponse({'error': 'Invalid request'}, status=400)

def notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'notifications.html', {'notifications': notifications})

def delete_notification(request, id):
    notification = get_object_or_404(Notification, id=id)
    if request.method == 'POST':
        notification.delete()
        messages.success(request, "Eslatma o‘chirildi!")
        return redirect('notifications')
    return JsonResponse({'error': 'Invalid request'}, status=400)

def settings(request):
    if request.method == 'POST':
        language = request.POST.get('language', 'uz')
        background_color = request.POST.get('background-color', '#f3f4f6')
        request.session['language'] = language
        request.session['background_color'] = background_color
        messages.success(request, "Sozlamalar saqlandi!")
        return redirect('settings')
    return render(request, 'settings.html')

from .forms import ClientForm

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            Activity.objects.create(client=client, description="Mijoz ro‘yxatga qo‘shildi")
            messages.success(request, "Mijoz muvaffaqiyatli qo‘shildi!")
            return redirect('clients_list')
    else:
        form = ClientForm()
    return render(request, 'add-client.html', {'form': form})

def edit_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            Activity.objects.create(client=client, description="Mijoz ma'lumotlari yangilandi")
            messages.success(request, "Mijoz ma'lumotlari yangilandi!")
            return redirect('client_profile', id=id)
    else:
        form = ClientForm(instance=client)
    return render(request, 'edit-client.html', {'form': form, 'client': client})