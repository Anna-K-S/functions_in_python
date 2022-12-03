# *args - arguments
# **kwargs - Keyword Arguments

def ten_percent_of_pro(x, y):
    return (x * y) * 0.1


print(ten_percent_of_pro(10, 20))

# *args
def ten_percent_of_pro_with_args(*args):
    # можно помещать неограниченное количество агрументов
    # можно совершать любые действия
    # получаем объект типа tuple
    product = 1
    for number in args:
        product = product * number
    return product * 0.1


print(ten_percent_of_pro_with_args(3, 5, 6, 9, -67))


def percent_of_product_with_args(percent, *args, ):
    # сначала устанавливается позиционные параметр, затем *args
    prod = 1
    for num in args:
        prod = prod * num
    return (prod / 100) * percent


print(percent_of_product_with_args(10, 4, 5, 7, 8, 11, 5, 4, 66, -5))


def func_with_kwargs(**kwargs):
    print(kwargs)


func_with_kwargs(first=1, second=2, third=3)


# **kwargs
возвращает oбъeкт dictionary
ключ в kwargs всегда должен быть словом
def hello_with_kwargs(**kwargs):
    if 'name' in kwargs:
        print('Hello! nice to meet you, {}'.format(kwargs['name']))
    else:
        print('Hello, what is your name?')


hello_with_kwargs(gender='male', age=24, name='Mike')
hello_with_kwargs(gender='male', age=24)
def hello_with_greeting_and_kwargs(greeting, **kwargs):
    if 'name' in kwargs:
        print('{}! nice to meet you, {}'.format(greeting, kwargs['name']))
    else:
        print('{}, what is your name?', format(greeting))


hello_with_greeting_and_kwargs("HI", gender='male', age=24, name='Mike')


def func_with_args_and_kwargs(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))


func_with_args_and_kwargs('one', 'two', drink='coffee', food='pizza')


# 1
def is_cat_here(*args):
    if "cat" in args:
        return True
    else:
        return False


print(is_cat_here('gog', 'dog', 45, 67, 'cat'))


# 2
def is_item_here(item, *args):
    if item in args:
        return True
    else:
        return False


print(is_item_here(3, 55, 65, 'black', 'cat', -565))


# 3.1
def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is' + str(my_color) + ', but '
              + str(kwargs['color'] + ' is also pretty good!'))
    else:
        print('My favorite color is {}. What\'s yours?'.format(my_color))


your_favorite_color(' black', red=1, dog=2, cat=3, green=4, pig='green')

# 3.2
def your_favorite_color(my_color, **kwargs):
    if 'color' in kwargs:
        print('My favorite color is {}, but {} is also pretty good!'.format(my_color, kwargs['color']))
    else:
        print('My favorite color is {}. What n\'s yours?'.format(my_color))


your_favorite_color(' black', red=1, dog=2, cat=3, green=4, color='blue')
