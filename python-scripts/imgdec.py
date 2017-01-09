#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import sys
from PIL import Image

DIST = 8


def is_modify_pixel(r, g, b):
    return r % DIST == g % DIST == b % DIST == 1


def to_str(s):
    return s.decode("hex")


def read_text(path):
    img = Image.open(path)
    counter = 0
    result = []
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            if is_modify_pixel(r, g, b):
                result.append(counter)
            counter += 1
            if counter == 16:
                counter = 0
    return to_str(''.join([hex(_)[-1:] for _ in result]))


def main():
    if len(sys.argv) == 2:
        input_image_path = sys.argv[1]
        print(read_text(input_image_path))
        return
    help()


def help():
    print("Przyklad uzycia:")
    print("imgdec.py /tmp/image/output.jpg")
    print("")


if __name__ == "__main__":
    main()
