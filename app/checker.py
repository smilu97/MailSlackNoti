# -*- coding: utf8 -*-

import time

from .mail import get_last_mail

from email.utils import parsedate
from datetime import datetime


def work_check(users, slack):

	while True:
		for idx, user in enumerate(users):
			try:
				last_mail = get_last_mail(user.host, user.username, user.password)
			except Exception as e:
				print 'Failed to receive last mail of {}: {}'.format(user.username, str(e))
				continue

			if not last_mail:
				continue

			last_mail_id = last_mail.id if last_mail else 'None'

			if user.prev_mail_id == '':
				user.prev_mail_id = last_mail_id

			elif user.prev_mail_id != last_mail_id:

				mail_date = datetime(*(parsedate(last_mail.mail_date)[:6]))
				print 'found change on {} : {}'.format(user.channel, mail_date)
				if (datetime.now() - mail_date).total_seconds() < 300:

					noti_msg = last_mail.compose_noti_msg()

					try:
						slack.post_message(user.channel, noti_msg, as_user=True)
						print 'Sent {} in {}'.format(last_mail.mail_subject, user.channel)
					except Exception as e:
						print 'Failed to post slack message: {}'.format(str(e))

				user.prev_mail_id = last_mail_id

		time.sleep(10)

def check_periodically(users, slack, noti_room):
	while True:
		try:
			work_check(users, slack)
		except Exception as e:
			error_msg = 'Critical error: {}'.format(str(e))
			print error_msg
			slack.post_message(noti_room, error_msg, as_user=True)

		time.sleep(300)