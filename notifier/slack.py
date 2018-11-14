from slackclient import SlackClient

class Slack:
	def __init__(self, slackAttachmentConfig):
		self.slackAttachmentConfig = slackAttachmentConfig
		self.token = 'aeae-545165484-564654654-23c90n4n0932hjdk'
		self.slackClient = SlackClient(self.token)
	
	def send_message(self, title, summary, author_name, link):
		self.slackClient.api_call("chat.postMessage",
				channel=self.slackAttachmentConfig.getChannel(),
				username=self.slackAttachmentConfig.getUsername(),
				parse='full',
				as_user=False,
				attachments=[
					        {
					            "color": self.slackAttachmentConfig.getColor(),
					            "author_name": author_name,
					            "title": title,
					            "title_link": link,
					            "text": summary + "....",
					            "thumb_url": self.slackAttachmentConfig.getThumbUrl(),
					            "footer": self.slackAttachmentConfig.getFooterText(),
					            "footer_icon": self.slackAttachmentConfig.getFooterIcon(),
					            "ts": 123456789
					        }
					    ]

			)