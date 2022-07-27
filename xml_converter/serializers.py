from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class XMLFileSerializer(serializers.Serializer):
    file = serializers.FileField(allow_empty_file=False, validators=[FileExtensionValidator(allowed_extensions=['xml'])])

    class Meta:
        fields = ('file',)
