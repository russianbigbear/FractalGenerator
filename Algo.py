"""Пакеты"""
import random
from collections import deque
from PIL import Image

"""
СИФ - это система итерируемых функций.
СИФ состоит из аффинных преобразований на плоскости,
которые задаются следущей системой уравнений:
X' = A*X + B*Y + E
Y' = C*X + D*Y + F
Каждая ситема - это СИФ-прелбразование.
Число таких систем должно быть не менее 2.

Удобнее использовать запись в виде матрицы со столбцами:
| A | B | C | D | E | F | G |
, где каждая строка - это система уравненей
, а G - вероятность выбора ситемы.
Назовем FRACTINT.
"""

size = ""


def fern():
    """FRACTINT IFS *Папоротник Барнсли* """
    return [[0.0, 0.0, 0.0, 0.16, 0.0, 0.0, 0.01],
            [0.85, 0.04, -0.04, 0.85, 0.0, 1.6, 0.85],
            [0.2, -0.26, 0.23, 0.22, 0.0, 1.6, 0.07],
            [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44, 0.07]]


def dragon_f():
    """FRACTINT IFS *Дракон 1* """
    return [[0.824074, 0.281482, -0.212346, 0.864198, -1.882290, -0.110607, 0.787473],
            [0.088272, 0.520988, -0.463889, -0.377778, 0.785360, 8.095795, 0.212527]]


def dragon_s():
    """FRACTINT IFS *Дракон 2* """
    return [[0.5, -0.5, 0.5, 0.5, 0.0, 0.0, 0.5],
            [-0.5, -0.5, 0.5, -0.5, 1.0, 0.0, 0.5]]


def fractal_c():
    """FRACTINT IFS *C фрактал* """
    return [[0.5, -0.5, 0.5, 0.5, 0.0, 0.0, 0.5],
            [0.5, 0.5, -0.5, 0.5, 0.5, 0.5, 0.5]]


def fractal_grid():
    """FRACTINT IFS *Фрактальная решетка* """
    return [[0.3, -0.3, 0.3, 0.3, 1, 1, 0.25],
            [0.3, -0.3, 0.3, 0.3, 1, -1, 0.25],
            [0.3, -0.3, 0.3, 0.3, -1, 1, 0.25],
            [0.3, -0.3, 0.3, 0.3, -1, -1, 0.25]]


def IFS_method(mat):
    """Отрисовка, используя метод IFS"""

    """
     Алгоритм построения СИФ-фрактала:
     1. Найти и закрасить начальную точку (X, Y) изображения (алгоритм поиска начальной точки приведен ниже).
     2. Выбрать, используя известные вероятности выбора, одно из СИФ-преобразований,
        найти координаты (X', Y') новой точки изображения и закрасить найденную точку.
     3. Принять X = X' и Y = Y'.
     4. Повторить п.п. 2 и 3 алгоритма заданное число раз.
     """

    """
    Алгоритм поиска начальной точки:
    1. Взять произвольную точку (X, Y) на плоскости.
    2. Выбрать, используя известные вероятности выбора,
       одно из СИФ-преобразований и найти координаты (X', Y') следующей точки.
    3. Принять X = X' и Y = Y'.
    4. Повторить п.п. 2 и 3 алгоритма заданное число раз (например, 100).
    5. Взять в качестве начальной точки последнюю точку.
    """

    # Размеры изображения
    _img_size_x = 512
    _img_size_y = 512
    iterations_count = 16

    m = len(mat)  # число преобразований IFS - число строк

    # найдем  xmin, xmax, ymin, ymax фрактала используя IFS алгоритм
    x = mat[0][4]
    y = mat[0][5]
    xa = x
    xb = x
    ya = y
    yb = y

    # поиск начальной точки
    for k in range(_img_size_x * _img_size_y):
        p = random.random()
        p_sum = 0.0
        for i in range(m):
            p_sum += mat[i][6]
            if p <= p_sum:
                break

        x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
        y = x * mat[i][2] + y * mat[i][3] + mat[i][5]
        x = x0

        if x < xa:
            xa = x
        if x > xb:
            xb = x
        if y < ya:
            ya = y
        if y > yb:
            yb = y

    # автоматически перенастраиваем соотношение сторон
    _img_size_y = int(_img_size_y * (yb - ya) / (xb - xa))
    _image = Image.new("RGB", (_img_size_x, _img_size_y), (83, 84, 81))

    # отрисовка, используя метод IFS
    x = 0.0
    y = 0.0
    for k in range(_img_size_x * _img_size_y):
        p = random.random()
        p_sum = 0.0
        for i in range(m):
            p_sum += mat[i][6]
            if p <= p_sum:
                break

        x0 = x * mat[i][0] + y * mat[i][1] + mat[i][4]
        y = x * mat[i][2] + y * mat[i][3] + mat[i][5]
        x = x0

        jx = int((x - xa) / (xb - xa) * (_img_size_x - 1))
        jy = (_img_size_y - 1) - int((y - ya) / (yb - ya) * (_img_size_y - 1))
        _image.putpixel((jx, jy), (17, 194, 132))

    size = str(_img_size_x) + "x" + str(_img_size_y)
    _image.save("IFS1.png", "PNG")

    # отрисовка с расскраской
    for ky in range(_img_size_y):
        for kx in range(_img_size_x):

            x = float(kx) / (_img_size_x - 1) * (xb - xa) + xa
            y = float(ky) / (_img_size_y - 1) * (yb - ya) + ya

            queue = deque([])
            queue.append((x, y, 0))

            # итерируем пока не закончатся точки
            while len(queue) > 0:
                (x, y, i) = queue.popleft()
                # применяем все обратные преобразования
                for j in range(m):
                    d = mat[j][0] * mat[j][3] - mat[j][2] * mat[j][1]
                    if d != 0.0:
                        x_new = ((x - mat[j][4]) * mat[j][3] - (y - mat[j][5]) * mat[j][1]) / d
                        y_new = ((y - mat[j][5]) * mat[j][0] - (x - mat[j][4]) * mat[j][2]) / d

                        if xa <= x_new <= xb and y_new >= ya <= yb:
                            if i + 1 == iterations_count:
                                break
                            queue.append((x_new, y_new, i + 1))

            _image.putpixel((kx, ky), (i % 8 * 10, i % 16 * 8, i % 6 * 8))

    _image.transpose(Image.ROTATE_180).save("IFS2.png", "PNG")


