import cv2
import numpy as np
import argparse

'''
    Quick prototype of a steganography program.
'''


def extract():
    '''
        to-do
    '''
    pass

def char_to_bits(c):
    '''
        Given a character, 'c', return an array of the bits that represent the
        ASCII representation of that character.

            EX:
                'h' -> 104 -> '0b1101000' -> ['1', '1', '0', '1', '0', '0', '0']
    '''

    return list(bin(ord(c)))[2:]

def msg_to_bits(msg):
    bits = ''
    for c in msg:
        bits += "".join(char_to_bits(c))

    bits = list(bits)

    # Add 8 zeros to signal the end of the message
    for i in range(8):
        bits.append('0')

    return bits

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
                val == 255 == 0b11111111
                b == 0

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

def encode(img):


    # shape of an image --> returns a tuple of (rows, cols, channel)
    shape = image.shape

    # dimensions of the image
    height = shape[0]
    width = shape[1]

    msg = 'hi'

    w = 10
    h = 10

    # make a fake 'image'
    img = [[(255, 255, 255) for x in range(w)] for y in range(h)]

    bits = msg_to_bits(msg)

    curr = 0

    for i in range(0, w):
        for j in range(0, h):
            for k in range(0, 3):
                if curr == len(bits):
                    break

                print("Current:", bits[curr], curr)

                val = img[i][j][k]
                b = int(bits[curr])

                # Major hack, fam
                img[i][j] = list(img[i][j])
                img[i][j][k] = int(inject_bit(b, val), 2)
                img[i][j] = tuple(img[i][j])

                curr += 1

    for i in range(0, w):
        for j in range(0, h):
            print(img[i][j]),
            if j == h -1:
                print('')


def decode():
    pass


def main():
    '''
        Flow:
            python stega -f <img> -s "this text is to be hidden"

            -or-

            python stega -d <img> -o <output file w/ decoded message>
    '''


     # Read an image file into a variable
    image = cv2.imread('mouse.png')

    encode(image)


if __name__ == '__main__':
    main()

