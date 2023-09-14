
______

<H2>
    Тестовое задание
</H2>

---
<H3>
    Установка
</H3>

1. Установить зависимости:

```bash
    pip install -r requirements.txt
```

2. Установить Tkinter, если его нет

```bash
    sudo apt-get install python3-tk
```

---

3. Для проверки можно запустить базу данных из докер-контейнера

```bash
    docker-compose up --build
```

Либо отредактировать файл

```html
    test_tkinter/database/settings/db.ini
```

указав свои параметры подключения

```html
    [postgresql]
    host=127.0.0.1
    port=5400
    user=postgres
    password=188651
```

