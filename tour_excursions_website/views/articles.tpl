<!DOCTYPE html>
<html style="font-size: 16px;" lang="en-GB">
  <head>
  <!Подключение всем файлов разметки css и скриптов js, а также иконки  >
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Latest novelties</title>
    <link rel="stylesheet" href="./static/content/articles.css">
    <link rel="icon" href="./static/images/logo_1.png">
    </head>
  <body>
    <h1 class="add-article">Form to add an article</h1>
    <form action="/submit_article" method="post">
        <p>Brief name:</p><input name="brief_field" type="text"></input>
        <p>URL:</p><input name="url_field" type="text"></input>
        <br>
        <br>
        <select name="significance_combo">
            <option disabled>Choose priority</option>
            <option>High priority</option>
            <option>Medium priority</option>
            <option>Low priority</option>
        </select>
        <p>Description:</p><textarea name="desc_field"></textarea>
        <br>


        <input value="Submit" type="submit"></input>
        

    </form>
    
    <h3>Latest articles</h3>
    <br>


    %file = open("./static/data/userArticles.txt", "r")
    %article_lines = [line.strip() for line in file]
    %for line in article_lines:
        <div class="border-article">
    %temp_line = line.split(";")
        {% if temp_line[2] == "High priority" %}
            <p class="high-priority-article">{{temp_line[0]}}</p>
        {% elif temp_line[2] == "Medium priority" %}
            <p class="medium-priority-article">{{temp_line[0]}}</p>
        {% else %}
            <p class="low-priority-article">{{temp_line[0]}}</p>
        {% end if %}
        <p>{{temp_line[1]}}</p>
        <p>{{temp_line[3]}}</p>
            
        </div>
        <br>

    %file.close()

  </body>
</html>