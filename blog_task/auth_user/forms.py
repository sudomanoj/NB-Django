from django import forms

class OTPForm(forms.Form):
    otp_code = forms.CharField(max_length=6, min_length=6, widget=forms.TextInput(attrs={'autocomplete': 'off'}))
