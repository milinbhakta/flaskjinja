from flask import Flask, url_for;
from hello import app

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
@app.route('/create')
def create():
    return "<h2>this is my first page!!!</h2>"


#server/question/<title>
@app.route('/question/<title>')
def question(title):
    return "<h2>"+ title +"</h2>";
