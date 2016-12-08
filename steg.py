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
def extract():
    pass

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



def flip_lsb(val, b):
    '''
        If b == 0 --> make the LSB of 'val' a 1,
        If b == 1 --> make the LSB of 'val' a 0

        Return the modified bitstring
    '''

    return bin((val & ~1) | b)


def produce_bitmask(val):
    '''
        Return a bitmask of the appropriate length, given val.

        EX:
            bits -> 0b10101010
            mask -> 0b00000001
    '''

    bit_len = len(bin(ord(chr(val))))

    # Build the mask as a string
    mask = '0b'
    for i in range(bit_len - 3):
        mask += '0'
    mask += '1'

    return int(mask, 2)


def access_lsb(val):
    b = ord(chr(val))
    bitmask = produce_bitmask(val)

    return b & bitmask

def inject_bit(b, val):
    '''
        Put the bit, 'b' in the LSB position of 'val'.

            EX:
                r_1 = 255 = 0b11111111
                b = 0

                ------
                RESULT:
                    0b11111110

        Return the modified bitstring with the new bit 'injected'.
    '''

    lsb = access_lsb(val)

    if (b == lsb):
        # No work to be done
        return bin(val)
    elif (b == 1):
        return flip_lsb(val, b)
    elif (b == 0):
        return flip_lsb(val, b)


def main():

    msg = 'hi'


    w = 1000
    h = 1000

    # make a fake 'image'
    img = [[(255, 255, 255) for x in range(w)] for y in range(h)]

'''
    for i in range(w):
        for j in range(h):
            print(img[i][j])
'''

    i = 0
    j = 0

    for c in msg:

        try:
            px_1, px_2, px_3 = img[i][j], img[i + 1][j + 1], img[i + 2][j + 2]
        except IndexError:
            break

        # All the space we need for an 8-bit character
        R1, G1, B1 = px_1[0], px_1[1], px_1[2]
        R2, G2, B2 = px_2[0], px_2[1], px_2[2]
        R3, G3 = px_3[0], px_3[1]



        i += 1
        j += 1



if __name__ == '__main__':
    main()


'''
def inject_msg(msg, img):
    shape = image.shape
    height = shape[0]
    width = shape[1]

    for i in range(0, width):
        for j in range(0, height):

        # R1, G1, B1
        rgb_1 = img[i][j]
        r_1, g_1, b_1 = rgb_1[0], rgb_1[1], rgb_1[2]


        # R2, G2, B2
        rgb_2 = img[i + 1][j + 1]
        r_2, g_2, b_2 = rgb_2[0], rgb_2[1], rgb_2[2]


        # R3, G3 (B3 not needed)
        rgb_3 = img[i + 2][j + 2]
        r_3, g_3 = rgb_3[0], rgb_3[1]

        char_bits = char_to_bits(msg[i])





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

        # R1, G1, B1
        rgb_1 = img[i][j]
		r_1, g_1, b_1 = rgb_1[0], rgb_1[1], rgb_1[2]


        # R2, G2, B2
        rgb_2 = img[i + 1][j + 1]
        r_2, g_2, b_2 = rgb_2[0], rgb_2[1], rgb_2[2]


        # R3, G3 (B3 not needed)
        rgb_3 = img[i + 2][j + 2]
        r_3, g_3 = rgb_3[0], rgb_3[1]



'''