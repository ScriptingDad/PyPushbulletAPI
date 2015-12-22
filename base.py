from statistics import mean
from requests import get


class PushbulletException(Exception):
    pass


class Pushbullet(object):

    def __init__(self, access_token):
        self.header = {'Access-Token': access_token, 'Content-Type': 'application/json'}
        self.me = get(url='https://api.pushbullet.com/v2/users/me',
                      headers=self.header).json()

        self.rl_reset = None    # place holder for ratelimit.
        self.rl_left = None
        self.rl_reduce = []

    def ratelimit(self, response):
        # called at the end of a message send to update the remaining.
        if None is not self.rl_left:
            self.rl_reduce.append(
                int(self.rl_left) - int(response.headers['x-ratelimit-remaining']))
        self.rl_left = response.headers['x-ratelimit-remaining']
        self.rl_reset = response.headers['x-ratelimit-reset']
        return mean(self.rl_reduce) if len(self.rl_reduce) > 0 else 0

    @property
    def reduced(self):
        return mean(self.rl_reduce)
