from bottle import route, view, template, post, request
from datetime import datetime
import routes
import re

@post('/submit_article', method='post')
def check_article():
    mail = request.forms.get('mail_field').strip()
    brief_name = request.forms.get('brief_field').strip()
    url = request.forms.get('url_field').strip()
    significance = request.forms.get('significance_combo')
    description = request.forms.get('desc_field').strip()
    if (len(brief_name)) != 0 & (len(description) != 0):
        if isUrlValid(url):
            if isMailValid(mail):
                file = open('./static/data/userArticles.txt', 'a')
                res = mail + ";" + brief_name + ";" + url + ";" + significance + ";" + description + "\n"
                file.write(res)
                file.close()
                return brief_name
            else:
                return "Your mail is invalid"
        else:
            return "Article URL is invalid"
    else:
        return "Fill in all the fields!"
   

def isUrlValid(url):
    url_pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    if re.match(url_pattern, url):
        return True
    else:
        return False

def isMailValid(mail):
    mail_pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})+$'
    if re.match(mail_pattern, mail):
        return True
    else:
        return False



