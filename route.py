from flask import Flask, url_for, request, render_template;
from hello import app
import os
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
        nh = open("data.txt","w")
        nh.write(answer)
        nh.close()
        nh1 = open("ques.txt","w")
        nh1.write(question)
        nh1.close()
        return render_template('CreatedQuestion.html', question = question);
    else:
        return "invalid request </h2>"

#server/question/<title>
@app.route('/question/<title>', methods=['GET','POST'])
def question(title):
    if request.method == 'GET':
        #send the user form
        #read question from data store
        nh1 = open("ques.txt","r")
        ques = nh1.read(20)
        nh1.close()
        return render_template('AnswerQuestion.html',question = ques)
    elif request.method == 'POST':
        #user has qttempted question. Check if they're correct
        submittedAnswer = request.form['submittedAnswer']

        #read answer from th data store
        nhr = open("data.txt","r")
        ans = nhr.read(20)
        nhr.close()

        if submittedAnswer == ans :
            return render_template('correct.html')
        else:
            return render_template('incorrect.html', submittedAnswer = submittedAnswer, Answer = ans)
    else:
        return "<h2>invalid request</h2>";
