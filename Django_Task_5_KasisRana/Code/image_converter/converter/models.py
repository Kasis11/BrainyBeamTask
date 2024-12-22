from django.db import models

class Image(models.Model):
    original_image = models.ImageField(upload_to='images/originals/')
    converted_image = models.ImageField(upload_to='images/converted/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"
