from django.urls import path
from .views import ItemCreateAPIView

urlpatterns = [
    path('create-item/', ItemCreateAPIView.as_view(), name='create-item'),
]
