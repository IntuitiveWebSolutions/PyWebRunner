#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyWebRunner import WebTester
from yaml import load
from json import loads


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run a PyWebRunner YAML/JSON script.')
    parser.add_argument('-b', '--browser', help='Which browser to load. Defaults to Firefox.')
    parser.add_argument('--base-url', help='Base URL to use with goto command.')
    parser.add_argument('--errors', dest='errors', action='store_true', help='Whether or not to show errors.')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    errors = args.errors or False
    wt = WebTester(driver=args.browser, base_url=args.base_url)
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
            wt.command_script(script=script, errors=errors)
    wt.stop()


if __name__ == '__main__':
    main()
