#!/usr/bin/env python3

import os
import math

def traversal_error_handler(oserror_instance):
    print(oserror_instance) # May do something more substantial here

# png meta should not be coupled with main function
bits_per_byte = 8
hexstr_png_header = '89504e470d0a1a0a'
sizeof_png_header = math.ceil(len(hexstr_png_header)*4/bits_per_byte)

for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown=True, onerror=traversal_error_handler, followlinks=True):
    print('Traversal path:', dirpath)
    for filename in filenames:
        with open(os.path.join(dirpath, filename), 'rb') as f:
            if f.read(sizeof_png_header) == bytes.fromhex(hexstr_png_header): # png meta...
                print('\t', filename, 'is a png file.')
            else:
                print('\t', filename, 'is not a png file.')
