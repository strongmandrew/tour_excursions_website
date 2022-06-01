<!DOCTYPE html>
<html style="font-size: 16px;" lang="en-GB">
  <head>
  <!Подключение разметки css, а также иконки  >
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>Latest articles</title>
    <link rel="stylesheet" href="./static/content/articles.css">
    <link rel="icon" href="./static/images/logo_1.png">
    </head>
  <body>
  
    <h1 class="add-article">Form to add an article</h1>

    <!Форма для для добавления новых статей >
    <form action="/submit_article" method="post">
        <p>Your mail:</p><input name="mail_field" type="text"></input>
        <p>Title:</p><input name="brief_field" type="text"></input>
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

    <! Открытие файла на чтение >
    %file = open("./static/data/userArticles.txt", "r")

    <! Считывание построчно>
    %article_lines = [line.strip() for line in file]
    %for line in article_lines:

        <! Создаю блок для записи в него информации о статье>
        <div class="border-article">
    %temp_line = line.split(";")
        % color = "red"

        <! градация статей по приоритету осуществляется с поммощью установления свойства прозрачности>
        <% if temp_line[3] == "High priority": %>
            % opacity = 1
            
        <% elif temp_line[3] == "Medium priority": %>
            % opacity = 0.6
        <% else: %>
            % opacity = 0.3
        <% end %>
        <h2 style="color: {{color}};opacity: {{opacity}};" class="brief-name">{{temp_line[1]}}</h2>

        <! Вывожу только первые 250 символов описания, чтобы не перегружать блок текстом>
        <p class="desc-article">{{temp_line[4][0:250]}}...</p>
        <div class="url-info">

        <! ссылка на полноценную статью> 
        <p>Read the entire article at <a href="{{temp_line[2]}}">{{temp_line[2]}}</a> </p>
        
        </div>
        <p class="date-article">{{temp_line[5]}}</p>
        </div>
        <br>

    %file.close()

  </body>
</html>