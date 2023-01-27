'''
Задание 2.
Функции, методы, тайпинги.
'''


# Реализовать функцию, которая принимает строку и возвращает ее в обратном порядке.
def str_return(a: str) -> str:
    return a[::-1]


print(str_return('привет я строка'))


# Реализовать функцию, которая принимает два параметра: число и степень - и возвращает это число,
# возведенное в степень.
# В случае, если степень не задана пользователем, используется значение 2.0.
def step(a: float, n=2.0) -> float:
    return a ** n


print(step(2.5, 4.0))


# Реализовать функцию, которая принимает произвольный набор параметров и возвращает кортеж, содержащий
# типы переданных параметров.
def params(*args) -> tuple:
    return tuple(map(type, args))


print(params(2.5, 4, (2, 5, 1), {1: 2}, 'stroka', [1, 24, 3], True))


# Реализовать функцию, которая принимает произвольный набор именованных параметров и возвращает их
# группировку по типу в виде словаря.
# Например, если входные параметры заданы как `a=34, b='some text', c=2, d=1.3, e={1: 2}, f=-3.0`,
# то необходимо вернуть словарь следующего вида:
# {
#   int: [['a', 34], ['c', 2]]int: [['a', 34], ['c', 2]],
#   str: [['b', 'some text']],
#   float: [['d', 1.3], ['f', -3.0]],
#   dict: [['e', {1: 2}]]
# }

def slowar(**kwargs) -> dict:
    slow = {}
    for key, value in kwargs.items():
        slow.setdefault(type(value), []).append([key, value])
    return slow


print(slowar(a=1, b=2.4, c=3, d=4.5, e=5.8, f='sa', g='stroka', h={1: 2}, i={3: 4}, j=(1, 4), k={5, 8}))


# Реализовать функцию, которая принимает строку и произвольный набор неименованных и именованных параметров.
# Строка может содержать произвольный набор подстрок вида **, *index* или *name*.
# Вместо ** в строку должен быть подставлен символ *.
# Вместо *index* должен быть подставлен неименованный параметр с индексом index. Должна поддерживаться
# отрицательная индексация.
# Вместо *name* должен быть подставлен именованный параметр с именем name.

def stroka(string: str, *args, **kwargs) -> str:
    st_separate = string.split('*')
    for i in range(len(st_separate)):
        if i % 2:
            if not st_separate[i]:
                st_separate[i] = '*'
            elif st_separate[i] in kwargs:
                st_separate[i] = str(kwargs[st_separate[i]])
            else:
                st_separate[i] = str(args[int(st_separate[i])])

    strk = ''.join(st_separate)
    return strk


print(stroka('** slovo *rat*, **, *asu* *0* *1* *2*', 2, 'sd', 4.5, rat='dog', asu='Vaas'))
