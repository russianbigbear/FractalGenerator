from tkinter import *
from Algo import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import scrolledtext

window = Tk()
tabs = ttk.Notebook(window)
tab_ifs = ttk.Frame(tabs)
tab_ite = ttk.Frame(tabs)
back1 = Label(tab_ifs)
back2 = Label(tab_ite)

# Вывод картинки
def init_img():
    img1 = Image.open("IFS1.png")
    img2 = Image.open("IFS2.png")

    render1 = ImageTk.PhotoImage(img1)
    render2 = ImageTk.PhotoImage(img2)

    back1.configure(image=render1)
    back2.configure(image=render2)
    back1.image = render1
    back2.image = render2
    back1.pack()
    back2.pack()

    tabs.pack(expand=2, fill="both")


# Вызов Папоротника Барнсли
def clk_btn1():
    IFS_method(fern())
    window.geometry(size)
    init_img()


# Вызов дракона 1
def clk_btn2():
    IFS_method(dragon_f())
    window.geometry(size)
    init_img()


# Вызов дракона 2
def clk_btn3():
    IFS_method(dragon_s())
    window.geometry(size)
    init_img()


# Вызов C фрактала
def clk_btn4():
    IFS_method(fractal_c())
    window.geometry(size)
    init_img()


# Вызов фрактальной решетки
def clk_btn5():
    IFS_method(fractal_grid())
    window.geometry(size)
    init_img()


def clk_gen(text_field, wind):
    text = text_field.get('1.0', END + '-1c')
    tmp = [float(item) for item in text.split()]
    matrix = []

    for i in range(int(tmp[0])):
        matrix.append([])
        for j in range(7):
            matrix[i].append(tmp[(7*i) + j + 1])

    wind.destroy()

    IFS_method(matrix)
    window.geometry(size)
    init_img()


def generator():
    gen = Tk()
    gen.title("Создание своей матрицы")
    gen.geometry("512x512")
    gen.resizable(False, False)

    txt = scrolledtext.ScrolledText(gen, width=63, height=30)
    txt.insert(INSERT, "Введите в первую строку количество строк в будущей матрицы"
                       "\nНиже заполните значение матрицы, в которой должно быть:\n"
                       "- семь столбцов\n"
                       "- две и больше строк\n"
                       "- сумма значений последнего стобца равна 1\n")
    txt.grid(column=0, row=1)

    btn = Button(gen, text="Сгенерировать!",  font=("Comic Sans MS", 9, "italic"), command= lambda: clk_gen(txt, gen))
    btn.grid(column=0, row=2)

    gen.mainloop()


def home():
    img = Image.open("back.jpg")
    render = ImageTk.PhotoImage(img)

    back1.configure(image=render)
    back2.configure(image=render)
    back1.image = render
    back1.image = render
    back1.pack()
    back2.pack()
    tabs.pack(expand=2, fill="both")


def main():
    window.title("Генератор изображений на основе СИФ")
    window.geometry("512x512")
    window.resizable(False, False)

    tabs.add(tab_ifs, text="Обычный СИФ фрактал")
    tabs.add(tab_ite, text="СИФ фрактал в цвете")
    tabs.pack(expand=2, fill="both")

    menu = Menu(window)
    examples = Menu(menu)
    examples = Menu(menu, tearoff=0)
    examples.add_command(label="Папоротник Барнсли",  font=("Comic Sans MS", 9, "italic"), command=clk_btn1)
    examples.add_separator()
    examples.add_command(label="Морской дракон",  font=("Comic Sans MS", 9, "italic"), command=clk_btn2)
    examples.add_separator()
    examples.add_command(label="Кораллы",  font=("Comic Sans MS", 9, "italic"), command=clk_btn3)
    examples.add_separator()
    examples.add_command(label="Фрактал С",  font=("Comic Sans MS", 9, "italic"), command=clk_btn4)
    examples.add_separator()
    examples.add_command(label="Фрактальная решетка",  font=("Comic Sans MS", 9, "italic"), command=clk_btn5)
    menu.add_cascade(label="Примеры фракталов", menu=examples)
    menu.add_command(label="Генератор изображения", command=generator)
    menu.add_command(label="Главная", command=home)
    window.config(menu=menu)

    home()
    window.mainloop()


if __name__ == "__main__":
    main()

