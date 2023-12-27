from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# create an instance of a Flask app (referencing this file)
app = Flask(__name__)
# three "/": relative path; four is absolute
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)  # initialize database


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')  # route called by user
def index():  # function called by '/' route
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)  # starts the web app at port 8000
