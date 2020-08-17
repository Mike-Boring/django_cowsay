from django import forms
from homepage.models import Text_line


class TextForm(forms.Form):
    user_text = forms.CharField(max_length=240)
