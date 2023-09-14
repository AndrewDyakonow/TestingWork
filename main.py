from app.window import create_window, draw_widget


def main():
    window = create_window()
    draw_widget(window)
    window.mainloop()


if __name__ == '__main__':
    main()
