# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from PIL import Image
import random


def normalize_pixel(r, g, b):
    if r % 8 == g % 8 == b % 8 == 1:
        seed = random.randint(1, 3)
        if seed == 1:
            r = r - 1 if r >= 128 else r + 1
        if seed == 2:
            g = g - 1 if r >= 128 else g + 1
        if seed == 3:
            b = b - 1 if r >= 128 else b + 1
    return r, g, b


def _modify(i):
    if i >= 128:
        for x in range(8 + 1):
            if i % 8 == 1:
                return i
            i -= 1
    else:
        for x in range(8 + 1):
            if i % 8 == 1:
                return i
            i += 1
    raise ValueError


def normalize(path, output):
    img = Image.open(path)
    img = img.convert('RGB')
    size = img.size
    new_img = Image.new('RGB', size)

    for y in range(img.size[1]):
        for x in range(img.size[0]):
            r, g, b = img.getpixel((x, y))
            _r, _g, _b = normalize_pixel(r, g, b)
            new_img.putpixel((x, y), (_r, _g, _b))
    new_img.save(output, "PNG", optimize=True)


def hide_text(path, text):
    text = str(text)

    write_param = []
    _base = 0
    for _ in text.encode("hex"):
        write_param.append(int(_, 16) + _base)
        _base += 16

    img = Image.open(path)
    counter = 0
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            if counter in write_param:
                r, g, b = img.getpixel((x, y))
                r, g, b = map(_modify, [r, g, b])
                img.putpixel((x, y), (r, g, b))
            counter += 1

    img.save(path, "PNG", optimize=True)


def encode(input_image_path, output_image_path, encode_text):
    normalize(input_image_path, output_image_path)
    hide_text(output_image_path, encode_text)
