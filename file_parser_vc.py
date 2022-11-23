#!/usr/bin/env python

from PIL import Image
import gzip
import zipfile

class File:
    def __init__(self, filepath):
        self.filepath = filepath
    def format_ext(self):
        #img
        try:
            with Image.open(self.filepath) as img:
                if img.format == 'PNG':
                    return ('.png',)
                elif img.format == 'JPEG':
                    return ('.jpeg','.jpg')
                elif img.format == 'BMP':
                    return ('.bmp',)
                elif img.format == 'GIF':
                    return ('.gif',)
                elif img.format == 'TIFF':
                    return ('.tiff','.tif')
        except IOError as e:
            pass
        except Exception as e:
            # Other errors...
            raise e
        #gz
        try:
            with gzip.open(self.filepath) as gz:
                gz.read()
                return ('.gz','.gzip')
        except IOError as e:
            pass
        except Exception as e:
            # Other errors...
            raise e
        #zip
        try:
            with zipfile.ZipFile(self.filepath) as zip:
                return ('.zip',)
        except zipfile.BadZipFile as e:
            pass
        except Exception as e:
            # Other errors...
            raise e
        #others
        return False
