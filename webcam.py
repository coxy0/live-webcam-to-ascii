import math
import cv2
import imutils
import os

character_map = 'Ñ@#W$986543210?!abc;:+=-,._ '[::-1]
def rgb_to_ascii(r, g, b):
    relative_luminance = 0.000833725490196 * r + 0.00280470588235 * g + 0.000283137254902 * b
    index = math.floor(relative_luminance * (len(character_map) - 1))
    return character_map[index]


capture = cv2.VideoCapture(0)
while 1:
    ret, frame = capture.read()
    if not ret:
        break

    frame = imutils.resize(cv2.flip(frame, 1), width=84)
    height, width, channels = frame.shape
    characters = ''
    for y in range(height):
        for x in range(width):
            try:
                b, g, r = frame[y, x]
                character = rgb_to_ascii(r, g, b)
                characters += (character + ' ')
            except IndexError:
                characters += ' '
        characters += '\n'
    print(characters)
    # os.system('cls')

