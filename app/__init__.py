# -*- coding: utf8 -*-

from arguments import USERS, SLACK_TOKEN, NOTI_ROOM

from .checker import check_periodically
from .slack import Slack
from .user import User

def main(args):
	print 'running services...'

	try:
		frog_slack = Slack(SLACK_TOKEN)
		users = [User(*i) for i in USERS]

		check_periodically(users, frog_slack, NOTI_ROOM)
	except Exception as e:
		print 'Level3 Error: {}'.format(str(e))