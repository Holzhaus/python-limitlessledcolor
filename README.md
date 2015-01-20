# LimitlessLED color converter

This is a small module to convert HTML/RGB/HSV colors into LimitlessLED hex
command codes.

Please note that this does not allow you to control the LimitlessLED bulbs
directly, but can be used together with
[python-wifi-leds](https://github.com/joaquincasares/python-wifi-leds) to
do so.

## Colors (ordered by calculation precision)

HTML     | expected | calculated | diff
---------------------------------------
0x4169e1 |     0x10 |       0x10 |    0
0x87cefa |     0x20 |       0x1f |    1
0x00ffff |     0x30 |       0x2f |    1
0xdaa520 |     0x90 |       0x91 |   -1
0xff0000 |     0xb0 |       0xaf |    1
0x7fffd4 |     0x40 |       0x3e |    2
0xffff00 |     0x80 |       0x84 |   -4
0x008000 |     0x60 |       0x5a |    6
0xda70d6 |     0xe0 |       0xd8 |    8
0x2e8b57 |     0x50 |       0x47 |    9
0xff00ff |     0xd0 |       0xd9 |   -9
0xffc0cb |     0xc0 |       0xb6 |   10
0xffa500 |     0xa0 |       0x93 |   13
0xe6e6fa |     0xf0 |       0x05 |  -20
0x32cd32 |     0x70 |       0x5a |   22
0xee82ee |     0x00 |       0xd9 |   38

## Contributing

The algorithm isn't very precise, so any improvements are welcome. Make sure
to include an updated version of the above table in your pull request.

## License

This is licensed under the BSD (3-Clause) License. See [LICENSE](LICENSE) for details.

## Author

This was written by Jan Holthuis.