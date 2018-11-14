class MailConfig(object):
	def __init__(self, object):
		self.to = object['to'];
		self.subject = object['subject'];

	def getToEmail(self):
		return self.to;

	def getSubject(self):
		return self.subject;