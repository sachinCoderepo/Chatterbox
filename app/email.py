
from flask import render_template
from . import mail



# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
import requests
def send_email(to, subject, template,**kwargs):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox9d1db8a2773143c3bb9abc1cfc6fb597.mailgun.org/messages",
		auth=("api", "99d99427193c3b935e7ebd37bef32bfb-b36d2969-de178daa"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox9d1db8a2773143c3bb9abc1cfc6fb597.mailgun.org>",
			"to": to,
			"subject": subject,
			"text": render_template(template + '.txt', **kwargs),
            "html":render_template(template + '.html', **kwargs) })



# def send_email(to, subject, template, **kwargs):
#     app = current_app._get_current_object()
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#     msg.body = render_template(template + '.txt', **kwargs)
#     msg.html = render_template(template + '.html', **kwargs)
#     thr = Thread(target=send_async_email, args=[app, msg])
#     thr.start()
#     return thr