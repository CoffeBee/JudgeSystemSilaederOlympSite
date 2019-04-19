from django import forms
from django.contrib.auth import authenticate, get_user_model


class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'style' : 'background-color : transparent', 'class' : 'tn-atom', 'field' : 'tn_text_1555101043582'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'style' : 'background-color : transparent', 'class' : 'tn-atom', 'field' : 'tn_text_1555101043582'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Вы не зарегистрированы ;(')
            if not user.check_password(password):
                raise forms.ValidationError('Вы забыли пароль')
            if not user.is_active:
                raise forms.ValidationError('Вы слегка за бортом')
        return super().clean(*args, **kwargs)


User = get_user_model()