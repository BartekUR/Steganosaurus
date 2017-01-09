#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from __future__ import absolute_import, unicode_literals

import sys
from PIL import Image


def read_text(path):
    img = Image.open(path)
    counter = 0
    result = []
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            if r % 8 == g % 8 == b % 8 == 1:
                result.append(counter)
            counter += 1
            if counter == 16:
                counter = 0
    return ''.join([hex(_)[-1:] for _ in result]).decode("hex")


def main():
    if len(sys.argv) == 2:
        input_image_path = sys.argv[1]
        print(read_text(input_image_path))
        return
    print("\nPrzyklad uzycia:")
    print("./imgdec.py /tmp/lolcat.png")


if __name__ == "__main__":
    main()
