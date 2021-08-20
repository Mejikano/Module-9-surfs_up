from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello world'

@app.route('/skilldrill')

def skill_drill():
    return 'Skill Drill Route'