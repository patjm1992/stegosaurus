# stegosaurus

```
              
                         .       .
                        / `.   .' \
                .---.  <    > <    >  .---.
                |    \  \ - ~ ~ - /  /    |
                 ~-..-~             ~-..-~
             \~~~\.'                    `./~~~/
              \__/                        \__/
               /                  .-    .  \
        _._ _.-    .-~ ~-.       /       }   \/~~~/
    _.-'q  }~     /       }     {        ;    \__/
   {'__,  /      (       /      {       /      `. ,~~|   .     .
    `''''='~~-.__(      /_      |      /- _      `..-'   \\   //
                / \   =/  ~~--~~{    ./|    ~-.     `-..__\\_//_.-'
               {   \  +\         \  =\ (        ~ - . _ _ _..---~
               |  | {   }         \   \_\
              '---.o___,'       .o___,'       -- Stegosaurus
```

A CLI [steganography tool](https://en.wikipedia.org/wiki/Steganography) written in Python. It packs your message in the least significant bits of the pixels of an image. **Note**: I've only tested this on .png files.

## Usage

The CLI is pretty simple. You're either hiding a message or you're extracting a message from an image (the message will be printed to STDOUT).

```bash
usage: steg.py [-h] -f IMG_FILE [-m MSG] [-o OUTPUT_IMG]

A steganography tool written in Python.

optional arguments:
  -h, --help            show this help message and exit

  -f IMG_FILE, --img-file IMG_FILE
                        The .png file you would like to either hide a message
                        in or extract a message from.

  -m MSG, --msg MSG     The message you would like to hide.

  -o OUTPUT_IMG, --output-img OUTPUT_IMG
                        The output file name of the image with the message
                        hidden inside of it.

```

## Installation

OpenCV-Python is a dependency. Get it [here.](http://docs.opencv.org/2.4/doc/tutorials/introduction/table_of_content_introduction/table_of_content_introduction.html)

```bash
$ git clone https://github.com/patjm1992/stegosaurus
$ cd stegosaurus
```

_Hiding a message:_
```bash
$ python steg.py -f mouse.png -m "ayy lmao" -o encoded.png
Loading image 'mouse.png'... image loaded.
Encoding message 'ayy lmao' in image...
Bit representation: 011000010111100101111001001000000110110001101101011000010110111100000000
Message hidden.
```

_Extracting a message:_
```bash
$ python steg.py -f encoded.png                           
Loading image 'encoded.png'... image loaded.
Extracting message from image... got it.
MESSAGE: 'ayy lmao'
```

Since only the least significant bit of each pixel is used to hold the bits that comprise your message, the altered pixels in the modified image are imperceptible to the human eye.

##  To-Do

Right now the program doesn't check ahead of time if a message will fit in your image (it probably will unless your image is really tiny or you're hiding a long novel, or something). It'd be simple to add though and I may tack that on eventually.