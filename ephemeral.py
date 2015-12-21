from requests import post
from .base import Pushbullet, PushbulletException
# from re import match


class Sms(Pushbullet):

    def __init__(self, access_token):

        Pushbullet.__init__(self, access_token)
        self.url = 'https://api.pushbullet.com/v2/ephemerals'

    def send_sms(self, message, device, phone):
        if (not self.me or
                not device or
                not phone):
            raise PushbulletException('Missing required value (iden|device_id|phone)')
        data = {'push': {
                    'package_name': 'com.pushbullet.android',
                    'type': 'messaging_extension_reply',
                    'conversation_iden': phone,
                    'source_user_iden': self.me['iden'],
                    'target_device_iden': device,
                    'message': message},
                'type': 'push'}
        response = post(url=self.url, headers=self.header, json=data)
        if response.status_code == 200:
            self.ratelimit(response.headers['x-ratelimit-reset'],
                           response.headers['x-ratelimit-remaining'])
        return response
