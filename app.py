import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

app = Flask(__name__)



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'mysql://student:yiJmf7G9kiQ7Vth**@10.57.10.25:3306/mikrotik'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Inputs(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dispatcher = db.Column(db.String(15), nullable=False, default='0.0.0.0')
    ipaddress = db.Column(db.String(15), nullable=False, unique=True, default='0.0.0.0')
    ipversion = db.Column(db.Enum('IPv4','IPv6'), nullable=False)
    note = db.Column(db.String(255))

    def __repr__(self):
        return f'<IP adresa: {self.ipaddress}>'



@app.route('/')
def index():
    inputs = Inputs.query.all()
    return render_template('index.html', inputs=inputs)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        ipaddress = request.form['ipaddress']
        dispatcher = request.form['dispatcher']
        ipversion = request.form['ipversion']
        note = request.form['note']
        inputs = Inputs(ipaddress=ipaddress,
                          dispatcher=dispatcher,
                          ipversion=ipversion,
                          note=note)
        db.session.add(inputs)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:input_id>/edit/', methods=('GET', 'POST'))
def edit(input_id):
    input = Inputs.query.get_or_404(input_id)

    if request.method == 'POST':
        ipaddress = request.form['ipaddress']
        dispatcher = request.form['dispatcher']
        ipversion = request.form['ipversion']
        note = request.form['note']

        input.ipaddress=ipaddress
        input.dispatcher=dispatcher
        input.ipversion=ipversion
        input.note=note

        db.session.add(input)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('edit.html', input=input)


@app.post('/<int:input_id>/delete/')
def delete(input_id):
    input = Inputs.query.get_or_404(input_id)
    db.session.delete(input)
    db.session.commit()
    return redirect(url_for('index'))


