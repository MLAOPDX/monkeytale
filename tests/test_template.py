import re

import pytest
from devtools import debug  # noqa
from hypothesis import example
from hypothesis import given
from hypothesis import settings
from hypothesis import strategies as st  # noqa
from utils import pushd
from utils import st_expectation
from utils import st_scenario
from utils import UUID_PATTERN


@settings(max_examples=100)
@given(
    scenario=st_scenario,
    expectation=st_expectation,
)
@example(
    scenario="example",
    expectation=None,
)
def test_function(tmp_path_factory, scenario: str, expectation):
    """Test function template"""
    # Run each test in its own directory
    with pushd(tmp_path_factory.mktemp(scenario)):
        if re.fullmatch(UUID_PATTERN, scenario):
            # Property-Based Testing
            assert expectation is None
        elif isinstance(expectation, Exception):
            with pytest.raises(expectation) as e:
                assert e
        else:
            assert expectation is None
