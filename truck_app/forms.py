from django import forms
from django.contrib.auth.models import User
from .models import TruckOrder
from django.utils import timezone

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("This username is already taken. Please choose another one.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("A user with this email already exists. Please use a different email.")
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password and len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords don't match")
        return password_confirm

class TruckOrderForm(forms.ModelForm):
    pickup_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M']
    )
    delivery_time = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
        required=False
    )

    class Meta:
        model = TruckOrder
        fields = [
            'pickup_location', 'delivery_location', 'shipment_size',
            'shipment_weight', 'shipment_type', 'pickup_time', 'delivery_time'
        ]
        widgets = {
            'pickup_location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Warehouse A'}),
            'delivery_location': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Port Terminal B'}),
            'shipment_size': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. 20ft Container'}),
            'shipment_weight': forms.NumberInput(attrs={'class': 'form-input', 'placeholder': 'Weight in kg'}),
            'shipment_type': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'e.g. Electronics, Perishables'}),
        }

    def clean_shipment_weight(self):
        weight = self.cleaned_data.get('shipment_weight')
        if weight is not None and weight <= 0:
            raise forms.ValidationError("Shipment weight must be a positive number.")
        return weight

    def clean_pickup_time(self):
        pickup_time = self.cleaned_data.get('pickup_time')
        if pickup_time and pickup_time < timezone.now():
            raise forms.ValidationError("Pickup time cannot be in the past.")
        return pickup_time

    def clean_delivery_time(self):
        pickup_time = self.cleaned_data.get('pickup_time')
        delivery_time = self.cleaned_data.get('delivery_time')
        
        if pickup_time and delivery_time and delivery_time <= pickup_time:
            raise forms.ValidationError("Delivery time must be after the pickup time.")
        return delivery_time

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email
