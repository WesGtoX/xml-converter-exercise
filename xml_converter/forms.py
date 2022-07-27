from django import forms
from django.core.validators import FileExtensionValidator


class XMLFileForm(forms.Form):
    file = forms.FileField(allow_empty_file=False, validators=[FileExtensionValidator(allowed_extensions=['xml'])])
