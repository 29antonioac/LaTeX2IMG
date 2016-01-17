#!/usr/bin/env python3

"""
LaTeX2IMG use example
"""

import sys
from LaTeX2IMG import latex2img


if __name__ == "__main__":

    if len(sys.argv) < 4:
        EXPRESSION = input("Type LaTeX expression: ")
        FILENAME = input("Type desired file name: ")
        EXTENSION = input("Type desired file extension (gif,png,pdf,swf,emf,svg,webp): ")
    else:
        EXPRESSION = sys.argv[1]
        FILENAME = sys.argv[2]
        EXTENSION = sys.argv[3]

    file_result = latex2img(EXPRESSION, FILENAME, EXTENSION)

    print("Downloaded as", file_result)
