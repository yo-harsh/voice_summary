from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import serializers
from core.models import AudioFile
from rest_framework import status
from rest_framework.response import Response
import openai
from django.shortcuts import get_object_or_404
from dotenv import load_dotenv
import os


class AudioView(viewsets.ModelViewSet):
    serializer_class = serializers.AudioSerializer
    queryset = AudioFile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        file_serializer = serializers.AudioSerializer(data=request.data)

        if file_serializer.is_valid():
            file_serializer.save()
        text = self.process_audio(file_serializer.instance.pk)

        # You can now return the processed text in the response
        return Response({"data": text}, status=status.HTTP_201_CREATED)

    def process_audio(self, pk):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        print(openai.api_key)
        audio = get_object_or_404(AudioFile, pk=pk)

        # Get the absolute file path of the audio file
        audio_file_path = audio.file.path

        audio_data = open(audio_file_path, 'rb')

        # Pass the binary audio data to openai.Audio.transcribe
        transcript = openai.Audio.transcribe("whisper-1", audio_data)

        # Do something with the transcript

        return transcript


