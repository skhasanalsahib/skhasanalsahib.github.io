import requests
from PIL import Image

def resize_image(image_url, new_width, new_height):
  """Resizes an image and returns the resized image."""
  # Get the image from the URL.
  response = requests.get(image_url)
  image = Image.open(response.content)

  # Resize the image.
  image = image.resize((new_width, new_height))

  # Return the resized image.
  return image

def crop_image(image_url, x, y, width, height):
  """Crops an image and returns the cropped image."""
  # Get the image from the URL.
  response = requests.get(image_url)
  image = Image.open(response.content)

  # Crop the image.
  image = image.crop((x, y, x + width, y + height))

  # Return the cropped image.
  return image

def rotate_image(image_url, angle):
  """Rotates an image and returns the rotated image."""
  # Get the image from the URL.
  response = requests.get(image_url)
  image = Image.open(response.content)

  # Rotate the image.
  image = image.rotate(angle)

  # Return the rotated image.
  return image

def save_image(image, filename):
  """Saves an image to a file."""
  image.save(filename)

def process_image():
  # Get the image URL from the user.
  image_url = input('Enter the image URL: ')

  # Get the new width and height from the user.
  new_width = int(input('Enter the new width: '))
  new_height = int(input('Enter the new height: '))

  # Resize the image.
  resized_image = resize_image(image_url, new_width, new_height)

  # Crop the image.
  cropped_image = crop_image(image_url, 100, 100, 100, 100)

  # Rotate the image.
  rotated_image = rotate_image(image_url, 90)

  # Save the resized image.
  save_image(resized_image, 'resized_image.png')

  # Save the cropped image.
  save_image(cropped_image, 'cropped_image.png')

  # Save the rotated image.
  save_image(rotated_image, 'rotated_image.png')

if __name__ == '__main__':
  process_image()
