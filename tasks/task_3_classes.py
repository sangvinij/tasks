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
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('invalid value type')
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = other.value
        return self.__class__(self.value + sc)

    def __iadd__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = other.value

        self.value += sc
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = other.value
        return self.__class__(self.value - sc)

    def __isub__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = other.value

        self.value -= sc
        return self

    def __mul__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        return self.__class__(self.value * sc)

    def __imul__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other

        self.value *= sc
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = other.value
        return self.__class__(self.value / sc)

    def __itruediv__(self, other):
        if not isinstance(other, (int, float, LengthUnits)):
            raise ArithmeticError('invalid other type')

        sc = other
        if not isinstance(other, (int, float)):
            sc = other.value

        self.value /= sc
        return self


class Millimeters(LengthUnits):
    CONV = 1000
    UNIT = 'mm'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Centimeters(LengthUnits):
    CONV = 100
    UNIT = 'cm'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Meters(LengthUnits):
    CONV = 1
    UNIT = 'm'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Kilometers(LengthUnits):
    CONV = 0.001
    UNIT = 'km'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Inches(LengthUnits):
    CONV = 39.3701
    UNIT = 'inc'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Feets(LengthUnits):
    CONV = 3.28084
    UNIT = 'ft'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Yards(LengthUnits):
    CONV = 1.0936
    UNIT = 'yd'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Miles(LengthUnits):
    CONV = 0.000621371
    UNIT = 'mi'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Fen(LengthUnits):
    CONV = 269.2
    UNIT = 'fen'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class Chi(LengthUnits):
    CONV = 2.692
    UNIT = 'chi'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'


class In(LengthUnits):
    CONV = 0.03125
    UNIT = 'in'

    def __init__(self, value):
        super().__init__(value)

    def __str__(self):
        return f'{self.value * self.CONV} {self.UNIT}'
