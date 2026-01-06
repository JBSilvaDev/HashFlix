from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Usuario

class CreateAccountForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "email", "username"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-black rounded-md p-2 w-full'

class EditProfileForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "email"]
        
    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields.pop('password', None)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-black rounded-md p-2 w-full'

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text-black rounded-md p-2 w-full'
