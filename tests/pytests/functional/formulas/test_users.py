"""
Tests using users formula
"""

import pytest


@pytest.fixture(scope="module")
def _formula(saltstack_formula):
    with saltstack_formula(name="users-formula", tag="0.48.8") as formula:
        yield formula


@pytest.fixture(scope="module")
def modules(loaders, _formula):
    return loaders.modules


def test_users_formula(modules):
    # sudo
    ret = modules.state.sls("users.sudo", test=True)
    for staterun in ret:
        assert not staterun.result.failed

    # bashrc
    ret = modules.state.sls("users.bashrc", test=True)
    for staterun in ret:
        assert not staterun.result.failed
