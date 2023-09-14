from tkinter import Listbox


class ListBoxWidget(Listbox):
    """Виджет: текстовое поле"""

    def write(self, list_task):
        """Стирает всё и заново выводит"""
        super().delete(0, 'end')
        for task in list_task:
            super().insert('end', task[1])
