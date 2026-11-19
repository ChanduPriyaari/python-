

even or odd
n=[1,2,3,4,5]
for i in range(len(n)):
    if n[i]%2==0:
        print(n[i])
swap of 2 nums
a=10
b=20
a=a+b
b=a-b
a=a-b
print(a)
print(b)
n=4
t=0
for i in range(1,n+1):
  t+=i
print(t)
count the no of digits
n=1234
c=0
while n>0:
    c+=1
    n//=10
print(c)
prime number innrange of two numbers
n=int(input())
m=int(input())

for num in range(n,m+1):
    is_prime=True

    if num<=1:
        is_prime=False
    else:
        for i in range(n,int(n**0.5)+1):
            if num%i==0:
                is_prime=False
                break
if is_prime:
        print(num)
n=int(input())
prime=True

if n<=1:
  prime=False

for i in range(2,int(n**0.5)+1):
  if n%i==0:
    prime=False

if prime:
  print("prime")

n=int(input())
m=int(input())


for num in range(n,m+1):
    prime=True
    if num<=1:
        prime=False
    else:
        for i in range(2,num//2+1):
            if num%i==0:
                prime=False
                break
        if prime:
            print(num)
perfect number
n=int(input())
t=0
for i in range(1,n):
    if n%i==0:
        t+=i
if n==t:
    print("perfect")
else:
    print("not")
strong num
n=int(input())
total=0
m=n
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        fact=fact*i

    total=total+fact
    n//=10
if m==total:
    print("Stromg")
else:
    print("not")
n=list(map(int,input().split()))
total=0
for i in range(len(n)):
    total=total+n[i]
print(total)

using while loop
n=5

while 0<n:
    print(n)

i=1
while i<=10:
    print(i)
    i+=1

i=10
while i>=1:
    print(i)
    i-=1

i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

for i in range(1,4):
    for j in range(1,4):
        print(i,end="")
    print()

for i in range(1,4):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,3):
    for j in range(1,4):
        print(j)
loops

for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=" ")

    print()

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
for i in range(1,5):
    for j in range(1,5):
        if i+j>4:
            print(j,end=" ")
        else:
            print("*",end=" ")

    print()

for i in range(1,4):
    for j in range(1,4):
        if i+j==4:
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()
for i in range(1,4):
    for j in range(1,5):
        if j==2:
            continue
        print(i+j,end=" ")
    print()
for i in range(1,5):
    if i==3:
        pass
    print(i)

for i in range(1,4):
    for j in range(1,5):
        if j==2:
            continue
        if i==3 and j==4:
            break
        print(i*j,end="")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        if i==1 or i==2 or i==3 or i==4:
            print("*",end=" ")

        print()
a=[1,2,3]
b=a
print(a is b)
print(a==b)
for i in range(1,4):
    for j in range(i):
        print(j,end=" ")
    print()
armsrtonf

n=int(input())
m=n
rev=0
x=len(str(n))
while n>0:

    digit=n%10
    rev=rev+digit**x
    n=n//10

if rev==m:
    print("arm")
else:
    print("not anarmstron")

su=list(map(int,input().split()))
t=0
m=su
while su>0:
    digit=su%10
    t=t*10+digit
    su//=10
if m==t:
    print("palindrome numbv")
else:
    print("not ")

shallow copy shared among instances
a=[[100,1],[1,2]]

b=a.copy().copy()
a[0][0]=10
print(a)
print(b)

deepcopy is independent in nature
import copy
a=[[10,20],[1,2]]
b=copy.deepcopy(a)
a[1][1]=30
print(a)
print(b)

import copy
a=[[1,2],[3,4]]
b=copy.copy(a)

a[0][0]=100
print(a)
print(b)
import copy
a=[[1,2],[3,4]]
b=copy.deepcopy(a)
a[0][0]=10
print(a)
print(b)

prime number
nums=[1,2,3,4,5,6,7]

for n in nums:
    if n>1:
        prime=True

    for i in range(2,n):
        if n%i==0:
            prime=False
            break

if prime:
#     print("prime")# prime in range between
n=list(map(int,input().split()))

for num in n:
    if num>1:
        prime=True

        for i in range(2,num):
            if num%i==0:
                prime=False
                break
        if prime:
            print(num)
prime in range

n=list(map(int,input().split()))

for num in n:
    if num>1:
        prime=True
        for i in range(2,num):
             if num%i==0:
                 prime=False
        if prime:
            print(num)


n=int(input())



if n>1:
    prime=True
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            prime=False
    if prime:
        print("prime")
fact=int(input())
f=1
for i in range(1,fact+1):
    f=f*i
print(f)
n=int(input())
a=0
b=1
for i in range(1,n):
    print(a)
    a=b
    b=a+b
n=int(input())
a=0
b=1
for i in range(n):
    print(a)
    a,b=b,a+b
Pattern sequence
1. Arrays
2. Strings
3. Hashing
4. Two Pointers
5. Sliding Window
6. Prefix Sum
7. Sorting and Binary Search
8. Stack and Queue
9. Linked Lists
10. Recursion and Backtracking
11. Trees and BST
12. Heap and Priority Queue
13. Greedy Algorithms
14. Graphs
15. Dynamic Programming

for i in range(1,101):

    print(i,end=" ")
    if i%10==0:
        print()

for i in range(1,101):
    print(i,end=" ")
    if i%10==0:
        print()
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

l=[1,2,3,4,5,6,7,8]
c=0


for i in range(len(l)):
    if l[i]%2==0:
        c+=1
print(c)
5. take an array / list of 10 random numbers.
copy even numbers into array2/list2.
copy odd numbers into array3/list3.
don't use copy() or other copying methods.

l=[1,2,3,4,5,6,7]
l1=[]
l2=[]
for i in range(len(l)):
    if l[i]%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])

print(l1)
print(l2)
l1=[1,2,3]
l2=[1,7,5]
l3=[]
for i in range(len(l1)):
    l3.append(l1[i]+l2[i])

print(l3)



list1 = [10,20,30]
list2 = [40,50]
list3 = list1 + list2
print

list1 = [10, 20, 30]
list2 = [40, 50, 60, 70]

result = []
i = 0

while i < len(list1) or i < len(list2):

    if i < len(list1):
        result.append(list1[i])

    if i < len(list2):
        result.append(list2[i])

    i += 1

print(result)



