#!/usr/bin/env python3

import os
import sys
import pathlib
import subprocess
import argparse


def get_pytest():
    paths = map(pathlib.Path, os.environ['PATH'].split(':'))
    paths = [pathlib.Path(sys.executable).parent] + list(paths)
    for path in paths:
        path = path / 'py.test'
        if path.exists():
            return str(path)
    raise RuntimeError('py.test is not installed (pip install pytest)')


def run_tests(base, paths):
    pytest = get_pytest()
    for path in paths:
        print('%-24s' % ('%s...' % path.parent.relative_to(base)), end=' ')
        os.chdir(str(path.parent))
        try:
            subprocess.check_output([
                pytest, '-vv', '--tb=native', 'tests.py',
            ], stderr=subprocess.STDOUT, universal_newlines=True)
        except subprocess.CalledProcessError as e:
            print()
            print(e.output)
        else:
            print('OK')
        os.chdir(str(base))


def find_tests(paths):
    for path in paths:
        path = path.parent if path.is_file() else path
        yield from path.resolve().glob('**/tests.py')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*')
    args = parser.parse_args()

    base = pathlib.Path().resolve()

    if args.paths:
        paths = map(pathlib.Path, args.paths)
    else:
        paths = [base]

    run_tests(base, find_tests(paths))


if __name__ == '__main__':
    main()
