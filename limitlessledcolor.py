#!/usr/bin/env python
# -*- coding: utf-8 -*-
import colorsys
import math

NAMES = {'Violet':       0x00,
         'RoyalBlue':    0x10,
         'LightSkyBlue': 0x20,
         'Aqua':         0x30,
         'AquaMarine':   0x40,
         'SeaGreen':     0x50,
         'Green':        0x60,
         'LimeGreen':    0x70,
         'Yellow':       0x80,
         'Goldenrod':    0x90,
         'Orange':       0xA0,
         'Red':          0xB0,
         'Pink':         0xC0,
         'Fuchsia':      0xD0,
         'Orchid':       0xE0,
         'Lavender':     0xF0}


def html_to_rgb(html):
    b = html % 0x100
    g = ((html - b) % 0x10000) / 0x100
    r = (html - (b + g)) / 0x10000
    return tuple([float(x)/255 for x in (r, g, b)])


def htmlstring_to_rgb(html):
    rgb = [int(n, 16)/float(255) for n in (html[:2], html[2:4], html[4:])]
    return tuple(rgb)


def rgb_to_ledcolor(r, g, b):
    hsv = colorsys.rgb_to_hsv(r, g, b)
    return hsv_to_ledcolor(*hsv)


def hsv_to_ledcolor(h, s, v):
    # FIXME: This is kinda hacky, so there's probably room for improvement
    color = int(round(math.radians(-h*360)/(math.pi*2)*255))
    # Compensate the roation
    color += 175
    # Make sure number is between 0 and 255
    if color > 255:
        color -= 255
    elif color < 0:
        color += 255
    return color


def html_to_ledcolor(html):
    rgb = html_to_rgb(html)
    return rgb_to_ledcolor(*rgb)


def htmlstring_to_ledcolor(html):
    rgb = htmlstring_to_rgb(html)
    return rgb_to_ledcolor(*rgb)


def name_to_ledcolor(name):
    if name in NAMES:
        return NAMES[name]

if __name__ == "__main__":
    # Output color precision table
    testcolors = ((0x00, 0xEE82EE),
                  (0x10, 0x4169E1),
                  (0x20, 0x87CEFA),
                  (0x30, 0x00FFFF),
                  (0x40, 0x7FFFD4),
                  (0x50, 0x2E8B57),
                  (0x60, 0x008000),
                  (0x70, 0x32CD32),
                  (0x80, 0xFFFF00),
                  (0x90, 0xDAA520),
                  (0xA0, 0xFFA500),
                  (0xB0, 0xFF0000),
                  (0xC0, 0xFFC0CB),
                  (0xD0, 0xFF00FF),
                  (0xE0, 0xDA70D6),
                  (0xF0, 0xE6E6FA))
    results = []
    for expected, html in testcolors:
        calculated = html_to_ledcolor(html)
        diff = expected - calculated
        if diff < -128:
            diff += 255
        elif diff > 128:
            diff -= 255
        colorstring = hex(html).ljust(8, '0')[2:].upper()
        url = ("![%s](http://dummyimage.com/20x20/%s/%s.gif)"
               % (colorstring, colorstring, colorstring))
        results.append([html, expected, calculated, diff, url])

    results = sorted(results, key=lambda x: math.fabs(x[3]))
    print("Colors (ordered by calculation precision)")
    colnames = ("HTML", "expected", "calculated", "diff", "color")
    colwidths = (10, 10, 12, 6, 56)
    print('| '+' | '.join([colnames[i].ljust(colwidths[i])
                           for i in range(5)])+' |')
    print('|-'+':|-'.join([("-"*colwidths[i]) for i in range(5)])+':|')
    for row in results:
        row[0] = ("0x%06x" % row[0])
        row[1] = ("0x%02x" % row[1])
        row[2] = ("0x%02x" % row[2])
        print('| '+' | '.join([(("`%s`" if i != 4 else "%s")
                                % str(row[i])).rjust(colwidths[i])
                               for i in range(5)])+' |')
