def my_shiny_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        print("Я - код, который отработает до вызова функции")
        function_to_decorate() # Сама функция
        print("А я - код, срабатывающий после")
    # Вернём эту функцию
    return the_wrapper_around_the_original_function

# Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
def stand_alone_function():
    print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?")

@my_shiny_new_decorator
def stand_alone_function_2():
    print("second function")

# stand_alone_function()
# Однако, чтобы изменить её поведение, мы можем декорировать её, то есть просто передать декоратору,
# который обернет исходную функцию в любой код, который нам потребуется, и вернёт новую,
# готовую к использованию функцию:
# stand_alone_function_decorated = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function_decorated()
if __name__ == "__main__":
    # stand_alone_function_2 = my_shiny_new_decorator(stand_alone_function_2)

    stand_alone_function_2()

    stand_alone_function_2()

# stand_alone_function = my_shiny_new_decorator(stand_alone_function)
# stand_alone_function()

# @my_shiny_new_decorator
# def another_stand_alone_function():
#     print("Оставь меня в покое")

# another_stand_alone_function()

# # -------------------------------------------------------------
# def bread(func):
#     def wrapper():
#         print()
#         func()
#         print("<\______/>")
#     return wrapper

# def ingredients(func):
#     def wrapper():
#         print("#помидоры#")
#         func()
#         print("~салат~")
#     return wrapper

# def sandwich(food="--ветчина--"):
#     print(food)

# sandwich()
# sandwich = bread(ingredients(sandwich))
# sandwich()


# @bread
# @ingredients
# def sandwich(food="--ветчина--"):
#     print(food)

# sandwich()

# def benchmark(func):
#     """
#     Декоратор, выводящий время, которое заняло
#     выполнение декорируемой функции.
#     """
#     import time
#     def wrapper(*args, **kwargs):
#         t = time.clock()
#         res = func(*args, **kwargs)
#         print(func.__name__, time.clock() - t)
#         return res
#     return wrapper

# def logging(func):
#     """
#     Декоратор, логирующий работу кода.
#     (хорошо, он просто выводит вызовы, но тут могло быть и логирование!)
#     """
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         print(func.__name__, args, kwargs)
#         return res
#     return wrapper

# def counter(func):
#     """
#     Декоратор, считающий и выводящий количество вызовов
#     декорируемой функции.
#     """
#     def wrapper(*args, **kwargs):
#         wrapper.count += 1
#         res = func(*args, **kwargs)
#         print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
#         return res
#     wrapper.count = 0
#     return wrapper

# @benchmark
# @logging
# @counter
# def reverse_string(string):
#     return ''.join(reversed(string))

# print(reverse_string("А роза упала на лапу Азора"))
# print(reverse_string("A man, a plan, a canoe, pasta, heros, rajahs, a coloratura,"
# "maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag,"
# "a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash,"
# "a jar, sore hats, a peon, a canal: Panama!"))