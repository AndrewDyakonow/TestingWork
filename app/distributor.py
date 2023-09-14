from tkinter.messagebox import showerror
from app.classes.entry_widget import EntryWidget
from app.classes.listbox_widget import ListBoxWidget
from database.database import DBManager


class Distributor:
    """Дистрибьютор"""
    dbconnect = DBManager()
    actual_list_task = []
    flag = None

    @classmethod
    def create_database(cls, listbox_widget):
        """Создать базу данных"""
        cls.dbconnect.create_db()
        ListBoxWidget.write(listbox_widget, cls.__read_tasks_in_db())

    @classmethod
    def add_click(cls, entry_widget, listbox_widget):
        """Обработка нажатия кнопки Add"""
        entry_text = EntryWidget.read_text(entry_widget)
        if entry_text:
            cls.dbconnect.add_task(entry_text)
            ListBoxWidget.write(listbox_widget, cls.__read_tasks_in_db())
        else:
            showerror('Ошибка!!!', 'Не введена задача')

    @classmethod
    def delete_click(cls, listbox_widget):
        """Обработка нажатия кнопки Delete"""
        choice_index = ListBoxWidget.curselection(listbox_widget)
        if choice_index:
            intresting = cls.__read_tasks_in_db()[choice_index[0]]
            cls.dbconnect.drop_task(intresting[0])
            ListBoxWidget.write(listbox_widget, cls.dbconnect.read_tasks())

    @classmethod
    def edit_click(
            cls,
            entry_widget,
            listbox_widget,
            btn_add,
            btn_edit,
            btn_delete,
    ):
        """Обработка нажатия кнопки Edit"""
        choice_index_tuple = ListBoxWidget.curselection(listbox_widget)
        if choice_index_tuple or cls.flag:
            if choice_index_tuple:
                choice_index = choice_index_tuple[0]
                cls.flag = choice_index
            else:
                choice_index = cls.flag
            choice_text = ListBoxWidget.get(listbox_widget, choice_index)
            if btn_edit.cget('text') == 'Edit':
                cls.__widget_status_edit(btn_add, btn_edit, btn_delete, listbox_widget)
                entry_widget.delete(0, 'end')
                entry_widget.insert(0, choice_text)
            else:
                new_text = EntryWidget.read_text(entry_widget)
                if new_text:
                    cls.__widget_status_save(btn_add, btn_edit, btn_delete, listbox_widget)
                    cls.dbconnect.change_task(cls.actual_list_task[choice_index][0], new_text)
                    ListBoxWidget.write(listbox_widget, cls.__read_tasks_in_db())
                else:
                    showerror('Предупреждение!!!', 'Введите новое название задачи')
        else:
            showerror('Ошибка!!!', 'Не выбрана задача')
            cls.__widget_status_save(btn_add, btn_edit, btn_delete, listbox_widget)
            entry_widget.delete(0, 'end')

    @classmethod
    def __read_tasks_in_db(cls):
        """Прочитать из БД и актуализировать список задач в классе"""
        cls.actual_list_task = cls.dbconnect.read_tasks()
        return cls.actual_list_task

    @classmethod
    def __widget_status_edit(cls, btn_add, btn_edit, btn_delete, listbox_widget):
        """Состояние виджетов при редактировании"""
        btn_add.config(state=["disabled"], bg='gray')
        btn_edit.config(text="Save")
        btn_delete.config(state=["disabled"], bg='gray')
        listbox_widget.config(state=["disabled"])

    @classmethod
    def __widget_status_save(cls, btn_add, btn_edit, btn_delete, listbox_widget):
        """Состояние виджетов при редактировании"""
        btn_add.config(state=["active"], bg='#1E90FF')
        btn_edit.config(text="Edit")
        btn_delete.config(state=["active"], bg='#1E90FF')
        listbox_widget.config(state=["normal"])
        cls.flag = None