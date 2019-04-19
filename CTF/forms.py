from django import forms
from django.contrib.auth import authenticate, get_user_model


class SubmitForrm(forms.Form):
    answer = forms.CharField(widget=forms.TextInput(attrs={'class' : 't-input', "style" :  'border:1px solid #000000;'}))

    def clean(self, *args, **kwargs):
        answer = self.cleaned_data.get('answer')
        description = self.cleaned_data.get('description')

        return super().clean(*args, **kwargs)


User = get_user_model()