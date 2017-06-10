# -*- coding: utf8 -*-

from slacker import Slacker


class Slack:
	def __init__(self, api_token):
		self.api_token = api_token
		self.slack = Slacker(api_token)
		try:
			print self.slack.auth.test()
		except:
			raise Exception('Invalid slack token')

	def post_message(self, *args, **kwargs):
		self.slack.chat.post_message(*args, **kwargs)