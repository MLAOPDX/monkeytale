import os
from contextlib import contextmanager
from pathlib import Path

from hypothesis import strategies as st


UUID_PATTERN = (  # noqa
    r"(?i)[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}"
)


@contextmanager  # noqa
def pushd(path: Path):
    """Context manager version of pushd/popd."""
    old_cwd = os.getcwd()
    os.chdir(path)
    try:
        yield old_cwd
    finally:
        os.chdir(old_cwd)


# GENERIC HYPOTHESIS STRATEGIES
st_scenario = st.uuids(version=4).map(lambda u: u.hex)  # noqa
st_expectation = st.none()  # noqa
