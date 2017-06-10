# -*- coding: utf8 -*-

import poplib, email, mimetypes

from email import Header

class Mail(object):

	def __init__(self, mail_from, mail_to, mail_subject, mail_date, mail_content=None):
		self.mail_from = mail_from
		self.mail_to = mail_to
		self.mail_subject = mail_subject
		self.mail_date = mail_date
		self.mail_content = mail_content

		self.id = '{}{}{}{}'.format(mail_date, mail_from, mail_to, mail_subject)


	def compose_noti_msg(self):
		return 'From: {}\nTitle: {}'.format(self.mail_from, self.mail_subject)

def decode_header(header_msg):
	result = Header.decode_header(header_msg)
	return ''.join(t[0] for t in result)

def get_last_mail(host, username, password):
	try:
		mbox = poplib.POP3(host)

		mbox.user(username)
		mbox.pass_(password)
	except Exception as e:
		raise Exception('Login fail: {}:{} in {}\n{}'.format(username, password, host, str(e)))
		return

	msg_num, t_size = mbox.stat()

	try:
		server_msg, body, octets = mbox.retr(msg_num) # Retrieve last mail
		msg = email.message_from_string('\n'.join(body))

		mail_from    = decode_header(msg['from'])
		mail_to      = decode_header(msg['to'])
		mail_subject = decode_header(msg['subject'])
		mail_date    = msg['date']

		return Mail(mail_from, mail_to, mail_subject, mail_date)
	except Exception as e:
		raise Exception('Failed to receive mail: {}'.format(str(e)))

	try:
		mbox.quit()
	except:
		pass

