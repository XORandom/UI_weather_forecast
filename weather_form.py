from tkinter import Button, Entry, Tk, Label, Text, END
from weather_request import get_request


class WeatherApp:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('350x330')
        self.window.title('Прогноз погоды')
        self.label = Label(text='Введите город:', font=('Times New Roman', 16))
        self.label.place(x=5, y=5)
        self.entry = Entry(width=30, font=('Times New Roman', 16))
        self.entry.place(x=5, y=50)
        self.text = Text(height=8, width=30, font=('Times New Roman', 16))
        self.text.place(x=5, y=100)
        self.button_run = Button(text='Выполнить', width=20, height=0, command=self.get_result)
        self.button_run.place(x=5, y=300)
        self.button_close = Button(text='Закрыть', width=20, height=0, command=self.window.destroy)
        self.button_close.place(x=190, y=300)
        self.window.mainloop()


    def get_result(self):
        self.text_clear()
        town = self.entry.get()
        self.text.insert(1.0, get_request(town))

    def text_clear(self):
        self.text.delete(1.0, END)

