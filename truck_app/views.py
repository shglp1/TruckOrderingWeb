from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import UserRegistrationForm, TruckOrderForm, UserProfileForm
from .models import TruckOrder

def home(request):
    return render(request, 'truck_app/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect('/admin/')
        
    orders = request.user.orders.all().order_by('-created_at')
    stats = {
        'total': orders.count(),
        'pending': orders.filter(status='pending').count(),
        'in_progress': orders.filter(status='in_progress').count(),
        'delivered': orders.filter(status='delivered').count(),
    }
    return render(request, 'truck_app/dashboard.html', {'orders': orders, 'stats': stats})

@login_required
def create_order(request):
    if request.user.is_staff:
        return redirect('/admin/')

    if request.method == 'POST':
        form = TruckOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            
            # Send email to admin
            send_mail(
                subject=f'New Truck Order #{order.id}',
                message=f'A new truck order has been placed by {request.user.username}.\n\nPickup: {order.pickup_location}\nDelivery: {order.delivery_location}',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL], # sending to admin
                fail_silently=True,
            )
            return redirect('dashboard')
    else:
        form = TruckOrderForm()
    return render(request, 'truck_app/create_order.html', {'form': form})

@login_required
def profile(request):
    if request.user.is_staff:
        return redirect('/admin/')

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'truck_app/profile.html', {'form': form})
