from .base import PushbulletException, Pushbullet
from requests import get, post


class Push(Pushbullet):

    def __init__(self, access_token):
        super().__init__(access_token)
        self.url = 'https://api.pushbullet.com/v2/pushes'

    def send_push(self, title, message, target):
        data = {'email': target, 'type': 'note', 'title': title, 'body': message}
        response = post(self.url, json=data, headers=self.header)
        if response.status_code == 200:
            self.ratelimit(response)
        return response
