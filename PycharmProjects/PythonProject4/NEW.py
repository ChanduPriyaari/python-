# n=[10,20,30,40]
# s=[]
#
# for i in range(0,len(n)):
#     score=int(input())
#     s.append(score)
# print(s)
#
#
# n=[10,20,30,40]
#
# n.insert(1,4)
# print(n)
# n[1:1]=[11]
# print(n)
#
# name=input()
# course=input()
# student_rec=(name,course)
# student_name,student_course=student_rec
# print(student_rec)
#
# word=input()
#
# f=int(input())
# s=int(input())
# t=int(input())
# nums=[f,s,t]
# re=(f,s,t)
#
# print(word[1:-1])
# print(nums[:2])
# print(re[::-1])
#
# t=["hi","helloe"]
# print(t.split()
# )
#
# print("--".join(t))
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.strip())
# print(text.lstrip())
# print(text.replace("python","java"))
# print(text.find("pro"))
# print(text.count('m'))
# print(text.split(","))
# print(text.startswith(""))
#
# print(t.split())
# print("-".join(t))
# words=["learn", "python", "dailu "]
# s="--".join(words)
# print(s)
#
# words="chandu aari"
# print("--".join(words))
# t=["hi","eug"]
# print(".".join(t))
#
# lst1=[10,20,30,40,50]
# print(lst1)#10
# print(id(lst1))#id address
#
# lst2=lst1
# print(lst2)#10...
# print(id(lst2))#address)
# lst2=[10,20,50]
# lst2.remove(50)#removes 50
# print(lst2)#10,20,30,40
# print(lst1) #10,20,30,40,50
# lst1.remove(10)
# print(lst1)
# print(lst2)
# l=[1,2,3,4,5]
#
# print(l)
# print(id(l))
#
# l1=l
# print(l1)
# print(id(l1))
#
# l1=[1,2,3,4,5,6,7]
# print(l1)
# print(id(l1))
# l1.remove(2)
# print(l1.pop(0))
# print(l1.pop())
# print(l1)
# a=input()
# b=input()
# c=(a,b)
# updated=input()
# c=(a[0],updated,b[1])
# print(c)
# t1=(1,2,3)
# t2=(3,4,5)
# total=(t1,t2)
# total=(t1[0],t2[0])
# print(total)
# def greet():
#     print("good morning")
# greet()
# def greet():
#     return 20
# a=greet()
# print(a)
# def demo():
from os import name


# name="chandu"
#
# def demo():
#     name="chandu aari"
#     print(name)
# demo()
# print(name)
#
# def ad(skill,skills=[]):
#     skills.append(skill)
#     return skills
# print(ad("java"))
# print(ad("bava"))
# def m(skill,skills=None):
#     if skills is None:
#         skills=[]
#         skills.append(skill)
#         return skills
# print(m('python'))
# print(m("java"))

# def cl(mom,dad=[]):
#     dad.append(mom)
#     return dad
# print(cl("chandu"))
# print(cl("dilliee"))
#
# def home(mom,dad=None):
#     if dad is None:
#         dad=[]
#         dad.append(mom)
#
#         return mom
# print(home("chandu"))
# print(home("dilli"))
# print(home("abba"))

# ##functions
# def tml(balaji,amma=None):
#     if amma is None:
#         amma=[]
#         amma.append(balaji)
#     return amma
# print(tml("bhakt"))
# print(tml("prace"))
#
# lst1=[1,1,3,5,8,9]
# print(lst1)
# print(id(lst1))
# lst2=lst1
# print(lst2)
# print(id(lst2))
# print(lst1==lst2)
# print(lst1 is lst2)

# std={'name':"chandu",'course':"python",'marks':90}
# print(std['name'])
# std['name']="priya"
# print(std['name'])
# print(std.get('name'))
# print(std.get('course'))
# print(std.get("marks"))
# std['city']='blore'
# print(std['city'])
# if 'course' in std:
#     print("yeahh")
# print(std)
# print(std.keys())
# print(std.values())
# print(std.items())
# s={"hi","py","hi","sql"}
# print(s)
# print(type(s))
# s.add('git')
# print(s)
# s.remove('hi')
# print(s)
# s.discard('git')
# print(s)
# s.discard('java')
# print(s)
# if "py" in s:
#     print(s,"yes")
# s={[1,2]}
# print(s)
# s1={1,2,3,4,5,6}
# s2={4,5,6,7,8}
# s=s1|s2
# print(s)
# s=s1.union(s2)
# print(s)
# s=s1.intersection(s2)
# print(s)
# s=s1-s2
# print(s)
# s4=s2-s1
# print(s4)

# text="  python programmingh     "
# # print(t.split())
# #
# # print("--".join(t))
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.strip())
# print(text.lstrip())
# print(text.rstrip())
# print(text.replace("python","java"))
# print(text.find("pro"))
# print(text.count('m'))
# print(text.split(","))
# print(text.startswith(""))
# #
# print(t.split())
# print("-".join(t))
# words=["learn", "python", "dailu "]
# s="--".join(words)
# print(s)


# class A:
#     def __init__(self):
#         print("constructor")
# t=A()
#
# class Prod:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#
# p=Prod("jaggery",1200)
#
# print(p.name)
# print(p.price)
#
# p.price=1100
# print(p.price)
#
# class Car:
#     def __init__(self,name):
#         self.name=name
#
#
# c=Car("lamborghini")
# print(c.name)
# c.name="tata"
# print(c.name)

# class Home:
#     def __init__(self,mom,dad):
#         self.mom=mom
#         self.dad=dad
#     def __str__(self):
#         return f"{self.mom}   {self.dad}"
# h=Home("anu","narsimhulu")
# print(h)
#
# class Std:
#     def __init__(self,std_id,name,course,score=0.0,skill=None,is_placed=False):
#         self.std_id=std_id
#         self.name=name
#         self.course=course
#         self.score=score
#         self.skill=[] if skill is None else list(skill)
#         self.is_placed=is_placed
#
#     def __str__(self):
#         skill_text=(",".join(self.skill) if self.skill else "nooo")
#         place=("placed" if self.is_placed else "nott")
#
#         return (f"{self.std_id}\n"
#                 f"{self.name}\n"
#                 f"{self.course}\n"
#                 f"{self.score}\n"
#                 f"{place}")
# s=Std(1,"chand","py",85.5,["python,sql,git"],True)
# print(s)




#
# l=[11,2,3,5,4,24]
# even=0
# for i in range(len(l)):
#     if l[i]%2==0:
#         even=even+1
#
# print(even)

# l=[2,3,45,5,22,11,44]
#
# big=l[0]
#
# for i in range(len(l)):
#     if i%2==0:
#         if l[i]%big==0:
#             big=l[i]
# print(big)





