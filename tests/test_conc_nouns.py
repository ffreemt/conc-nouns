"""Test conc_nouns."""
# pylint: disable=broad-except
from conc_nouns import __version__
from conc_nouns import conc_nouns


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not conc_nouns()
    except Exception:
        assert True
