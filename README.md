## session_service

### Процесс загрузки на тестовый сервер

При первом развертывании приложения необходимо синхронизировать файлы приложения с файлами на сервере.

Например, находясь в директории проекта `session_service` на компьютере разработчика:

`rsync -avF --filter=':- .gitignore' --exclude '.git' . developer@ip_addr:/home/developer/miigaik_practice/session_service`

Затем, на сервере, внутри директории проекта `sesion_service` необходимо создать виртуальное окружение:

`python3 -m venv venv`

А затем, необходимо его активировать и установить зависимости:

`source venv/bin/activate`
`python -m pip install -r requirements.txt`

Из файла `session_service/config.example.ini` необходимо создать файл конфигурации `session_service/config.ini` и заполнить следующие настройки:

```
[server]

SESSION_FILE_DIR = /home/developer/miigaik_practice/flask_session

[uwsgi]

mount = /auth=wsgi:app
manage-script-name = true

socket = /home/developer/miigaik_practice/session_service.socket
chmod-socket = 660

die-on-term = true
```

_В случае, если пути в вашей системе отличаются, то необходимо учитывать это._

### Создание сервиса приложения

Для того, чтобы приложение работало в фоновом режиме, как сервис, необходимо создать файл (с правами суперпользователя) для `systemd` по пути: 

`/etc/systemd/system/session_service.service`

со следующим содержанием:

```
[Unit]
Description=Session service for deans office portal
After=network.target

[Service]
User=developer
Group=www-data

WorkingDirectory=/home/developer/miigaik_practice/session_service
Environment="PATH=/home/developer/miigaik_practice/session_service/venv/bin"
ExecStart=/home/developer/miigaik_practice/session_service/venv/bin/uwsgi --ini session_service/config.ini

[Install]
WantedBy=multi-user.target
```

После этого необходимо запустить сервис:

`sudo systemctl start session_service.service`

### Конфигурация веб-сервера nginx

В случае, если веб-сервер `nginx` не установлен:

`sudo apt install nginx`

Необходимо создать конфигурационный файл `nginx`: `/etc/nginx/sites-available/miigaik_practice`

Со следующим содержимым:

```
server {
	listen 80;
	server_name deans.office;

	location /auth {
		include uwsgi_params;
		uwsgi_pass unix:/home/developer/miigaik_practice/session_service.socket;
	}

}
```

Затем, необходимо создать ссылку на файл в директории `sites-enabled` и перезапустить сервис `nginx`:

```
sudo ln -s /etc/nginx/sites-available/miigaik_practice /etc/nginx/sites-enabled
sudo service nginx restart
```


### Добавление доменного имени в файл hosts

Для того, чтобы сайт был доступен по доменному имени `deans.office` необходимо отредактировать файл `hosts` на своей локальной машине.
