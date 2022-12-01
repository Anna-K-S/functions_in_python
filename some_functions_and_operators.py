from random import shuffle  # "shuffle" - перемешивать
from random import randint  # случайное целое число

for x in range(3, 11, 2):  # диапазон от "х,у,(шаг, с которым будет генерироваться последовательность) z)

    print(x)

print(range(5))  # "range(0, 5)" объект типа "range"
print(list(range(5)))  # получаем список "[0, 1, 2, 3, 4]"

letter_index = 0
my_string = 'fqwertyui'
for letter in my_string:
    print(letter + " is at index" + str(letter_index))
    letter_index += 1

my_string_2 = 'ghjepdk'
for item in enumerate(my_string_2):
    # функция 'enumerate' возвращает объекты типа 'tuple'
    # автоматически считает итерации цикла
    print(item)

my_string_2 = 'ghjepdk'
for index, lettter in enumerate(my_string_2):
    # распаковка объекта типа 'tuple'
    print(lettter + " is at index " + str(index))

# КС 'in" проверяет находится ли значение в последовательности/объекте
# результат "True/False"
print('a' in 'Jack')

letter_list = ['a', 'd', 'v', 'g']
print(7 in letter_list)
print('s' in letter_list)

dict_1 = {1: 'a', 2: 'b', 3: 'c'}
print(1 in dict_1)
print(1 in dict_1.keys())
print(1 in dict_1.values())

# Operation 'not in'
# возвращает 'True', если посл-ть с указанным значением отсутствует в объекте
fruits_list = ['apple', 'banana', 'orange']
print('grape' not in fruits_list)

integer_list = [1, 4, 6, 78]
print(34 not in integer_list)

print(list(range(7)) not in integer_list)

# Logical operators

# Operator 'and'
# возвращает 'True", если оба значения правдивы

x = 6
print(x > 3 and x < 10)  # (3 < x < 10) # True

colors_list = ['red', 'black', 'white']
print('red' in colors_list and 'pink' in colors_list)  # False

# Operator 'or'
# возвращает "True", если одно из значений правдиво
print(x < 15 or x < 1) # True
print('s' in colors_list or 4 in colors_list) # False

# Operator 'not'
# обратный результат. вернет 'False", если значение верное

print(not(2 < x > 4))  # False

# Functions 'min', 'max'
print(min(1, 4, 6, 7))  # минимальный объект в последовательности
print(max(23, 56, 78, 1.3))  # максимальны объект в последовательности
print(min('a', 't', "l"))

for let in "Hello":
    print(ord(let))
# 'ord()' - аски код символа

# Shuffle

my_list = [1, 2, 56, 78]
shuffle(my_list)
# возвращает перемешанный список
print(my_list)

# Randint
print(randint(34, 56))
