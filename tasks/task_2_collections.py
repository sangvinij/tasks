'''
Задание 2.
Коллекции.
Примечание: входные параметры ни в однй из задач не должны быть модифицированы.
'''

from typing import Any, Dict, Iterable, List, Tuple
from itertools import zip_longest


# Сконструировать и вернуть список из переданных аргументов.
def build_list_from_args(*args) -> List:
    return list(args)


print(build_list_from_args(2, 4, 5, 6))


# Сконструировать и вернуть список из переданных аргументов, имеющих тип int.
def build_int_list_from_args(*args) -> List[int]:
    return [arg for arg in args if isinstance(arg, int)]


print(build_int_list_from_args(2, 4, 5, 2.2, 'sao', '21', 3.5))


# Сконструировать и вернуть список из переданных аргументов, имеющих заданный тип.
def build_list_from_args_using_type(argument_type: type, *args) -> List:
    return [arg for arg in args if isinstance(arg, argument_type)]


print(build_list_from_args_using_type(str, 2, 4, 5, 2.2, 'sao', '21', 3.5))


# Сконструировать и вернуть список из переданных аргументов, тип которых входит заданное множество.
# Для более эффективной работы преобразовать `argument_types` в `set`.
def build_list_from_args_using_type_set(argument_types: Iterable, *args) -> List:
    return [arg for arg in args if type(arg) in set(argument_types)]


print(build_list_from_args_using_type_set([int, float], 2, 3, 4.5, '21', 'str'))


# Сконструировать и вернуть список из двух списков, переданных в качестве аргументов.
def build_list_from_two_lists(first: List, second: List) -> List:
    return first + second


print(build_list_from_two_lists([2, 4, 5], [6, 7, 8]))


# Сконструировать и вернуть список из неограниченного числа списков, переданных в качестве аргументов.
def build_list_from_list_args(*lists) -> List:
    spis = []
    for i in lists:
        spis.extend(i)

    return spis


print(build_list_from_list_args([2, 4, 5], [5, 5, 6], [6, 7, 8]))


# Сконструировать список из заданного элемента и значения длины (использовать умножение).
def build_list_from_value_and_length(value: Any, length: int) -> List:
    return [value] * length


print(build_list_from_value_and_length(5, 7))


# Удалить из списка заданный элемент.
def remove_value_from_list(values: List, value_to_remove: Any) -> List:
    while value_to_remove in values:
        values.remove(value_to_remove)

    return values


print(remove_value_from_list([2, 4, 4, 5, 124], 4))


# Удалить из списка заданный элемент, используя comprehension expression [... for .. in ...].
def remove_value_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value != value_to_remove]


print(remove_value_from_list_using_comprehension([2, 4, 4, 5, 124], 4))


# Удалить из списка заданный элемент, используя `filter` и lambda-функцию.
def remove_value_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x != value_to_remove, values))


print(remove_value_from_list_using_filter([2, 4, 4, 5, 124], 4))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list(values: List, values_to_remove: Iterable) -> List:
    return [value for value in values if value not in set(values_to_remove)]


print(remove_values_from_list([2, 4, 5, 4, 4, 124], [4, 2]))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
def remove_values_from_list_using_comprehension(values: List, value_to_remove: Any) -> List:
    return [value for value in values if value not in set(value_to_remove)]


print(remove_values_from_list([2, 4, 5, 4, 4, 124], [4, 2]))


# Удалить из списка заданные элементы. Преобразовать `values_to_remove` в `set`.
# Использовать `filter` и lambda-функцию.
def remove_values_from_list_using_filter(values: List, value_to_remove: Any) -> List:
    return list(filter(lambda x: x not in set(value_to_remove), values))


print(remove_values_from_list([2, 4, 5, 4, 4, 124], [4, 2]))


# Удалить из списка дублирующиеся значения (использовать преобразование в `set` и обратно).
def remove_duplicates_from_list(values: List) -> List:
    return list(set(values))


print(remove_duplicates_from_list([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]))


# Создать и вернуть словарь из заданного набора именованных аргументов, значения которых имеют тип int.
def build_dict_from_named_arguments_of_type_int(**kwargs) -> Dict:
    return {k: v for k, v in kwargs.items() if isinstance(v, int)}


print(build_dict_from_named_arguments_of_type_int(a=1, b=2, c=3, d='4', e='5', f=6.5, g=[2, 1]))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


print(build_dict_from_keys([1, 2, 3, 4, 5]))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - None (dict.fromkeys).
def build_dict_from_keys(values: Iterable) -> Dict:
    return dict.fromkeys(values)


print(build_dict_from_keys([1, 2, 3, 4, 5]))


# Создать и вернуть словарь, используя в качестве ключей аргумент функции,
# а в качестве значений - значение по-умолчанию.
def build_dict_from_keys_and_default(values: Iterable, default: Any) -> Dict:
    return dict.fromkeys(values, default)


