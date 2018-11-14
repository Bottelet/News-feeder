# Get your news live with News-feeder 

Post your favorite RSS Feed to Slack or your email, with simple configuration.

### How to get started
1. Copy one of the current sites under `rssfeeds/` for example take `new_york_times.py`
2. Edit the values in your new file (Or change a old one)
```python
self.url is the base url of the RSS feed
self.slack is your slack config, what the bot should be called what images the bot should have etc.
self.email is the email config for site, what the subject should be etc.
```
3. Under `config/services.cfg` You can chose where to be notified, by setting `enabled` to `True` or `False`
```
If you enable email you should change the config in `notifier/email.py` to use a SMTP of your choice etc.
If you enable Slack you should insert your bot token under `notifier/slack.py` (See under how to get a slack token)
```

### Create a Slack App
1. [Create a slack app here](https://api.slack.com/slack-apps)
2. Under "OAuth & Permissions"
3. Take the "Bot User OAuth Access Token" 
4. Use it

## Database types
To keep track of what news is already sent there are two ways use a Sqlite3 Database which is saved locally(So will not work on something like Lambda). Which is why there is also a Redis option which can be a stored on another server somewhere.

There is also a third options which is `Stateless` which does not keep track of anything but just takes the last 24 hours and post the entries from those, meaning if u run it multiple times a day you will get the same news over and over.

You can change the Database use in `config/database.cfg` And just change the `Default` value to what you wish it should use.