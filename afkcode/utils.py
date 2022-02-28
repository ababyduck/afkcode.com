import PIL.Image
from django.core.files import File
from pathlib import Path
from PIL import Image
from io import BytesIO

IMAGE_TYPES = {
    'jpg':  'JPEG',
    'jpeg': 'JPEG',
    'png':  'PNG',
    'gif':  'GIF',
    'tif':  'TIFF',
    'tiff': 'TIFF'
}


# Image resize mixin based on code from the following blog:
# https://blog.soards.me/posts/resize-image-on-save-in-django-before-sending-to-amazon-s3/
def image_resize(image, width, height):
    # Open the image with Pillow
    img = Image.open(image)
    # If width or height are larger than the max
    if img.width > width or img.height > height:
        output_size = (width, height)
        # Create resized "thumbnail" version with Pillow (preserves aspect ratio)
        # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.thumbnail
        img.thumbnail(output_size, resample=PIL.Image.LANCZOS, reducing_gap=3.0)
        # Get filename and determine extension
        img_filename = Path(image.file.name).name
        img_suffix = Path(image.file.name).name.split('.')[-1]
        img_format = IMAGE_TYPES[img_suffix.lower()]
        # Save resized image to memory buffer
        buffer = BytesIO()
        img.save(buffer, format=img_format, optimize=True)
        # Buffer to File object, File object to disk. Result gets uploaded by django-storages
        file_object = File(buffer)
        image.save(img_filename, file_object)
