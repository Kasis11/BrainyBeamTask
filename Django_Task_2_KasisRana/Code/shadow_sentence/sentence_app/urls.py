from django.urls import path
from .views import generate_shadow_sentence

urlpatterns = [
    path('shadow-sentence/', generate_shadow_sentence, name='shadow_sentence'),
]
