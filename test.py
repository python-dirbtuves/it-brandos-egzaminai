#!/usr/bin/env python3

import argparse
import os
import pathlib
import subprocess
import sys
import pip


class Config:

    def __init__(self, base):
        self.base = base
        self.venv = base / 'env'
        self.pip = self.venv / 'bin/pip'
        self.mypy = self.venv / 'bin/mypy'
        self.pytest = self.venv / 'bin/py.test'
        self.flake8 = self.venv / 'bin/flake8'
        self.restview = self.venv / 'bin/restview'


def ensure_venv(config: Config):
    if not config.venv.exists():
        subprocess.run([sys.executable, '-m', 'venv', str(config.venv)], check=True)
    if not config.mypy.exists():
        pip.main(['install', 'mypy'])
    if not config.pytest.exists():
        pip.main(['install', 'pytest'])
        pip.main(['install', 'pytest-mock'])
        pip.main(['install', 'pytest-cov'])
    if not config.flake8.exists():
        pip.main(['install', 'flake8'])
    if not config.restview.exists():
        pip.main(['install', 'restview'])


def run_mypy(config, path):
    files = [path.parent / x for x in os.listdir(path.parent) if x.endswith('.py') and not x.startswith('test')]
    subprocess.run(
        [config.mypy, '--follow-imports=skip', '--show-traceback'] + files,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        check=True,
    )


def run_pytest(config, path):
    coverage = sum([['--cov', u.stem] for u in path.parent.glob('u*.py')], [])
    subprocess.run(
        [config.pytest, '-vvx', '--tb=native'] + coverage + ['--cov-report', 'term-missing', '--cov-fail-under', '100', path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        check=True,
    )


def run_flake8(config, path):
    subprocess.run(
        [config.flake8, '--exclude=env,.ropeproject', '--max-line-length=120', path],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
        check=True,
    )


def run_tests(config: Config, paths):
    for path in paths:
        print('%-42s' % ('%s...' % path.parent.relative_to(config.base)), end=' ', flush=True)
        try:
            run_mypy(config, path)
            run_pytest(config, path)
            run_flake8(config, path)
        except subprocess.CalledProcessError as e:
            print()
            print(e.stdout)
            return e.returncode
        else:
            print('OK', flush=True)
    print("All tests PASS.")


def find_tests(paths):
    for path in paths:
        path = path.parent if path.is_file() else path
        yield from sorted(path.resolve().glob('**/tests.py'))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('paths', nargs='*')
    args = parser.parse_args()

    base = pathlib.Path(__file__).resolve().parent
    config = Config(base)

    if args.paths:
        paths = args.paths
    else:
        paths = sorted([pathlib.Path(base / 'exams' / x) for x in os.listdir(base / 'exams') if x.isdigit()])

    ensure_venv(config)
    return run_tests(config, find_tests(map(pathlib.Path, paths)))


if __name__ == '__main__':
    sys.exit(main() or 0)
