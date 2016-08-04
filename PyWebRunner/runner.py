#!/usr/bin/env python
from PyWebRunner import WebTester
from yaml import load


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Run a PyWebRunner YAML script.')
    parser.add_argument('files', nargs='*')
    args = parser.parse_args()

    wt = WebTester()
    wt.start()
    for filepath in args.files:
        print("Processing {}:".format(filepath))
        with open(filepath, 'r') as f:
            script = load(f)
            wt.command_script(script=script, errors=False)
    wt.stop()


if __name__ == '__main__':
    main()
