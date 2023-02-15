from PIL import Image

image = Image.open("/upload/astronaut.png")
image.thumbnail(400,400)
image.save('image_resize.png')
print(image.size)