import pytest
from xcleaner import authenticate_x

def test_authenticate_x(monkeypatch):
    class DummyAuth:
        pass
    class DummyAPI:
        pass
    def dummy_handler(api_key, api_secret_key, access_token, access_token_secret):
        return DummyAuth()
    def dummy_api(auth):
        return DummyAPI()
    monkeypatch.setattr('tweepy.OAuth1UserHandler', dummy_handler)
    monkeypatch.setattr('tweepy.API', dummy_api)
    api = authenticate_x('k', 's', 't', 'ts')
    assert isinstance(api, DummyAPI)
