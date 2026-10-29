def my_decorator(func):
    def wrapper():
        print("hi gm")
        func()
        print("good eve")
    return wrapper

@my_decorator
def teach():
    print("hi")
# teach=my_decorator(teach)
teach()

def place_visit(place):

    def wrapper():
        print("thinking..")
        place()
        print("tirumala")

    return wrapper

@place_visit
def going():
    print("visiting")
going=place_visit(going)
going()
#creating a dec using the argments

def announce(function):
    def wrapper(name):
        print("hello greeting")
        return function(name)
    return wrapper

@announce
def my_name(name):
    return name
my_name("chandu")


without args
def my_func(func):
    def wrapper():
        print("hello chandu")
        func()

    return wrapper
@my_func
def teach():
    print("is itgood")
teach()

import time

from threading import Thread

def marks():
    print("downloading data")
    time.sleep(2)
    print("helloq")

def course():
    print("drawingg")
    time.sleep(2)
    print("chandu")

t1=Thread(target=marks)
t2=Thread(target=course)
t1.start()
t1.join()
t2.start()
t2.join()

iterators

l=[1,2,3,4,5]

t=iter(l)
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t))
print(next(t,"stopped"))
generator

def gen_func():
    yield 10
g=gen_func()
print(next(g))








