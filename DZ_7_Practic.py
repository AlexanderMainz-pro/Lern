import tkinter
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir='/',
                                          title='выберите файл', filetypes=(('Текстовый файл', '.txt'),
                                                ('все файлы', '*')))

window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x350')
window.configure(bg='black')
window.resizable(False, False) #запрещаем менять размеры окна
text = tkinter.Label(window, text='Файл:', height=10, width=5, background='silver',
                     foreground='blue')
text.grid(colums=1, row=1)
button_select = tkinter.Button(window, width=5, height=3, text='Выберите файл', background='silver',
                               foreground='blue')
window.mainloop() #постоянное обовление окна
