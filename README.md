<b>Конфигурация проекта</b><br>
<ul>
<li>БД - postgress</li>
<li>ORM - Django</li>
<li>API - DRF</li>
</ul>

<b>Настройки:</b><br>
в файл .env необходимо заполнить своими настройками(DB) по примеру файла <b>example.txt</b></br>
</br>

<b>Старт проекта:</b><br>
<ol>
<li>
docker-compose build (создаем/импортируем образы) <br>
</li>
<li>
docker-compose up<br>
</li>
<li>
Опционально:</br>
docker compose run web python manage.py shell (вставляем тестовые данные из файла команды для shell.txt)
</li>
</ol>
<b>Дополнительно</b> <br>
Проект также может быть запущен обычным путем:<br>
python manage.py runserver<br>

<b>Эндпоинты:</b><br>
<ul>
<li>
http://127.0.0.1:8000/api/ - перечень всех эндпоинтов входящих в роутер API)
</li>
<li>
http://127.0.0.1:8000/api/swagger/ - документация к API)
</li>
<li>
http://127.0.0.1:5555/ - pg админ (для удобства отслеживания данных в бд, лог и пасс по умолчанию - pgadmin4@pgadmin.org, admin).</br>
Для подключения к БД нужно создать сервер, и ввести учетные данные из .env
</li>

</ul>

P.S. реализованы все задачи из ТЗ<br>
P.P.S. Что хотелось бы еще написать тесты , не успел т.к. старался сделать ТЗ в оговоренное время<br>
