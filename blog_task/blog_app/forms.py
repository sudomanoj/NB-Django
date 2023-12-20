from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, UsernameField
from django.contrib.auth.models import User
from blog_app.models import Post

class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        label = {'first_name':'First Name', 'last_name':'Last Name', 'email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class': 'form-control'}),
                   'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name':forms.TextInput(attrs={'class': 'form-control'}),
                   'email':forms.EmailInput(attrs={'class': 'form-control'})
                   }

class LoginForm(AuthenticationForm):
    username = UsernameField(label = 'Username', widget=forms.TextInput(attrs={"autofocus": True, 'class':'form-control'}))
    password = forms.CharField(
        label= "Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", 'class':'form-control'}),
    )
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title':'Title', 'content':'Content'}
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'content':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Content'})
                   }
        