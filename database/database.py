import psycopg2
from psycopg2 import errors
from database.settings import config


class DBManager:
    db_name = 'tkinter_tasks'

    def create_db(self):
        """Создать БД"""
        connector = psycopg2.connect(dbname='postgres', **config.get_config_db())
        connector.autocommit = True
        cursor = connector.cursor()

        try:
            cursor.execute(f'CREATE DATABASE {self.db_name}')
            self.__create_table()
        except psycopg2.errors.DuplicateDatabase:
            print('Подключение к БД выполнено')

        cursor.close()
        connector.close()

    def __create_table(self):
        """Создать таблицу в БД"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        with connector.cursor() as cursor:
            cursor.execute("CREATE TABLE tasks (Id SERIAL PRIMARY KEY, name_task text NOT NULL)")
        connector.commit()
        connector.close()

    def add_task(self, task):
        """Добавить задачу в таблицу"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            try:
                cursor.execute(
                    "INSERT INTO tasks (name_task) VALUES (%s)", (task,)
                )
            except psycopg2.errors.UniqueViolation:
                print('error')

        connector.commit()
        connector.close()

    def read_tasks(self):
        """Читать задачи"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            cursor.execute("SELECT * FROM tasks ORDER BY Id")
            data = cursor.fetchall()

        connector.commit()
        connector.close()
        return data

    def drop_task(self, pk):
        """Удалить задачу"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            delstatmt = "DELETE FROM tasks WHERE Id = '%s'" % (pk,)
            cursor.execute(delstatmt)

        connector.commit()
        connector.close()

    def change_task(self, pk, text):
        """Изменить задачу"""
        connector = psycopg2.connect(dbname=self.db_name, **config.get_config_db())
        connector.autocommit = True
        with connector.cursor() as cursor:
            delstatmt = "UPDATE tasks SET name_task = '%s' WHERE Id = '%s'" % (text, pk)
            cursor.execute(delstatmt)

        connector.commit()
        connector.close()
