from flask import Flask, url_for, request, render_template;
from hello import app
import os
import redis

#connect to redis database
r = redis.StrictRedis(host = 'localhost', port=6379, db=0,charset="utf-8",decode_responses=True)
#server/
@app.route('/')
def hello_world():

    createlink = "<a href='" + url_for('create') + "'>create a question</a>";
    return """<html>
                    <head>
                        <title>Hello,Milin</title>
                    </head>
                    <body>
                        """ + createlink + """
                    </body>
                </html>""";

#server/create
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        #send the user the form
        return render_template('CreateQuestion.html')
    elif request.method == 'POST':
        #read form data and save it
        title = request.form['Title']
        question = request.form['Question']
        answer = request.form['Answer']
        #store data in datastorage
        #key name will be what ever they type in :Question
        r.set(title+':question',question)
        r.set(title+':answer',answer)

        return render_template('CreatedQuestion.html', question = question);
    else:
        return "invalid request </h2>"

#server/question/<title>
@app.route('/question/<title>', methods=['GET','POST'])
def question(title):
    if request.method == 'GET':
        #send the user form
        #read question from data store
        question = r.get(title+':question')

        return render_template('AnswerQuestion.html',question = question)
    elif request.method == 'POST':
        #user has qttempted question. Check if they're correct
        submittedAnswer = request.form['submittedAnswer']

        #read answer from th data store
        answer = r.get(title+':answer')

        if submittedAnswer == answer :
            return render_template('correct.html')
        else:
            return render_template('incorrect.html', submittedAnswer = submittedAnswer, Answer = answer)
    else:
        return "<h2>invalid request</h2>";
