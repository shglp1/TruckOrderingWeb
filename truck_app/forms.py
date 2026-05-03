from django import forms
from django.contrib.auth.models import User
from .models import TruckOrder

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

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
            'pickup_location': forms.TextInput(attrs={'class': 'form-input'}),
            'delivery_location': forms.TextInput(attrs={'class': 'form-input'}),
            'shipment_size': forms.TextInput(attrs={'class': 'form-input'}),
            'shipment_weight': forms.NumberInput(attrs={'class': 'form-input'}),
            'shipment_type': forms.TextInput(attrs={'class': 'form-input'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }
