#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyWebRunner import WebTester
from yaml import load
from json import loads


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run a PyWebRunner YAML/JSON script.')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    wt = WebTester()
    wt.start()
    for filepath in args.files:
        print("Processing {}:".format(filepath))
        with open(filepath, 'r') as f:
            if filepath.lower().endswith('yaml') or filepath.lower().endswith('yml'):
                script = load(f)
            elif filepath.lower().endswith('json'):
                script = loads(f.read())
            else:
                print("Couldn't detect filetype from extension. Defaulting to YAML.")
                script = load(f)
            wt.command_script(script=script, errors=False)
    wt.stop()


if __name__ == '__main__':
    main()
