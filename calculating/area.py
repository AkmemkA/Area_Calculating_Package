import math


def calculate_circle(radius):
    """Функция для вычисления площади круга по радиусу
    :radius - int
    """
    if radius <= 0:
        raise ValueError("Радиус должен быть положительным числом")
    return round(math.pi * radius ** 2, 3)


def calculate_triangle(side1, side2, side3):
    """Функция для вычисления площади треугольника по трём сторонам
    :side1 - int
    :side2 - int
    :side3 - int
    """
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        raise ValueError("Длины сторон должны быть положительными числами")
    perimeter = (side1 + side2 + side3) / 2
    area = math.sqrt(perimeter * (perimeter - side1) * (perimeter - side2) * (perimeter - side3))
    return round(area, 3)


def right_triangle(side1, side2, side3):
    """Функция для проверки, является ли треугольник прямоугольным
    :side1 - int
    :side2 - int
    :side3 - int
    """
    sides = [side1, side2, side3]
    sides.sort()
    return math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2, rel_tol=0.01)

def calculate_unknown(shape, *params):
    """Метод для вычисления площади фигуры без знания типа фигуры
    :shape - str
    :parameters - int
    """
    if shape == "circle":
        return calculate_circle(*params)
    elif shape == "triangle":
        return calculate_triangle(*params)
    else:
        raise ValueError("Фигура не поддерживается")




