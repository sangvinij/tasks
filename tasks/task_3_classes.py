'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.


class LengthUnits:
    def __init__(self, value, conv=1, v=None):
        if not isinstance(value, (int, float)):
            raise TypeError('invalid value type')
        self.value = value
        self.conv = conv
        self.v = v

    def __str__(self):
        return f"{self.value} {self.v}"

    def __eq__(self, other):
        sc = (other.value / other.conv) * self.conv
        return self.value == sc

    def __lt__(self, other):
        sc = (other.value / other.conv) * self.conv
        return self.value < sc

    def __add__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = (other.value / other.conv) * self.conv
        return f'{self.value + sc} {self.v}'

    def __iadd__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = (other.value / other.conv) * self.conv
        self.value += sc
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = (other.value / other.conv) * self.conv
        return f'{self.value - sc} {self.v}'

    def __isub__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = (other.value / other.conv) * self.conv

        self.value -= sc
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        return f'{self.value * sc} {self.v}'

    def __imul__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other

        self.value *= sc
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, LengthUnits)):
            raise TypeError('only int or LengthUnits')

        sc = other
        if not isinstance(other, (int, float)):
            sc = (other.value / other.conv) * self.conv
        return f'{self.value / sc} {self.v}'

    def __itruediv__(self, other):
        if not isinstance(other, (int, LengthUnits)):
            raise TypeError('only int or LengthUnits')

        sc = other
        if not isinstance(other, (int, float)):
            sc = (other.value / other.conv) * self.conv

        self.value /= sc
        return self


class Millimeters(LengthUnits):
    def __init__(self, value, conv=1000, v='mm'):
        super().__init__(value, conv, v)


class Centimeters(LengthUnits):
    def __init__(self, value, conv=100, v='cm'):
        super().__init__(value, conv, v)


class Meters(LengthUnits):
    def __init__(self, value, conv=100, v='m'):
        super().__init__(value, conv, v)


class Kilometers(LengthUnits):
    def __init__(self, value, conv=0.001, v='km'):
        super().__init__(value, conv, v)


class Inches(LengthUnits):
    def __init__(self, value, conv=39.3701, v='in'):
        super().__init__(value, conv, v)


class Feets(LengthUnits):
    def __init__(self, value, conv=3.28084, v='f'):
        super().__init__(value, conv, v)


class Yards(LengthUnits):
    def __init__(self, value, conv=1.09361, v='yd'):
        super().__init__(value, conv, v)


class Miles(LengthUnits):
    def __init__(self, value, conv=0.000621371, v='miles'):
        super().__init__(value, conv, v)


class Fen(LengthUnits):
    def __init__(self, value, conv=269.2, v='Fen'):
        super().__init__(value, conv, v)


class Chi(LengthUnits):
    def __init__(self, value, conv=2.692, v='Chi'):
        super().__init__(value, conv, v)


class In(LengthUnits):
    def __init__(self, value, conv=0.03125, v='in'):
        super().__init__(value, conv, v)