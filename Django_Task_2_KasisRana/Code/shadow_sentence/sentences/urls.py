from django.urls import path
from . import views

urlpatterns = [
    path('shadow-sentence/', views.shadow_sentence_view, name='shadow_sentence'),
]
