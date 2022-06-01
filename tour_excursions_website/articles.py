from bottle import route, view, template, post, request
from datetime import datetime
import routes

@post('/submit_article', method='post')
def check_Novelty():
    brief_name = request.forms.get('brief_field').strip()
    url = request.forms.get('url_field').strip()
    significance = request.forms.get('significance_combo')
    description = request.forms.get('desc_field').strip()


    file = open('./static/data/userArticles.txt', 'a')
    res = brief_name + ";" + url + ";" + significance + ";" + description + "\n"
    file.write(res)
    file.close()
    
    return brief_name

