import redis
from redisworks import Root
import configparser
import json

class Redis():
	def __init__(self):
		config = configparser.RawConfigParser(allow_no_value=True)
		config.read("config/database.cfg")
		redis_host = config.get("Redis", "host")
		redis_port = config.get("Redis", "port")
		redis_password = config.get("Redis", "password")
		self.redis_db = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, db=0)
		self.root = Root(self.redis_db)

	def fetch_latest_by(self, tablename, where, orderBy, url):
		root = Root()
		result = root[url]
		print(result)
		return result
		
	def insert(self, tablename, columns, values):
		root = Root()
		if values[1] == None:
			values[1] = "None"
		if values[2] == None:
			values[1] = "No date"
			
		root[values[0]] = {"etag": values[1], "date": values[2], "url": values[0]}
