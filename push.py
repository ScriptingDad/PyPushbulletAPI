from .base import PushbulletException, Pushbullet
from requests import get, post


class Push(Pushbullet):

    def __init__(self, access_token):
        super().__init__(self, access_token)
        self.url = 'https://api.pushbullet.com/v2/push'

    def send_push(self, title, message, target):
        data = {'email': target, 'type': 'note', 'title': title, 'message': message}
        response = post(self.url, json=data, headers=self.headers)
        if response.status_code == 200:
            self.ratelimit(response)
        return response
