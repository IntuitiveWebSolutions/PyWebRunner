#!/usr/bin/env python
import sys
from PyWebRunner import WebTester
from yaml import load


def main(filepath):
    with open(filepath, 'r') as f:
        script = load(f)

    wt = WebTester()
    wt.start()
    wt.command_script(script, errors=False)
    wt.stop()


if __name__ == '__main__':
    filepath = sys.argv[1]
    main(filepath)
