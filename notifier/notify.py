from rssfeeds.site import Site
from .slack import Slack
from .mail import Mail
import html2text
import configparser

class Notify:
	def __init__(self, site, entry):
		config = configparser.RawConfigParser(allow_no_value=True)
		config.read("config/services.cfg")
		MailEnabled = config.get("Mail", "enabled")
		SlackEnabled = config.get("Slack", "enabled")
		self.site = site
		self.entry = entry

		self.formatter = html2text.HTML2Text()
		self.formatter.ignore_links = True
		self.formatter.ignore_images = True
		self.formatter.re_space  = True
		self.formatter.re_unescape = True
		self.formatter.inline_links = True
		self.formatter.protect_links = True
		self.formatter.single_linke_breaks = True
		
		if MailEnabled == "True":
			self.send_mail_message(self.entry)
		if SlackEnabled == "True":
			self.send_slack_message(self.entry)

	def send_slack_message(self, entry):
		Slack(self.site.getSlackConfig()).send_message(entry.title, self.formatter.handle(entry.summary)[:125], getattr(entry, "author", "Unknown Author"), entry.link)

	def send_mail_message(self, entry):
		Mail(self.site.getEmailConfig()).send_message(entry.title, self.formatter.handle(entry.summary)[:125], entry.link)