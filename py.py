# nums=[1,2,3,4,5]
#
# even=0
#
# for i in range(len(nums)):
#     if nums[i]%2==0:
#         even+=1
#
# print(even)
# l=[1,2,3,4,2,33,44,55,88]
# big=None
# for i in range(len(l)):
#     if l[i]%2==0:
#         if big is None or l[i]>big:
#             big=l[i]
#
# print(big)
# l=[1,2,2,3,5,6,7]
# even=0
# for num in l:
#     if num%2==0:
#         even+=1
# print(even)
#prime numbers in range
import string

# x=[1,2,12,4,5,6,7,3]
#
# even_ind=list(filter(lambda i: x.index(i)%2==0,x))
# print(even_ind)
#
# x=[11,1,2,3,4]
# y=list(map(lambda i:i*i,x))
# print(y)

# x=[1,2,3,4,5]
# sq=list(map(lambda i:i**2,x))
# print(sq)
# x=[1,2,3,4,5,6]
# ten=list(map(lambda i: i+10 ,x))
# print(ten)
#
# l=[10,20,30]
# st=list(map(str,l))
# print(st)

# l=["abbbbb","bqs","c","d","e"]
#
# le=list(map(lambda i: len(i),l))
# print(le)
#
# l=[10,20,30]
# map=list(map(str,l))
# print(map)

# l1=[34,87,56,3,90,6]
# if element is even then map that with square
# of that number else keep as t is

# ma=list(map(lambda x: x**2  if x%2==0 else x,l1))
# print(ma)
# even index even elements
# x=list(map(lambda i: l1.index(i),l1))
# print(x)
# l=[1,2,3,4,5]
# for i in enumerate(l):
#     print(i)
#map and filter comb usinf even index even elein a list
# l=[11,2,3,4,6,7]
# eve=list(filter( lambda i: l[i]))
# l=[0,2,2,4,5]
# eve=list(map(lambda x:l[x],filter(lambda i: i%2==0and l[i]%2==0,range(len(l)))))
# print(eve)
#
# l=[11,22,22,33,22,2]
# even=list(map(lambda x:l[x],filter(lambda i: i%2==0 and l[i]%2==0,range(len(l)))))
# print(even)

# odd index even elements
# l=[1,2,3,4,5]
# eve=list(map(lambda x:l[x],filter(lambda i: i%2!=0 and l[i]%2==0,range(len(l)))))
# print(eve)
# l=[10,11,12,13,14,15,16,17,18,19]
# even=list(filter(lambda i:l[i]%2==0,range(len(l))))
# print(even)
# l=[10,111,201,250,300,150,167]




