print(build_dict_from_keys_and_default([1, 2, 3, 4, 5], 6))


# Создать и вернуть словарь, ключами которого являются индексы элементов,
# а значениями - значения элементов iterable параметров (использовать enumerate и dict comprehension).
def build_dict_from_indexed_values(values: Iterable) -> Dict:
    return {key: value for key, value in enumerate(values)}


print(build_dict_from_indexed_values(['a', 'b', 'c', 'd', 'e', 'f']))


# Создать и вернуть словарь, собранный на основе списка пар ключ-значение.
def build_dict_from_key_value_pairs(kws: List[Tuple]) -> Dict:
    return dict(kws)


print(build_dict_from_key_value_pairs([(1, 2), (3, 4), (5, 6)]))


# Создать и вернуть словарь, собранный из двух списков, один из которых
# содержит ключ, а второй - соответствующее значение (использовать zip).
def build_dict_from_two_lists(keys: List, values: List) -> Dict:
    return dict(zip(keys, values))


print(build_dict_from_two_lists([1, 2, 3], [4, 5, 6]))


# Сформировать из двух словарей и вернуть его. В случае, если ключи совпадают,
# использовать значение из второго словаря (dict.update).
def build_dict_using_update(first: Dict, second: Dict) -> Dict:
    slow = first.copy()
    slow.update(second)
    return slow


print(build_dict_using_update({1: 2, 2: 3, 3: 4, 4: 5, 6: 7}, {5: 6, 7: 8, 1: 3}))


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Заменить значение в случае совпадения ключей.
def update_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    slow = dictionary.copy()
    slow.update(kwargs)
    return slow


