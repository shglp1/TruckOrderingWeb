from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

class EmailOrUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
            
        # Try to find the user by username first
        users = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username))
        
        for user in users:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        
        if not users:
            # Run the default password hasher once to reduce the timing difference
            UserModel().set_password(password)
            
        return None
