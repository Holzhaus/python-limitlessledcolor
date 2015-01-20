# LimitlessLED color converter

This is a small module to convert HTML/RGB/HSV colors into LimitlessLED hex
command codes.

Please note that this does not allow you to control the LimitlessLED bulbs
directly, but can be used together with
[python-wifi-leds](https://github.com/joaquincasares/python-wifi-leds) to
do so.

## Colors (ordered by calculation precision)

| HTML       | expected   | calculated   | diff   | color                                                    |
|-----------:|-----------:|-------------:|-------:|---------------------------------------------------------:|
| `0x4169e1` |     `0x10` |       `0x10` |    `0` | ![4169E1](http://dummyimage.com/20x20/4169E1/4169E1.gif) |
| `0x87cefa` |     `0x20` |       `0x1f` |    `1` | ![87CEFA](http://dummyimage.com/20x20/87CEFA/87CEFA.gif) |
| `0x00ffff` |     `0x30` |       `0x2f` |    `1` | ![FFFF00](http://dummyimage.com/20x20/FFFF00/FFFF00.gif) |
| `0xdaa520` |     `0x90` |       `0x91` |   `-1` | ![DAA520](http://dummyimage.com/20x20/DAA520/DAA520.gif) |
| `0xff0000` |     `0xb0` |       `0xaf` |    `1` | ![FF0000](http://dummyimage.com/20x20/FF0000/FF0000.gif) |
| `0x7fffd4` |     `0x40` |       `0x3e` |    `2` | ![7FFFD4](http://dummyimage.com/20x20/7FFFD4/7FFFD4.gif) |
| `0xffff00` |     `0x80` |       `0x84` |   `-4` | ![FFFF00](http://dummyimage.com/20x20/FFFF00/FFFF00.gif) |
| `0x008000` |     `0x60` |       `0x5a` |    `6` | ![800000](http://dummyimage.com/20x20/800000/800000.gif) |
| `0xda70d6` |     `0xe0` |       `0xd8` |    `8` | ![DA70D6](http://dummyimage.com/20x20/DA70D6/DA70D6.gif) |
| `0x2e8b57` |     `0x50` |       `0x47` |    `9` | ![2E8B57](http://dummyimage.com/20x20/2E8B57/2E8B57.gif) |
| `0xff00ff` |     `0xd0` |       `0xd9` |   `-9` | ![FF00FF](http://dummyimage.com/20x20/FF00FF/FF00FF.gif) |
| `0xffc0cb` |     `0xc0` |       `0xb6` |   `10` | ![FFC0CB](http://dummyimage.com/20x20/FFC0CB/FFC0CB.gif) |
| `0xffa500` |     `0xa0` |       `0x93` |   `13` | ![FFA500](http://dummyimage.com/20x20/FFA500/FFA500.gif) |
| `0xe6e6fa` |     `0xf0` |       `0x05` |  `-20` | ![E6E6FA](http://dummyimage.com/20x20/E6E6FA/E6E6FA.gif) |
| `0x32cd32` |     `0x70` |       `0x5a` |   `22` | ![32CD32](http://dummyimage.com/20x20/32CD32/32CD32.gif) |
| `0xee82ee` |     `0x00` |       `0xd9` |   `38` | ![EE82EE](http://dummyimage.com/20x20/EE82EE/EE82EE.gif) |

## Contributing

The algorithm isn't very precise, so any improvements are welcome. Make sure
to include an updated version of the above table in your pull request.

## License

This is licensed under the BSD (3-Clause) License. See [LICENSE](LICENSE) for details.

## Author

This was written by Jan Holthuis.