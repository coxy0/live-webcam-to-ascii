from PIL import Image
import math

image_path = "test.jpg"
image = Image.open(image_path)
width, height = image.size
pixels = image.load()

character_map = 'Ñ@#W$986543210?!abc;:+=-,._ '[::-1]
def rgb_to_ascii(r, g, b):
    relative_luminance = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255
    index = relative_luminance * (len(character_map) - 1)
    return character_map[math.floor(index)]

to_print = ""
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        character = rgb_to_ascii(r, g, b)
        to_print += (character + " ")
    to_print += "\n"
print(to_print)
