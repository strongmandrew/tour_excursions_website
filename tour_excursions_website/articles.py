from bottle import route, view, template, post, request
from datetime import date, datetime
import routes
import re

# обработка нажатия на кнопку отправки статьи
@post('/submit_article', method='post')
def check_article():
    #
    mail = request.forms.get('mail_field').strip()
    brief_name = request.forms.get('brief_field').strip()
    url = request.forms.get('url_field').strip()
    significance = request.forms.get('significance_combo')
    description = request.forms.get('desc_field').strip()
    # проверка введённых полей
    if (len(brief_name) != 0) & (len(description) != 0):
        # проверка валидности ссылки на статью
        if isUrlValid(url):
            # проверка валидности почты
            if isMailValid(mail):
                now_date = datetime.now()
                # запись в файл с разделителем ;
                file = open('./static/data/userArticles.txt', 'a')
                res = mail + ";" + brief_name + ";" + url + ";" + significance + ";" + description + ";" + now_date.strftime("%d.%m.%Y %H:%M") + "\n"
                file.write(res)
                file.close()
                return template('articles')
            else:
                return "Your mail is invalid"
        else:
            return "Article URL is invalid"
    else:
        return "Fill in all the fields!"
   

def isUrlValid(url):
    # паттерн URL-адреса
    url_pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
    if re.match(url_pattern, url):
        return True
    else:
        return False

def isMailValid(mail):
    # паттерн почты
    mail_pattern = r'^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})+$'
    if re.match(mail_pattern, mail):
        return True
    else:
        return False



