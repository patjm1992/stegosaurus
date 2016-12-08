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
    '''
        Given a character, 'c', return an array of the bits that represent the
        ASCII representation of that character.
        Example: 'a' --> 97 --> 01100001
    '''

    bit_array = []
    n_bits = 8

    for bit in range(n_bits - 1, -1, -1):
        ascii_rep = ord(c)
        bit_array.append((ascii_rep >> bit) & 1)

    return bit_array

def get_required_space(msg):
    '''
        Given a 'msg', return the number of pixels that will have to be accessed
        in order to hide this message.
    '''
    pass

def check_for_fit():
    pass

# Read an image file into a variable
img = cv2.imread('mouse.png')

# shape of an image --> returns a tuple of (rows, cols, channel)
shape = img.shape

# dimensions of the image
height = shape[0]
width = shape[1]

# Iterate through the image pixel-by-pixel
for i in range(0, width):
	for j in range(0, height):

        try:

            # R1, G1, B1
            rgb_1 = img[i][j]
    		r_1, g_1, b_1 = rgb_1[0], rgb_1[1], rgb_1[2]


            # R2, G2, B2
            rgb_2 = img[i + 1][j + 1]
            r_2, g_2, b_2 = rgb_2[0], rgb_2[1], rgb_2[2]


            # R3, G3 (B3 not needed)
            rgb_3 = img[i + 2][j + 2]
            r_3, g_3 = rgb_3[0], rgb_3[1]

        except IndexError:
            break



'''