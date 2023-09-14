import tkinter
import tkinter.ttk
from app.classes.listbox_widget import ListBoxWidget
from app.tools import label_main_param, btn_params, list_params, frame_params
from app.classes.entry_widget import EntryWidget
from app.distributor import Distributor


def create_window():
    """Окно программы"""
    window = tkinter.Tk()
    window.title('To Do App')
    window.geometry('750x450+10+10')
    window.resizable(True, True)
    window.minsize(400, 300)
    window.maxsize(1000, 1000)
    window.config(bg='#C0C0C0')
    return window
                                                     

def draw_widget(window):
    """Создание и отрисовка виджетов"""
    text_widget = tkinter.Label(window, **label_main_param)
    frame_main = tkinter.Frame(window, **frame_params)
    listbox_widget = ListBoxWidget(frame_main, **list_params)
    entry_widget = EntryWidget(frame_main, width=60)
    btn_add = tkinter.Button(
        window,
        text='Add',
        command=lambda: Distributor.add_click(entry_widget, listbox_widget),
        **btn_params
    )
    btn_delete = tkinter.Button(
        window,
        text='Delete',
        command=lambda: Distributor.delete_click(listbox_widget),
        **btn_params
    )

    btn_edit = tkinter.Button(
        window,
        text='Edit',
        **btn_params
    )

    btn_edit.config(
        command=lambda btn=btn_edit: Distributor.edit_click(
            entry_widget,
            listbox_widget,
            btn_add,
            btn_edit,
            btn_delete,
        )
    )

    text_widget.pack()
    frame_main.pack()
    entry_widget.pack()
    listbox_widget.pack()
    btn_add.pack()
    btn_edit.pack()
    btn_delete.pack()

    Distributor.create_database(listbox_widget)
