skills=["python","java"]
try:

    print(skills[int(input())])
except IndexError:
    print("index out of bound")
class Stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"{self.name} {self.age}"

s=Stud("chandu",21)
print(s)
    def m(self):
        print(self.name)
        print(self.age)
        # return self.name,self.age
name1=input().strip()
age2=int(input())
s=Stud(name1,age2)
s.m()

class S:
    def __init__(self,name):
        self.name=name
    def update_score(self,new_name):
        self.name=new_name
    def m(self):
        print(self.name)
s=S("hi")
s.m()
s.update_score("chandu")
s.m()
class A:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def updated_score(self,new):
        self.score=new
    def m(self):
        print(self.name)
        print(self.score)
s=A("hello",90)
s.m()
s.name="heloow"
s.m()
s.updated_score("chanduy")
s.m()

class A:
    def __init__(self,n,m):
        self.n=n
        self.m=m
    def __str__(self):
        return f"{self.n}\n{self.m}"

s=A("dd","cc")
print(s)

class Bank:
    def __init__(self,balance):
        self.balance=balance
    def deposit(self,amt):
        if amt>0:
            self.balance+=amt
    def withdraw(self,amt):
        if amt>0 and amt<=self.balance:
    def get_bal(self):
        return self.balance
b=Bank(1000)
print(b.get_balance)

b.balance=-10
print(b.balance)
Name mangling

class Student:
    def __init__(self):
        self.__cl="chandu"
    def m(self):
        print(self.__cl)
s=Student()
s.m()
print(s._Student__cl)
GETTERS AND SETTERS

class Student:
    def set_mtd(self,name):
        self.name=name
    def geto(self):
        return self.name

s=Student()
name=input("enter name:")
s.set_mtd(name)
print(s.geto())
class Student:
    def set_mtd(self,name):
        self.name=name
    def get_mtd(self):
        return self.name

s=Student()
name=input("enter your name:")
s.set_mtd(name)
print(s.get_mtd())

class S:
    def __init__(self,score):
        self.__score=score

    @property
    def score(self):
        return self.__score
print(S.score)

class Normal:
    def __init__(self,name):
        self.__name=name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,cname):

        self.__name=cname
s=Normal("chand")
print(s.name)

class Stu:
    def __init__(self,age):
        self.__age=age
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,value):
        if age>0 and age<18:
            self.__age=value
        print("not valif")

s=Stu(21)
print(s.age)
class AmtError(Exception):
    pass
bal=int(input())
amt=int(input())
try:
    if amt>bal:

        raise AmtError("insufficient balance")
    print("value allow")
except AmtError as e:
    print(e)

l=[1,2,8,4,5]
for i in range(len(l)):
    if l[i]%2==0:
        print(l[i])

class  Teacher:

    def m1(x,y):
        print("The sum",x+y)
class Student(Teacher):
    def m1(a,b):
        print(a+b)
s=Student()
Student.m1(10,2)
Student.m1(2,2)
class A:
    def __init__(self,name):
        self.name=name
    def __str__(self):
        return self.name

a=A("chandu")
print(a)

class Vehicle:
    def __init__(self,brand,rent_per_day):
        self.brand=brand
        self.rent_per_day=rent_per_day

class Car(Vehicle):
    def m(self):
        print(self.brand)
        print(self.rent_per_day)

class Bike(Vehicle):
class A:
    clg="chand"
    @classmethod
    def change_name(cls,new):
        cls.clg=new

A.change_name("xyz college")
print(A.clg)

class Loc:
    place="ctr"
    @classmethod
    def change_loc(cls,new_loc):
        cls.place=new_loc
Loc.change_loc("tirumala")
print(Loc.place

class Dog:
    def sound(self):
        print("bow")
class Cow:
    def sound(self):
        print("moo moo")

def animal_sound(animal):
    animal.sound()

c=Cow()
d=Dog()
c.sound()
d.sound()

l=[1,2,3,4]
def sum_fun(l):

    s=0
    for i in l:
        s+=i
    return s

nums=list(sum_fun(l)
print(nums)

def upper_name(name):
    return name.upper()

names = ["vinay","bob","charlie"]

result = list(map(upper_name, names))
print(result)



def greater(num):
    return num > 0
numbers = [-5,-10,2,7,-0,3]

result = list(filter(greater, numbers))
print(result)



from functools import reduce
def largest(a, b):
    if a > b:
        return a
    else:
        return b
numbers = [12,65,7,89,34]

result = reduce(largest, numbers)
print(result)




















