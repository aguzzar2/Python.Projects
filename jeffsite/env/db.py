from flask import Flask,\
redirect, url_for, request,\
render_template

from sqlalchemy import create_engine, String,\
Column, Integer, text



app = Flask(__name__)
'''lazy initialization... this engine will be managed by 
Session Object. Session transactional and executional ...
Sole purpose of ENGINE for user is provide unit of connectivity
to db called Connection object. which is exactly what it sounds like.
'''
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)



@app.route('/')
def index():
    return "you suck"

if __name__ == '__main__':
    app.run(debug=True)