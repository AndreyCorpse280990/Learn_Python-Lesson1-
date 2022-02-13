# -*- coding: utf-8 -*-
# Создайте список из чисел 3, 5, 7, 9 и 10.5
number = [3, 5, 7, 9, 10.5]
# Выведите содержимое списка на экран
print(number)
# Добавьте в конец списка строку "Python"
number.append('Python')
# Выведите длину списка на экран
print(len(number))

# Выведите на экран начальный элемент списка
print(number[0])
# Выведите на экран последний элемент списка
print(number[-1])
# Напечатайте элементы списка со второго по четвертый включительно
print(number[1:4])
# удалите из списка строку "Python"
del number[-1]

# Создайте словарь
dictionary = {"city": "Москва", "temperature": "20"}
# Выведите на экран значение ключа city
print(dictionary['city'])
# Уменьшите значение "temperature" на 5
dictionary['temperature'] = int(dictionary['temperature']) - 5

# Выведите на экран весь словарь
print(dictionary)

# Проверьте, есть ли в словаре ключ country
print(dictionary.get('country'))
# Выведите значение по-умолчанию "Россия" для ключа country
print(dictionary.get('country', 'Россия'))
# Добавьте в словарь элемент date со значением "27.05.2019"
dictionary['date'] = '27.05.2019'
# Выведите на экран длину словаря
print(len(dictionary))
