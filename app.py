#import modules
# from datetime import datetime
from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required

#create application object instance
app = Flask(__name__)
#configure encryption key
app.config['SECRET_KEY'] = 'OpenSesame'

#application instance passed to the constructor
manager = Manager(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
#defines class for form field input
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500


#run application instance
if __name__ == '__main__':
    manager.run()