import cv2
import numpy
import argparse

'''
    A CLI steganography tool.
'''

def char_to_bits(c):
    '''
        Given a character, 'c', return an array of the bits that represent the
        ASCII representation of that character.

            EX:
                'h' -> 104 -> '0b1101000' -> ['1', '1', '0', '1', '0', '0', '0']
    '''

    return list(bin(ord(c)))[2:]

def msg_to_bits(msg):
    '''
        Given a string 'msg', return a string representation of the binary
        representation of that string.
    '''

    bits = ''
    for c in msg:
        if len(bin(ord(c))) == 8:
            bits += '00'
        elif len(bin(ord(c))) == 9:
            bits += '0'
        bits += "".join(char_to_bits(c))

    bits = list(bits)

    # Add 8 zeros to signal the end of the message
    for i in range(8):
        bits.append('0')

    return bits

def bits_to_msg(bits):
    '''
        The opposite of the 'msg_to_bits' function.
    '''

    char_list = []
    char = ''
    i = 0

    # Build a list where each item is an 8-bit ASCII character (1 padding bit)
    for b in bits:
        char += b
        i += 1
        if i == 8:
            char_list.append(char)
            i = 0
            char = ''

    msg = ''

    for i in range(0, len(char_list)):
        msg += chr(int(char_list[i], 2))

    return msg

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
    '''
        Given a value 'val', such as 255, return the least significant bit.
    '''

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

def encode(img, msg):
    '''
        Given an image and a message, encode that message in the image.

        Return the modified image.
    '''

    # shape of an image --> returns a tuple of (rows, cols, channel)
    shape = img.shape

    # dimensions of the image
    height = shape[0]
    width = shape[1]

    bits = msg_to_bits(msg)

    curr = 0

    print("Encoding message '" + msg + "' in image..." )
    print("Bit representation: " + "".join(bits))

    for i in range(0, width):
        for j in range(0, height):
            for k in range(0, 3):
                if curr == len(bits):
                    break

                val = img[i][j][k]
                b = int(bits[curr])

                # Major hack, fam -- 'temporary workaroud'
                img[i][j] = list(img[i][j])
                img[i][j][k] = int(inject_bit(b, val), 2)
                img[i][j] = tuple(img[i][j])

                curr += 1

    print("Message hidden.")
    return img

def decode(img):
    '''
        Given an image (that supposedly has had steganography performed on it),
        return the message that is hidden within.
    '''

    shape = img.shape

    height = shape[0]
    width = shape[1]

    # Will hold the bits of the message as we collect them
    bits = ''

    print("Extracting message from image..."),
    for i in range(0, width):
        for j in range(0, height):
            px = img[i][j]
            for val in px:
                lsb = access_lsb(val)
                bits += str(lsb)
                # Check for the flag (8 zero bits)
                if bits[-8:] == '00000000':
                    print("got it.")
                    return bits_to_msg(bits)

def main():
    descrip = 'A steganography tool written in Python.'
    img_help = 'The .png file you would like to either hide a message in or extract a message from.'
    msg_help = 'The message you would like to hide.'
    out_help = 'The output file name of the image with the message hidden inside of it.'
    parser = argparse.ArgumentParser(description=descrip)
    parser.add_argument('-f', '--img-file', help=img_help, required=True)
    parser.add_argument('-m', '--msg', help=msg_help)
    parser.add_argument('-o', '--output-img', help=out_help)
    args = parser.parse_args()

    # Read an image file into a variable
    file_name = args.img_file

    print("Loading image '" + file_name + "'..."),
    image = cv2.imread(file_name)

    if image is not None:
        print("image loaded.")
        if args.msg is not None:
            encoded_img = encode(image, args.msg)
            cv2.imwrite(args.output_img, encoded_img)
        else:
            print("MESSAGE: '" + decode(image) + "'")
    else:
        print("Error loading image.")
        quit()


if __name__ == '__main__':
    main()

