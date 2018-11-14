import sqlite3
from config_repository.slack_config import SlackConfig
from config_repository.mail_config import MailConfig
from .site import Site

class NewYorkTimesTech(Site):
	def __init__(self):
		Site.__init__(self)
		self.url = "http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml";
		self.slack = SlackConfig({
			"color": "3390b2",
	        "thumb_url": "https://www.sjpl.org/sites/default/files/images/1718/nyt.png",
	        "footer_text": "New york Tech Time News",
	        "fotter_icon": "https://pmcvariety.files.wordpress.com/2013/08/t_logo_2048_black.png?w=1000&h=563&crop=1",
	        "username": "New York Times Tech",
	        "channel": "general"
		})
		self.email = MailConfig({
			"to": "your@gmail.com",
			"subject": "New York times Tech News"
		});
	
