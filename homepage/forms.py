from django import forms
from homepage.models import Text_line


class TextForm(forms.Form):
    Text = forms.CharField(max_length=240)
