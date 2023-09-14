
______

<H3>
    Тестовое задание
</H3>

---

Для проверки можно запустить базу данных из докер-контейнера

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

