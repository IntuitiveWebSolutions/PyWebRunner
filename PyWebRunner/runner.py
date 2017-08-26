#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse

from json import loads
from multiprocessing import Pool
from PyWebRunner import WebTester
from yaml import load

ARGS = {}


def run_test(filepath):
    try:
        errors = ARGS.errors or False
        driver = ARGS.browser or 'Chrome'
        timeout = ARGS.timeout or 30
        default_offset = ARGS.default_offset or 0

        wt = WebTester(driver=driver, base_url=ARGS.base_url,
                       timeout=int(timeout), default_offset=default_offset)
        wt.start()
        if ARGS.focus:
            wt.focus_browser()

        print("Processing {}:".format(filepath))
        with open(filepath, 'r') as f:
            if filepath.lower().endswith('yaml') or filepath.lower().endswith('yml'):
                script = load(f)
            elif filepath.lower().endswith('json'):
                script = loads(f.read())
            else:
                print("Couldn't detect filetype from extension. Defaulting to YAML.")
                script = load(f)
            wt.command_script(script=script, errors=errors, verbose=ARGS.verbose)
        wt.stop()
    except StandardError as e:
        print("Error running {}".format(filepath))
        print(e)


def main():
    global ARGS

    parser = argparse.ArgumentParser(description='Run a PyWebRunner YAML/JSON script.')
    parser.add_argument('-b', '--browser', help='Which browser to load. Defaults to Chrome.')
    parser.add_argument('--base-url', help='Base URL to use with goto command.')
    parser.add_argument('-t', '--timeout', help='Global wait timeout (in seconds). Defaults to 30.')
    parser.add_argument('-p', '--processes', help='Number of processes (browsers) to use. Defaults to 1')
    parser.add_argument('-do', '--default-offset', help='New default offset for scroll_to_element. (Default is 0)')
    parser.add_argument('--errors', dest='errors', action='store_true', help='Show errors.')
    parser.add_argument('--focus', dest='focus', action='store_true', help='Focus the browser on launch.')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Verbose output of commands being executed.')
    parser.add_argument('files', nargs='*')
    ARGS = parser.parse_args()

    processes = ARGS.processes or 1
    pool = Pool(int(processes))

    pool.map(run_test, ARGS.files)

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
