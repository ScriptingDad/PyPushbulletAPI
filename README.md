# PyPushbulletAPI
API to make interacting with Pushbullet API easier from python.
Requires requests library.

````from Pushbullet import Sms
````push = Sms('APIKey')
````push.send_sms(phone="", device=""deviceiden", message="")

This also requires an Android device that has pushbullet installed and running on it as an SMS relay.  
Message will come from the device identified by the device iden.  This can be found in a couple of ways.
Since the API call isn't implemented yet it will be easiest to login to Pushbullet and navigate to the device and pull it from the URL.

Open www.pushbullet.com and login > Select device > click on the desired device > look at the URL:      https://www.pushbullet.com/#devices/{device_iden}

The API will automatically grab and document the rate limite and reset and remaining calls that can be made.
It will also waste a call getting your information by calling the https://api.pushbullet.com/v2/users/me.
