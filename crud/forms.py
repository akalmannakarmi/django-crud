from django.forms import ModelForm
from . import models

class InfoForm(ModelForm):
    class Meta:
        model = models.Info
        fields = ['firstName', 'middleName', 'lastName', 'dob', 'address']