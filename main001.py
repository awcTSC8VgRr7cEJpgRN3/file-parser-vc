#!/usr/bin/env python

import os
import file_parser_vc as fp

def traversal_error_handler(oserror_instance):
    print(oserror_instance)
    # May do something more substantial here

for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown=True, onerror=traversal_error_handler, followlinks=True):
    # print('Traversal path:', dirpath)
    for filename in filenames:
        try:
            filepath = os.path.join(dirpath, filename)
            file = fp.File(filepath)
            fileext = file.format_ext()
            if fileext and os.path.splitext(filepath)[1].lower() not in fileext:
                os.rename(filepath, filepath + fileext[0])
        except Exception as e:
            # Other errors...
            print('\t' + str(type(e)) + ':', e)
