import os
import pathlib

import pytest


class Path(pathlib.WindowsPath if os.name == 'nt' else pathlib.PosixPath):

    def write(self, *lines):
        self.write_text('\n'.join(lines))

    def read(self):
        return self.read_text().splitlines()


@pytest.fixture()
def path(tmpdir):
    return Path(tmpdir)
