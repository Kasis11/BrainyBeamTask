from django.shortcuts import render
import random
from django.http import JsonResponse

def generate_shadow_sentence(request):
    # Get character length from request (e.g., ?length=50)
    char_length = int(request.GET.get('length', 50))
    
    # Example word pool (extend this for better variety)
    word_pool = ["cat", "dog", "apple", "orange", "mouse", "tree", "river", "cloud", "shadow", "earth", "star"]
    
    # Function to pick a random word of a specific length
    def find_word_of_length(length):
        same_length_words = [word for word in word_pool if len(word) == length]
        if same_length_words:
            return random.choice(same_length_words)
        return None  # Return None if no word of the required length is found

    # Example input sentence (replace this with user input if needed)
    input_sentence = "Hello world, this is Django!"

    # Generate shadow sentence
    shadow_sentence = []
    for word in input_sentence.split():
        clean_word = word.strip(",.!?")  # Remove punctuation for length matching
        shadow_word = find_word_of_length(len(clean_word))
        if shadow_word:
            # Add back punctuation if present
            shadow_sentence.append(shadow_word + (word[-1] if word[-1] in ",.!?" else ""))
        else:
            # Keep original word if no match found
            shadow_sentence.append(word)

    # Combine words into a sentence and trim to character length
    final_sentence = " ".join(shadow_sentence)[:char_length]
    return JsonResponse({"shadow_sentence": final_sentence})
