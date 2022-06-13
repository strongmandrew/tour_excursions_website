from bottle import route, view, post, template, request
import bottle
from datetime import datetime
import json
import os
import sys

@post('/user_review')
@view('reviews')
def review_form():
    mail = request.forms.get('MAIL')
    phone = request.forms.get('PHONE')
    review = request.forms.get('REVIEW')
    date = datetime.now()
    if (os.path.exists('reviews.txt')):
        with open('reviews.txt',encoding='utf8') as json_file:
            reviews = json.load(json_file)
    else:
        reviews = {}
    if (mail in reviews.keys()):
        reviews[mail]['phone'] = phone
        reviews[mail]['review'].append(review)
        reviews[mail]['date'].append(date.strftime("%x"))
    else:
        reviews[mail] = {'phone': phone, 'date': [date.strftime("%x")], 'review': [review]}
    print(reviews)
    with open('reviews.txt', 'w', encoding='utf8') as outfile:
        json.dump(reviews, outfile)
    return template('reviews')
    

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/articles')
@view('articles')
def nov_page():
    return template('articles')
