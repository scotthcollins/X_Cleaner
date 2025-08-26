
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from xcleaner.authenticate_x import authenticate_x


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
