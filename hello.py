# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired
# from flask_bootstrap import Bootstrap
# from flask import Flask, render_template,session, redirect, url_for, flash
# from flask_moment import Moment
# from datetime import datetime
# import os
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_mail import Mail
# from flask_mail import Message




# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
# 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# mail = Mail(app)


# # for mail
# app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
# app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
# app.config['FLASKY_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
# app.config['FLASKY_MAIL_SENDER'] = 'Flasky Admin <sachindwivedi772@gmail.com>'


# class Role(db.Model):
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role', lazy='dynamic')
#     def __repr__(self):
#         return '<Role %r>' % self.name
    
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), unique=True, index=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#     def __repr__(self):
#         return '<User %r>' % self.username


# # app = Flask(__name__)
# app.config['SECRET_KEY'] = 'hard to guess string'
# bootstrap = Bootstrap(app)
# moment = Moment(app)
# def send_async_email(app, msg):
#     with app.app_context():
#         mail.send(msg)
# def send_email(to, subject, template, **kwargs):
#         msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
#         sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
#         msg.body = render_template(template + '.txt', **kwargs)
#         msg.html = render_template(template + '.html', **kwargs)
#         mail.send(msg)
# class NameForm(FlaskForm):
#     name = StringField('What is your name?', validators=[DataRequired()])
#     submit = SubmitField('Submit')
#     app.config['FLASKY_ADMIN'] = os.environ.get('FLASKY_ADMIN')
    
#     @app.route('/', methods=['GET', 'POST'])
#     def index():
#         name = "sachin"
#         form = NameForm()

#         if form.validate_on_submit():
#             user = User.query.filter_by(username=form.name.data).first()
#             old_name = session.get('name')
#             if user is None:
#                 user = User(username=form.name.data)
#                 db.session.add(user)
#                 db.session.commit()
#                 session['known'] = False
#                 if app.config['FLASKY_ADMIN']:send_email(app.config['FLASKY_ADMIN'], 'New User',
#                     'mail/new_user', user=user)
#             else:
#                 session['known'] = True
#                 session['name'] = form.name.data
#                 form.name.data = ''

#             if old_name is not None and old_name != form.name.data:
#                 flash('Looks like you have changed your name!')
#             session['name'] = form.name.data
#             return redirect(url_for('index'))
#         return render_template('index.html',
#             form = form, name = session.get('name'),current_time=datetime.utcnow(),
#             known=session.get('known', False))


#     @app.route('/user/<name>')
#     def user(name):
#         return render_template('user.html', name="name")



#     @app.errorhandler(404)
#     def page_not_found(e):
#         return render_template('404.html'), 404

#     @app.errorhandler(500)
#     def internal_server_error(e):
#         return render_template('404.html'), 500


#     @app.shell_context_processor
#     def make_shell_context():
#         return dict(db=db, User=User, Role=Role)
    




    


s = "hellO world"
vol= ["a","e","i","o","u"]
v = 0
c = 0
res = ""
for i in s:
    if i in vol:
        res= res+"#"
        v +=1
    else:
        c +=1
        res += i

print(v,c,res)

