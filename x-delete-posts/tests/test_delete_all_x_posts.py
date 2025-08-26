import pytest
from xcleaner import delete_all_x_posts

def test_delete_all_x_posts(monkeypatch):
    class DummyAPI:
        def __init__(self):
            self.deleted = []
            self._posts = [type('Post', (), {'id': 1, 'full_text': 'foo'}), type('Post', (), {'id': 2, 'full_text': 'bar'})]
        def user_timeline(self, count, tweet_mode):
            if self._posts:
                posts, self._posts = self._posts, []
                return posts
            return []
        def destroy_status(self, post_id):
            self.deleted.append(post_id)
    api = DummyAPI()
    delete_all_x_posts(api)
    assert api.deleted == [1, 2]
