import sqlite3
from config_repository.slack_config import SlackConfig
from config_repository.mail_config import MailConfig
from .site import Site

class Awsfeed(Site):
	def __init__(self):
		Site.__init__(self)
		self.url = "http://feeds.feedburner.com/amazon/ISxM";
		self.slack = SlackConfig({
			"color": "36a64f",
	        "thumb_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/93/Amazon_Web_Services_Logo.svg/512px-Amazon_Web_Services_Logo.svg.png",
	        "footer_text": "AWS News Feed",
	        "fotter_icon": "https://platform.slack-edge.com/img/default_application_icon.png",
	        "username": "AWS",
	        "channel": "general"
		})
		self.email = MailConfig({
			"to": "your@gmail.com",
			"subject": "New AWS Article"
		});
	
