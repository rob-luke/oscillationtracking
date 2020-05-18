#!/usr/bin/env python

"""Tests for `oscillationtracking` package."""


from oscillationtracking.simulation import sinusoid


def test_sinusoid():
    """Sample pytest test function with the pytest fixture as an argument."""
    t, d = sinusoid()

    # Check defaults
    assert t.shape[0] == 6000
    assert d.shape[0] == 6000