print(update_dict_using_kwargs({'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 7}, a='21', b=6, f=19))


# Обновить словарь (и вернуть его), используя значения именованных аргументов.
# Объединить значения в список в случае совпадения ключей.
def update_and_merge_dict_using_kwargs(dictionary: Dict, **kwargs) -> Dict:
    slow = dictionary.copy()
    for k in kwargs:
        if k in slow:
            slow[k] = [slow[k]]
            slow[k].append(kwargs[k])
        else:
            slow[k] = kwargs[k]

    return slow


print(update_and_merge_dict_using_kwargs({'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 7}, a='21', b=6, f=19))


# Объединить два словаря и вернуть результат.
# Объединить значения в список в случае совпадения ключей.
def merge_two_dicts(first: Dict, second: Dict) -> Dict:
    slow = first.copy()
    for k in second:
        if k in slow:
            slow[k] = [slow[k]]
            slow[k].append(second[k])
        else:
            slow[k] = second[k]

    return slow


print(merge_two_dicts({1: 2, 2: 3, 3: 4, 4: 5, 5: 6}, {4: 7, 5: 8, 6: 9, 7: 10}))


# Объединить два словаря и вернуть результат.
# В случае совпадения ключей:
# - объединить значения рекурсивно, если оба значения - словари;
# - объединить значения в один список, если оба значения - списки;
# - объединить значения в одно множество, если оба значения - множества;
# - объединить значения в список в любом другом случае.
def deep_merge_two_dicts(first: Dict, second: Dict) -> Dict:
    slow = first.copy()
    for k in second:
        if k in slow:
            if isinstance(slow[k], dict) and isinstance(second[k], dict):
                slow[k].update(second[k])
            elif isinstance(slow[k], list) and isinstance(second[k], list):
                slow[k].extend(second[k])
            elif isinstance(slow[k], set) and isinstance(second[k], set):
                slow[k].union(second[k])
            else:
                slow[k] = [slow[k]]
                slow[k].append(second[k])
        else:
            slow[k] = second[k]
    return slow


print(deep_merge_two_dicts({'a': {1: 2}, 'b': [3, 4], 'c': {5, 6}, 'd': 7, 'e': 8},
                           {'a': {3: 4}, 'b': [5, 6], 'c': {7, 8}, 'd': 8, 'f': 'stroka'}))


# Вернуть список, состоящий из ключей, принадлежащих словарю.
def get_keys(dictionary: Dict) -> List:
    return list(dictionary.keys())


print(get_keys({1: 2, 2: 3, 3: 4, 4: 5, 5: 6}))


# Вернуть список, состоящий из значений, принадлежащих словарю.
def get_values(dictionary: Dict) -> List:
    return list(dictionary.values())


print(get_values({1: 2, 2: 3, 3: 4, 4: 5, 5: 6}))


# Вернуть список, состоящий из пар ключ-значение, принадлежащих словарю.
def get_key_value_pairs(dictionary: Dict) -> List[Tuple]:
    return list(dictionary.items())


print(get_key_value_pairs({1: 2, 2: 3, 3: 4, 4: 5, 5: 6}))


# Реверсировать и вернуть словарь.
def reverse_dict(dictionary: Dict) -> Dict:
    return dict(reversed(dictionary.items()))


print(reverse_dict({1: 2, 2: 3, 3: 4, 4: 5, 5: 6}))


# Удалить из словаря элементы, имеющие пустые значения (None, '', [], {}).
def clear_dummy_elements(dictionary: Dict) -> Dict:
    return {k: v for k, v in dictionary.items() if v}


print(clear_dummy_elements({1: {}, 2: 3, 3: 4, 4: [], 5: None, 6: []}))


# Удалить из словаря дублирующиеся и пустые элементы.
def clear_dummy_and_duplicate_elements(dictionary: Dict) -> Dict:
    slow = {}
    for k, v in dictionary.items():
        if v and v not in slow.values():
            slow[k] = [k]

    return slow


print(clear_dummy_and_duplicate_elements({1: {}, 2: 3, 3: 3, 4: [], 5: None, 6: []}))


# Обменять в словаре ключи и значения (в качестве значений могут выступать только неизменяемые значения).
def swap_dict_keys_and_values(dictionary: Dict) -> Dict:
    return {v: k for k, v in dictionary.items()}


print(swap_dict_keys_and_values({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))


# Вернуть словарь, отсортированный по ключу. Ключи могут иметь только тип int.
def sort_dict_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items()))


print(sort_dict_with_int_keys({4: 1, 2: 3, 1: 2, 3: 4, 5: 5}))


# Вернуть словарь, отсортированный по ключу в обратном порядке. Ключи могут иметь только тип int.
def sort_dict_backward_with_int_keys(dictionary: Dict) -> Dict:
    return dict(sorted(dictionary.items(), reverse=True))


print(sort_dict_backward_with_int_keys({4: 1, 2: 3, 1: 2, 3: 4, 5: 5}))


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
def group_dict_elements_by_key_type(dictionary: Dict) -> Dict:
    i = []
    fl = []
    st = []
    for k, v in dictionary.items():
        if isinstance(k, int):
            i.append((k, v))
        elif isinstance(k, float):
            fl.append((k, v))
        else:
            st.append((k, v))

    return dict(sorted(i) + sorted(fl) + sorted(st))


print(group_dict_elements_by_key_type({2.4: 1, 'a': 4, 4: 5, 1.5: 8, 'str': 'abc', 6: 2}))


# Вернуть словарь, элементы которого сгруппированы по типу ключа.
# В качестве ключей могут выступать: целые числа, дробные числа и строки.
# Приоритет сортировки групп (от высшего к низшему): целые числа, дробные числа, строки.
# Внутри каждой из групп отсортировать элементы по значениям ключа в обратном порядке.
def group_dict_elements_by_key_type_and_sort(dictionary: Dict) -> Dict:
    i = []
    fl = []
    st = []
    for k, v in dictionary.items():
        if isinstance(k, int):
            i.append((k, v))
        elif isinstance(k, float):
            fl.append((k, v))
        else:
            st.append((k, v))

    return dict(sorted(i, reverse=True) + sorted(fl, reverse=True) + sorted(st, reverse=True))


print(group_dict_elements_by_key_type_and_sort({2.4: 1, 'a': 4, 4: 5, 1.5: 8, 'str': 'abc', 6: 2}))


# Подсчитать количество элементов словаря, имеющих числовой тип, значение которых находится
# в интервале [-10, 25].
def count_dict_elements(dictionary: Dict) -> Dict:
    count = 0
    for k, v in dictionary.items():
        if (isinstance(v, int) or isinstance(v, float)) and -10 <= v <= 25:
            count += 1

    return {'numbers: ': count}


print(count_dict_elements({1: 2, 2: 412, 3: -24, 5: 2.4, 6: 'str', 7: [1, 2, 4]}))


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_lists(keys: List, values: List) -> Dict:
    return dict(zip_longest(keys, values))


print(build_dict_from_two_unaligned_lists([1, 2, 3, 4, 5], [6, 7, 8]))


# Построить и возвратить словарь из двух списков. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение, заданное по-умолчанию.
def build_dict_from_two_unaligned_lists_and_default(keys: List, values: List, default: Any) -> Dict:
    return dict(zip_longest(keys, values, fillvalue=default))


print(build_dict_from_two_unaligned_lists_and_default([1, 2, 3, 4, 5], [6, 7, 8], 9))


# Построить и возвратить словарь из двух iterable объектов. Количество ключей может превышать
# количество значений. В этом случае (для ключей, оставшихся без соответствующей пары)
# в качестве значений использовать значение None.
def build_dict_from_two_unaligned_iterables(keys: Iterable, values: Iterable) -> Dict:
    return dict(zip_longest(keys, values))


print(build_dict_from_two_unaligned_iterables({1, 2, 3, 4}, (4, 5, 6)))
