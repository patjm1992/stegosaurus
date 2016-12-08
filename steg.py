import cv2
import numpy as np

'''
Hiding the text inside the image:

    Loop through the pixels of the image. In each iteration, get the RGB values
    separated each in a separate integer. For each of R, G, and B, make the LSB
    equal to 0. These bits will be used in hiding characters. Get the current
    character and convert it to integer. Then hide its 8 bits in R1, G1, B1, R2,
    G2, B2, R3, G3, where the numbers refer to the numbers of the pixels. In each
    LSB of these elements (from R1 to G3), hide the bits of the character consecutively.
    When the 8 bits of the character are processed, jump to the next character, and
    repeat the process until the whole text is processed. The text can be hidden in a
    small part of the image according to the length of that text. So, there must be
    something to indicate that here we reached the end of the text. The indicator is
    simply 8 consecutive zeros. This will be needed when extracting the text from the
    image.

Extracting the text from the image:

	It's more simple than hiding. Just pass through the pixels of the image until
	you find 8 consecutive zeros. As you are passing, pick the LSB from each pixel
	element (R, G, B) and attach it into an empty value. When the 8 bits of this
	value are done, convert it back to character, then add that character to the
	result text you are seeking.
'''

def char_to_bits(c):
	return c





print(char_to_bits('a')


'''
# Read an image file into a variable
img = cv2.imread('mouse.png')

# shape of an image --> returns a tuple of (rows, cols, channel)
shape = img.shape

# dimentsions of the image
height = shape[0]
width = shape[1]

# Iterate through the image pixel-by-pixel
for i in range(0, width):
	for j in range(0, height):
		rgb = img[i][j]
		r, g, b = rgb[0], rgb[1], rgb[2]
		print("R", r, "G", g, "B", b)


'''