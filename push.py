from .base import PushbulletException, Pushbullet
from requests import post


class Push(Pushbullet):
    """Push notification."""

    def __init__(self, access_token):
        super().__init__(access_token)
        self.url = 'https://api.pushbullet.com/v2/pushes'

    def send_push(self, title, message, target, target_type='email'):
        # Check to see if the target type is an available option.
        types = ['device_iden', 'email', 'channel_tag', 'client_iden']
        if target_type not in types:
            raise PushbulletException('Target type {0} doesn\'t exist.\n'
                                      'Please use one of the following: {1}.'
                                      .format(target_type, types))
        data = {target_type: target, 'type': 'note', 'title': title, 'body': message}
        response = post(self.url, json=data, headers=self.header)
        if response.status_code == 200:
            self.ratelimit(response)
        return response
