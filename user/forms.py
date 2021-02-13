from django import forms

from .models import User

class SignInForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('full_name', 'email', 'password')

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'input'}),
            'email': forms.TextInput(attrs={'class':'input'}),
            'password': forms.TextInput(attrs={'class':'input'}),
        }
class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('email', 'password')

        widgets = {
            'email': forms.TextInput(attrs={'class':'input'}),
            'password': forms.TextInput(attrs={'class':'input'}),
        }