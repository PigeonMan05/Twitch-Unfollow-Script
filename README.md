# Twitch Unfollow Script

This is a Python script that mass unfollows Twitch channels.
I made this just because my account was hacked and followed over 900 channels. Just thought I'd post it here for others to use!

All credit doesn't go to me, I used [TobiasPankner](https://github.com/TobiasPankner)'s [Twitch-Unfollower](https://github.com/TobiasPankner/Twitch-Unfollower/tree/master) for reference.
Without their code, I probably wouldn't have been able to make this.
I also use their steps in the ReadMe.md file.

Just like how i used [TobiasPankner](https://github.com/TobiasPankner)'s code for reference and to addon to it, be free to do the same with my code.

## Prerequisites

- Python 3.x ([Download](https://www.python.org/downloads/))

## Getting your Twitch authorization
**Treat these headers like your password!**

1. Log into your Twitch account.
2. Open Chrome dev tools (F12) -> Network.
3. Refresh the page.
4. Copy the cookie of one of the gql requests (Right click -> Copy -> Copy request headers).

![image](https://user-images.githubusercontent.com/39444749/206862007-63c4c0ed-dbfa-4e71-8f34-2d42f75dd63a.png)

## Configuration
Fill in the required information in the `config.yml` file:

```yaml
Authorization: YOUR_TWITCH_AUTHORIZATION
Client-Id: YOUR_CLIENT_ID
Client-Integrity: YOUR_CLIENT_INTEGRITY
X-Device-Id: YOUR_DEVICE_ID
Content-Type: text/plain;charset=UTF-8

# Whitelist channels to not be unfollowed (optional - case sensitive - usernames only)
Whitelist:
  - username1
```
## Run the script

 1. Install dependencies:   ```pip install -r requirements.txt```
 2.  [Get your twitch authorization](#getting-your-twitch-authorization)
 3. Make sure you have filled in the necessary information in the config.yml file.
 4. Run [main.py](main.py): `python main.py`
