from flask import Flask
from threading import Thread
import random
import subprocess
import os

app = Flask('')


@app.route('/')
def home():
    return 'Im in!'


def run():
    print('starting...')
    subprocess.run([os.path.abspath(os.getcwd()) + '/sources/run'])
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))


def keep_alive():
    '''
	Creates and starts new thread that runs the function run.
	'''
    t = Thread(target=run)
    t.start()


if __name__ == '__main__':
    keep_alive()
