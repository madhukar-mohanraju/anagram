'''
Created on 26-May-2018

@author: Madhukar
'''

from flask import Flask, render_template, request
import itertools
import logging
file_handler = logging.FileHandler('/var/tmp/app.log')

app = Flask(__name__)

app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

def getAnagram(value):
    #value_arr = []
    output = ["".join(combo) for combo in itertools.permutations(value)]
    return ",".join(elem for elem in set(output))

@app.route('/')
def hello():
    app.logger.info(request)
    if request.method == 'GET':
        if 'name' in request.args:
            return render_template('index.html', username=request.args['name'])
        else:
            return 'Hello Everyone!!!'
    
@app.route('/anagram', methods = ['GET', 'POST'])
def anagram():
    if request.method == 'GET':
        app.logger.info(request)
        if 'userinput' in request.args:
            text = request.args['userinput']
            out = getAnagram(text.lower())
            return render_template('anagram.html', anagram_out=out)
        else:
            return render_template('anagram.html', anagram_out=None)
    if request.method == 'POST':
        app.logger.info(request)
        text = request.form['userinput']
        out = getAnagram(text.lower())
        return render_template('anagram.html', anagram_out=out)
        #return out

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

if __name__ == "__main__":
    app.debug = False
    app.run()