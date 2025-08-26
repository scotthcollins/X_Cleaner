import pytest
from xcleaner.authenticate_x import authenticate_x
import sys
import os


def test_authenticate_x(monkeypatch):
    class DummyAuth:
        pass
    class DummyAPI:
        pass
    def dummy_handler(*_args, **_kwargs):
        return DummyAuth()
    def dummy_api(*_args, **_kwargs):
        return DummyAPI()
    monkeypatch.setattr('tweepy.OAuth1UserHandler', dummy_handler)
    monkeypatch.setattr('tweepy.API', dummy_api)
    api = authenticate_x('k', 's', 't', 'ts')
    assert isinstance(api, DummyAPI)
