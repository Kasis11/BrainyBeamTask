from django.shortcuts import render
from django.http import JsonResponse
import random
# Create your views here.
def generate_shadow_sentence(char_length):
    """
    Generate a shadow sentence of the specified character length.
    """
    # Example word list (you can expand this with your own dataset)
    words = ["cat", "dog", "fox", "bat", "owl", "ant", "rat", "bee", "cow", "pig"]

    # Keep generating random sentences until we match the target length
    while True:
        sentence = " ".join(random.choices(words, k=random.randint(1, char_length // 2)))
        if len(sentence) == char_length:
            return sentence

def shadow_sentence_view(request):
    """
    Django view to generate a shadow sentence.
    """
    char_length = int(request.GET.get('length', 10))  # Default length is 10
    shadow_sentence = generate_shadow_sentence(char_length)
    return JsonResponse({'shadow_sentence': shadow_sentence})