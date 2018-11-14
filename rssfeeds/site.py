import sqlite3
import configparser
from connector.sqlite3 import SqlIte3
from connector.redis import Redis
import datetime
import feedparser;
import time

class Site:
	def __init__(self):
		config = configparser.RawConfigParser(allow_no_value=True)
		config.read("config/database.cfg")
		database = config.get("database", "default")
		if database != "Stateless":
			get_class = lambda x: globals()[x]
			self.connection = get_class(database)
		

	def get_latest_etag_from_site(self):
		result = self.connection().fetch_latest_by('rss', 'site = ' "'" + self.url + "'", 'rowid', self.url)
		return result

	def get_feed_from_yesterday_till_now(self, site):
		yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
		
		return feedparser.parse(site, modified=yesterday)

	def updateLatestRssInformation(self, last_etag, last_modified):
		self.connection().insert('rss',['site','etag', 'date'],[self.url, last_etag, last_modified])


	def getUrl(self):
		return self.url;

	def getSlackConfig(self):
		return self.slack;

	def getEmailConfig(self):
		return self.email;