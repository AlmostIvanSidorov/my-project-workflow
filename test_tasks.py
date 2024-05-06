def some(*args, **kwargs):
    print(locals())


# some(1,2,3, a=1, b=2, c=3)

a = {1:3, 2:2, 3:3}

# print(max(a,key=lambda x: a[x]))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    

print(factorial(9))

class Person():
    def __init__(self,name) -> None:
        self.name = name

    def say_hello(self):
        print(f"Hi! My name is {self.name}")

ivan = Person("Ivan")

ivan.say_hello()