class SlackConfig(object):
	def __init__(self, object):
		self.color = object['color'];
		self.thumb_url = object['thumb_url'];
		self.footer_text = object['footer_text'];
		self.fotter_icon = object['fotter_icon'];
		self.username = object['username'];
		self.channel = object['channel'];
		
	def getColor(self):
		return self.color;

	def getThumbUrl(self):
		return self.thumb_url;

	def getFooterText(self):
		return self.footer_text;

	def getFooterIcon(self):
		return self.fotter_icon;

	def getUsername(self):
		return self.username;

	def getChannel(self):
		return self.channel;
