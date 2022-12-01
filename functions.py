# Встроенные функции
x = print(88)
y = set()
print(type(x))
print(type(y))
print(x)
print(y)

# встроенные методы

my_list = [1, 2, 3, 4, 4]
my_list.append(4)
print(my_list)


def print_greeting():
    # Doc string/Документация данной функции
    """
    Print 'Hello!' text
    :return: None
    """
    print("Hello!")


# вызываем функцию
print(print_greeting())
# получаем описание функции
help(print_greeting)


def print_greeting_with_name(name='Name'):
    """
   :param name

   :return: None
   """
    print('Hello ' + name + '!')


print(print_greeting_with_name('Bill'))
help(print_greeting_with_name)


def sum_of_two_numbers(a=0, b=0):
    """
    :param a: The first addend
    :param b: The second addend
    :return: Sum of 'a' and 'b'
    """
    return a + b


x = sum_of_two_numbers(45, 1)
print(x)
help(sum_of_two_numbers)


def is_hello_in_text(text):
    if 'hello' in text.lower():
        return True
    else:
        return False


print(is_hello_in_text('Say hello everyone'))


def hello_in_text(text):
    return 'hello' in text.lower()


print(hello_in_text('Hello everyone'))


def is_string_in_text(string, text):
    return string in text


print(is_string_in_text('he', 'The apple'))
print(is_string_in_text('one', 'Hello'))


def greeting_depends_on_gender(name, gender):
    if gender == 'male':
        print('Hello ' + name + '!')
        return gender
    elif gender == 'female':
        print('Hey ' + name + '!')
        return gender
    else:
        print('Hi ' + name + '!')
        return gender


returned_value_1 = greeting_depends_on_gender('Jack', 'male')
returned_value_2 = greeting_depends_on_gender('Jane', 'female')
returned_value_3 = greeting_depends_on_gender('Ja', 'ale')

print(returned_value_1, returned_value_2, returned_value_3)
