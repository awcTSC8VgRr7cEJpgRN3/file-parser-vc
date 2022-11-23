#!/usr/bin/env python

import os
import filecmp

blah = ' (2)'

def traversal_error_handler(oserror_instance):
    print(oserror_instance)
    # May do something more substantial here

for dirpath, dirnames, filenames in os.walk(os.getcwd(), topdown=True, onerror=traversal_error_handler, followlinks=True):
    # print('Traversal path:', dirpath)
    for filename in filenames:
        try:
            filepath = os.path.join(dirpath, filename)
            indexof_last_blah = filename.rfind(blah)
            if not indexof_last_blah < 0:
                filename_wo_blah = filename[:indexof_last_blah] + filename[indexof_last_blah + len(blah):]
                filepath_wo_blah = os.path.join(dirpath, filename_wo_blah)
                if filecmp.cmp(filepath, filepath_wo_blah):
                    os.remove(filepath)
        except Exception as e:
            # Other errors...
            print('\t' + str(type(e)) + ':', e)
