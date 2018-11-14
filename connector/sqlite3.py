import sqlite3
class SqlIte3():
	def __init__(self):
		self.db_connection = sqlite3.connect('rss.sqlite')
		self.db_connection.row_factory = sqlite3.Row
		self.db = self.db_connection.cursor()
		self.db.execute('CREATE TABLE IF NOT EXISTS rss (site TEXT, etag TEXT, date TEXT)')

	def fetch_latest_by(self, tablename, where, orderBy):
		print("select * from %s where %s order by %s desc" % (tablename, where, orderBy))
		result = self.db.execute("select * from %s where %s order by %s desc" % (tablename, where, orderBy))
		
		result = result.fetchone();
		type(result);
		return result;

	def insert(self, tablename, columns, values):
		length=len(columns)
		parameters=['?']*length
		query='insert into ' + tablename + ' ('+','.join(columns)+') values ('+','.join(parameters)+')'
		self.db.execute(query,values)
		self.db_connection.commit()
