from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TruckOrder
from .forms import TruckOrderForm, UserProfileForm
from django.utils import timezone

class TruckAppTests(TestCase):
    def setUp(self):
        # Set up a test user and client
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword', email='test@example.com')
        
        # Set up a sample order
        self.order = TruckOrder.objects.create(
            user=self.user,
            pickup_location='Warehouse A',
            delivery_location='Store B',
            shipment_size='20ft container',
            shipment_weight=5000.50,
            shipment_type='Electronics',
            pickup_time=timezone.now(),
            status='pending'
        )

    def test_model_creation(self):
        """Test that the TruckOrder model instances are created successfully."""
        self.assertEqual(TruckOrder.objects.count(), 1)
        self.assertEqual(self.order.pickup_location, 'Warehouse A')
        self.assertEqual(self.order.status, 'pending')
        self.assertEqual(str(self.order), f"Order #{self.order.id} by testuser - Pending")

    def test_home_page_view(self):
        """Test the home page loads correctly."""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'truck_app/home.html')

    def test_register_page_view(self):
        """Test the registration page loads."""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_dashboard_access_unauthenticated(self):
        """Test that unauthenticated users are redirected from the dashboard to login."""
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/login/'))

    def test_dashboard_access_authenticated(self):
        """Test that authenticated users can access the dashboard and see their stats."""
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'truck_app/dashboard.html')
        self.assertContains(response, 'Warehouse A')
        
        # Check if stats are in context
        self.assertIn('stats', response.context)
        self.assertEqual(response.context['stats']['total'], 1)

    def test_create_order_view(self):
        """Test the create order form submission."""
        self.client.login(username='testuser', password='testpassword')
        
        # Test GET request
        response = self.client.get(reverse('create_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'truck_app/create_order.html')

        # Test POST request
        future_time = timezone.now() + timezone.timedelta(days=1)
        data = {
            'pickup_location': 'City Center',
            'delivery_location': 'Suburbs',
            'shipment_size': 'Small box',
            'shipment_weight': '50',
            'shipment_type': 'Fragile',
            'pickup_time': future_time.strftime('%Y-%m-%dT%H:%M')
        }
        
        post_response = self.client.post(reverse('create_order'), data)
        self.assertEqual(post_response.status_code, 302) # Redirects to dashboard
        self.assertEqual(TruckOrder.objects.count(), 2)

    def test_profile_view_and_update(self):
        """Test the profile page and form submission."""
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'truck_app/profile.html')

        # Update profile
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'newemail@example.com'
        }
        post_response = self.client.post(reverse('profile'), data)
        self.assertEqual(post_response.status_code, 302) # Redirects back to profile
        
        # Refresh user from DB
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.email, 'newemail@example.com')

    def test_truck_order_form_validation(self):
        """Test the order form validation."""
        data = {
            'pickup_location': '', # Missing required field
            'delivery_location': 'Store B',
            'shipment_size': '20ft container',
            'shipment_weight': 'invalid', # Invalid decimal
            'shipment_type': 'Electronics',
            'pickup_time': 'invalid-date'
        }
        form = TruckOrderForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('pickup_location', form.errors)
        self.assertIn('shipment_weight', form.errors)
        self.assertIn('pickup_time', form.errors)
