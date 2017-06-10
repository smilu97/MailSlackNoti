# -*- coding: utf8 -*-


class User:
	def __init__(self, host, username, password, channel):
		self.host = host
		self.username = username
		self.password = password
		self.channel = channel
		self.prev_mail_id = ''