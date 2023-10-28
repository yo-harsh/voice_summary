from core.models import AudioFile
from rest_framework import serializers


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = AudioFile
        fields = [
            'id', 'file'
        ]
        read_only_fields = ['id']
        extra_kwargs = {'file': {'required': 'True'}}
