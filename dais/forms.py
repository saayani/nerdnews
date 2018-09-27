from django import forms


class SignupForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = 'Username',
        max_length = 32
    )
    email = forms.CharField(
        required = True,
        label = 'Email',
        max_length = 32,
    )
    password = forms.CharField(
        required = True,
        label = 'Password',
        max_length = 32,
        widget = forms.PasswordInput()
    )


class SubmitForm(forms.Form):
    title = forms.CharField(
        required = True,
        label = 'Title',
        max_length = 255
    )
    url = forms.CharField(
        required = True,
        label = 'URL',
        max_length = 200,
    )
