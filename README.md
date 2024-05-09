## Описание
Тестовое задание на должность бекэнд-разработчика компании Центрсофт Solution

Автор:
* Анастасия Гречкина (Github beluza-n, telegram @beluza_n)


## Стэк:
* Python
* Django
* SQLite


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:beluza-n/school_library.git
```

```
cd school_library
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/Scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Перейти на http://127.0.0.1:8000/books (пункт 1 про SQL-запрос)
или на http://127.0.0.1:8000/assets (пункт 4 про активы)