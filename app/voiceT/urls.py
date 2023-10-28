"""
URL mapping for the voiceT app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter
from . import views as voiceT_views

router = DefaultRouter()
router.register('voiceT', voiceT_views.AudioView)

app_name = 'voiceT'

urlpatterns = [
    path('', include(router.urls))
]
