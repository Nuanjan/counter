import os
from flask import Flask, render_template, request, redirect, session
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECEST_KEY', 'for dev')


@app.route('/')
def visit():
    if 'visited' in session:
        session['visited'] += 1
    else:
        session['visited'] = 1
    return render_template('index.html', counter=session['visited'])


@app.route('/detroy_session')
def destroy_session():
    session.clear()
    return redirect('/')


@app.route('/count', methods=['GET'])
def show_count():
    if 'visited' in session:
        session['visited'] += 2
    else:
        session['visited'] = 1
    return render_template('count.html', counter=session['visited'])


if __name__ == "__main__":
    app.run(debug=True)
