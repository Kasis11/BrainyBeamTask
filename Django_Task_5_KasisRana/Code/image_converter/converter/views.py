from django.shortcuts import render, redirect
from .forms import ImageForm
from .models import Image
from PIL import Image as PILImage
import os

def convert_to_black_and_white(image_path):
    # Define the path for the converted image
    bw_image_path = image_path.replace('originals', 'converted')

    # Ensure the 'converted' directory exists
    converted_dir = os.path.dirname(bw_image_path)
    if not os.path.exists(converted_dir):
        os.makedirs(converted_dir)

    # Convert the image to grayscale and save
    img = PILImage.open(image_path).convert('L')
    img.save(bw_image_path)

    return bw_image_path

def upload_image(request):
    if request.method == 'POST' and request.FILES['original_image']:
        # Handle image upload
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()

            # Convert to black and white
            original_image_path = image.original_image.path
            converted_image_path = original_image_path.replace('originals', 'converted')

            # Ensure the 'converted' directory exists
            converted_dir = os.path.dirname(converted_image_path)
            if not os.path.exists(converted_dir):
                os.makedirs(converted_dir)

            # Convert the image
            img = PILImage.open(original_image_path).convert('L')
            img.save(converted_image_path)

            # Save the path to the converted image in the model
            image.converted_image = converted_image_path
            image.save()

            return render(request, 'converter/upload.html', {'image': image})

    else:
        form = ImageForm()
    return render(request, 'converter/upload.html', {'form': form})


def view_images(request):
    images = Image.objects.all()
    return render(request, 'converter/view_images.html', {'images': images})
