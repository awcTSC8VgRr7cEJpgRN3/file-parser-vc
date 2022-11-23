#!/usr/bin/env python3

import os
import math
from PIL import Image

def traversal_error_handler(oserror_instance):
    print(oserror_instance) # May do something more substantial here

# PNG meta should not be coupled with main function
bits_per_byte = 8
hexstr_png_header = '89504e470d0a1a0a'
sizeof_png_header = math.ceil(len(hexstr_png_header)*4/bits_per_byte)

for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown=True, onerror=traversal_error_handler, followlinks=True):
    print('Traversal path:', dirpath)
    for filename in filenames:
        try:
            with Image.open(os.path.join(dirpath, filename)) as img: # PNG meta...
                print('\tFormat of', '"' + filename + '"', 'is', img.format + '.')
        except IOError as e:
            print('\t' + str(type(e)), 'is raised by opening', '"' + filename + '".')
        except Exception as e:
            print('\t' + str(type(e)) + ':', e) # Other errors...
