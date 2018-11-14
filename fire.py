import feedparser;
import sqlite3
from rssfeeds.site import Site
from rssfeeds.awsfeed import Awsfeed
from rssfeeds.new_york_times_tech import NewYorkTimesTech
from notifier.slack import Slack
from notifier.notify import Notify
import configparser

if __name__ == '__main__':		
	config = configparser.RawConfigParser(allow_no_value=True)
	config.read("config/database.cfg")
	database = config.get("database", "default")

	print(database)
	for rss_site in Site.__subclasses__():
		if database == "Stateless":
			last_24_hours_feed = rss_site().get_feed_from_yesterday_till_now(rss_site().getUrl())
			entries = last_24_hours_feed.entries
			for entry in entries:
				Notify(rss_site(), entry);
		else:
			site_state = rss_site().get_latest_etag_from_site()
			newsFeed = feedparser.parse(rss_site().getUrl())
			###Try and find e-tag
			if hasattr(newsFeed, 'etag'):
				e_tag = newsFeed.etag	
			elif hasattr(newsFeed, 'feed'):
				if hasattr(newsFeed.feed, 'etag'):
					e_tag = newsFeed.feed.etag	
				else: 
					e_tag = None	
			else:
				e_tag = None
			

			if hasattr(newsFeed, 'modified'):
				modified = newsFeed.modified
				
			elif hasattr(newsFeed, 'feed'):
				if hasattr(newsFeed.feed, 'modified'):
					modified = newsFeed.feed.modified
				else: 	
					modified = None	
			else:
				modified = None

			if(site_state == None):
				rss_site().updateLatestRssInformation(e_tag, modified)	
				print("Site state is None")
				entries = newsFeed.entries
				for entry in entries:
					Notify(rss_site(), entry);
					pass
			else:
				rss_site().updateLatestRssInformation(e_tag, modified)
				feed_update = feedparser.parse(rss_site().getUrl(), etag=site_state['etag'], modified=site_state['date'])	
				if feed_update.status == 304:
					print("No changes")
				else:
					entries = feed_update.entries
					for entry in entries:
						Notify(rss_site(), entry);
				
			
	

