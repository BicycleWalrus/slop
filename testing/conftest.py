#!/usr/bin/env python3
"""TPatrick | Alta3 Research
   Controlling pytest behaviors with conftest.py"""

import pytest
import requests

@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        # This is the error we want to raise
        raise RuntimeError("Network access not allowed during testing!")

    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())
