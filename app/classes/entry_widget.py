from tkinter import Entry


class EntryWidget(Entry):
    """Виджет: поле ввода"""

    def read_text(self):
        """Читать текст из поля"""
        text = super().get()
        if text:
            self.delete(0, 'end')
            return text
        return None
