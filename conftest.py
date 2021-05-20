import pytest

from exams.testing import Path


@pytest.fixture()
def path(tmpdir) -> Path:
    return Path(tmpdir)
