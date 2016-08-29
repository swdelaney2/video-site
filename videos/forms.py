from django import forms
from django.forms import ModelForm
from .models import Video

class AddVideoForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = Video
        fields = "__all__"
