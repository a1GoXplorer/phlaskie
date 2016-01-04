#import dependencies
from flask import Flask, request, render_template
# from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

#create application object instance
app = Flask(__name__)

#application instance passed to the constructor
# manager = Manager(app)

#application instance is passed to the constructor
bootstrap = Bootstrap(app)

# @app.route('/')
# def index():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is %s</p>' % user_agent

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
  return render_template('500.html'), 500


#run application instance
if __name__ == '__main__':
    app.run(debug=True)