from flask import render_template 
from app import app 
 
Василий='username'
@app.route('/') 
@app.route('/index') 
def index(): 
    user = {'username': 'Учитель'} 
    posts = [ 
        { 
            'author': {'username': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        }, 
        { 
            'author': {'username': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        },  
        { 
            'author': {'username': "Костя"}, 
            'body':'вы самый лучший преподаватель в МТУСИ' 
        } 
    ]  
    return render_template('index.html', title='Home', user=user, posts=posts) 