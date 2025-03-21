from django.contrib.auth.forms import UserCreationForm
from usuarios_app.models import Usuario


class RegistroForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'age', 'bio']
    
