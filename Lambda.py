# Function Map
def sum_of_two_numbers(x):
    return x + x


number_list = [1, 2, 3, 4, 5, 6, 7]

result = map(sum_of_two_numbers, number_list)
print(result)

for item in result:
    print(item)

for item in map(sum_of_two_numbers, number_list):
    print(item)
# привести к list
print(list(map(sum_of_two_numbers, number_list)))


def is_a_in_string(string):
    if 'a' in string:
        print('String has "a"')
        return True
    else:
        print('String has not "a"')
        return False


string_list = ['Color', 'Cat', 'Dog', 'Rainbow']
print(list(map(is_a_in_string, string_list)))


# Filter function
# работает только с функциями, которые возвращают boolean значения

def is_number_odd(number_0):
    return number_0 % 2 == 1


number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(filter(is_number_odd, number_list)))

for number in filter(is_number_odd, number_list):
    print(number)


def is_cat_in_string(string):
    if 'cat' in string:
        print('String has "cat"')
        return True
    else:
        print("String hasn't 'cat'")
        return False


string_list_1 = ['sdjsjfjkfcatklfjjr', 'jfkfehrfskdog', 'djfjeihf']
print(list(filter(is_cat_in_string, string_list_1)))

# Lambda expression
# используется для создания анонимных функций

number_list = [1, 2, 3, 4, 5, 6, 7]
print(list(map(lambda number_1: number_1 ** 3, number_list)))
# анонимные функции всегда возвращают какое-то значение

print(list(filter(lambda number_2: number_2 % 2 == 1, number_list)))

print(list(map(lambda string: string[::-1], string_list_1)))
# '[::-1] - вывод в обратном порядке
