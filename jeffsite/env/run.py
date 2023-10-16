from flask import Flask,\
redirect, url_for, request,\
render_template
from sqlalchemy import create_engine, Column, Integer, \
String



app = Flask(__name__)

# db = SQLAlchemy()
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:/hell.db"
# db.init_app(app)

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)

@app.route('/')
def index():
    website_name = "Jeff's Site"

    return render_template('/blah.html', title = website_name)

@app.route('/hello/<name>')
def hello_name(name):
   return 'Hello %s!' % name

@app.route('/success/<name>')
def success(name):
    dict = []

    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        # return render_template('/blah.html', title = website_name)

        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        # return redirect(url_for('success', name=user))
        return render_template('/login.html', name = user)


if __name__ == '__main__':
    app.run(debug=True)