
from flask import Flask,request ,render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)

app.debug = True

app.config['SECRET_KEY'] = "ThisHappy123"
debug = DebugToolbarExtension(app)

@app.route('/')
def questions():
    """generate and show form to ask words"""
    prompts = story.prompts
    
    return render_template("questions.html",prompts=prompts)

@app.route('/story')
def show_story():
    text=story.generate(request.args)
    return render_template('story.html',text=text)