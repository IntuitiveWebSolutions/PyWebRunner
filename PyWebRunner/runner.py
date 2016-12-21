#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PyWebRunner import WebTester
from yaml import load
from json import loads


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run a PyWebRunner YAML/JSON script.')
    parser.add_argument('-b', '--browser', help='Which browser to load. Defaults to Chrome.')
    parser.add_argument('--base-url', help='Base URL to use with goto command.')
    parser.add_argument('-t', '--timeout', help='Global wait timeout (in seconds). Defaults to 30.')
    parser.add_argument('-do', '--default-offset', help='New default offset for scroll_to_element. (Default is 0)')
    parser.add_argument('--errors', dest='errors', action='store_true', help='Show errors.')
    parser.add_argument('--focus', dest='focus', action='store_true', help='Focus the browser on launch.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose output of commands being executed.')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    errors = args.errors or False
    driver = args.browser or 'Chrome'
    timeout = args.timeout or 30
    default_offset = args.default_offset or 0
    wt = WebTester(driver=driver, base_url=args.base_url, timeout=int(timeout), default_offset=default_offset)
    wt.start()
    if args.focus:
        wt.focus_browser()

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
            wt.command_script(script=script, errors=errors, verbose=args.verbose)
    wt.stop()


if __name__ == '__main__':
    main()
