from flask import Flask
from multiprocessing import Value
import os
import socket


counter = Value("i", 0)

app = Flask(__name__)

@app.route('/')
def hello():
    name = 'world'
    hostname = socket.gethostname()

    html = f"""
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    <b>Counter:</b> {counter.value}<br>
    """
    return html


@app.route('/stat')
def stat():
    counter.value += 1
    return hello()


@app.route('/about')
def about():
    name = os.getenv("NAME", 'world')
    hostname = socket.gethostname()

    html = f"""
    <h1>Hello, {name}!</h1> 
    <b>Hostname:</b> {hostname} <br>
    <b>Counter:</b> {counter.value}<br>
    """
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)