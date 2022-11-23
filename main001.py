#!/usr/bin/env python3

import os
import file_parser_vc

def traversal_error_handler(oserror_instance):
    print(oserror_instance) # May do something more substantial here

for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown=True, onerror=traversal_error_handler, followlinks=True):
    print('Traversal path:', dirpath)
    for filename in filenames:
        try:
            file = file_parser_vc.File(os.path.join(dirpath, filename))
            if file.isPNG():
                print('\t"' + filename + '"', 'is PNG.')
            else:
                print('\t"' + filename + '"', 'is not PNG.')
        except Exception as e:
            print('\t' + str(type(e)) + ':', e) # Other errors...
