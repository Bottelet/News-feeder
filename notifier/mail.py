import smtplib 
from email.mime.text import MIMEText
import configparser

class Mail:
	def __init__(self, mailConfig):
		self.mailConfig = mailConfig
		
	def send_message(self, article_title, article_summary, article_url):
	    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
	    smtp_server.ehlo()
	    smtp_server.starttls()
	    smtp_server.login('your@gmail.com', 'yourPassword123')
	    msg = MIMEText(f'\n {article_title}. \n {article_summary} \nYou can read it here {article_url}')
	    msg['Subject'] = self.mailConfig.getSubject()
	    msg['From'] = 'your@gmail.com'
	    msg['To'] = self.mailConfig.getToEmail()
	    smtp_server.send_message(msg)
	    smtp_server.quit()