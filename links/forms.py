__author__ = 'niemand'

from django.forms import ModelForm, HiddenInput

from links.models import Link

class LinkForm(ModelForm):
    class Meta:
        model = Link
        fields = ['link', 'description']