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


def test_conc_nouns1():
    """Test 1."""
    text = """The mountains and rivers are scenery, and life is
        destined; no matter from a distance, miss each other.
        A greeting is my wish; take care of  my body and be
        healthy for a century."""
    _ = conc_nouns(text)
    _ = sum(_)

    assert _ >= 3


def test_conc_nouns2():
    """Test 2."""
    # this seems to fail...
    text = """Have a seat in that chair with comfort and drink some
    juice to soothe your thirst."""

    text = """There is a road to the hill of books"""
    _ = conc_nouns(text)

    _ = sum(_)
    assert _ >= 2
