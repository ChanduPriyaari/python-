# for i in range(1,11):
#     print(i,end="")
# print()
# for j in range(2,21):
#     print(j,end=" ")
#
# ## Read a character and determine whether it is a vowel or not:
#
# n=input()
#
#     if n in "aeiou":
#         print(n,"vowel")
#     else:
#         print("not a vowel")
# # Copy all elements from array1/list1 into array2/list2.
# l1=[1,2,3,4]
# l2=[]
# for i in range(len(l1)-1,-1,-1):
#     l2.append(l1[i])
# print(l2)
# #usimg-match case
# n=input()
# match n:
#     case "a"|"e"|"i"|"o"|"u":
#         print("vowel")
#     case _:
#         print("not")
# ##count even nos and odd nums
# n=[1,2,3,4,5,6,7,8]
# e=0
# o=0
# for i in range(len(n)):
#     if n[i]%2==0:
#         e+=1
#     else:
#         o+=1
# print(e)
# print(o)
# #big num in an array
# arr=[11,12,1,2,13,1,99,101]
# big=arr[0]
# for i in range(len(arr)):
#     if arr[i]>big:#12>11 1>12 99>13 99>101
#         big=arr[i]#12 #13 #99 #101
# print(big)
#
# # # find even big and odd big
# l=[98,2,4,6]
# even=None
# odd=None
# for i in range(len(l)):
#     if l[i]%2==0:
#         if even is None or l[i]>even:
#             even=l[i]
#     elif l[i]%2!=0:
#         if odd is None or l[i]>odd:
#             odd=l[i]
#
# print(even,"eve bigg")
# print(odd,"odd big")
#
# # copy even numbers into array2/list2.
# # copy odd numbers into array3/list3.
# # don't use copy() or other copying methods.
# c=[1,2,3,4,5,6]
# arr1=[]
# arr2=[]
# for i in range(len(c)):
#     if c[i]%2==0:
#         arr1.append(c[i])
#     else:
#         arr2.append(c[i])
#
# print(arr1)
# print(arr2)
# # qn..take arr1/list1, arr2/list2 with some random numbers.
# # take an empty arr3/list3 of relevant size.
# # copy first arr1/list1 into arr3/list3.
# # copy the next arr2/list2 elements into arr3/list3.
# l1=[11,23,123,13,43]
# l2=[1,2,3,4,6]
# l3=[]
# for i in range(len(l1)):
#     l3.append(l1[i])
#
#
# for i in range(len(l2)):
#     l3.append(l2[i])
# print(l3)
#
# # with some numbers.print even nos present in the even positions.
# l=[10,10,20,33,33,44,55,6]
# for i in range(len(l)):
#     if l[i]%2==0 and i%2==0:
#         print(l[i])
#
# # with some numbers.add both arrays / list into third array / list
# l=[1,2,3]
# l2=[3,4,5]
# l3=[]
# for i in range(len(l)):
#     l3.append(l[i]+l2[i])
#
# for i in range(len(l)):
#     l3.append(l2[i])
#
# print(l3)
# #bigxt
# l=[1,13,45]
# max_num=l[0]
# for i in range(len(l)):
#     if l[i]>max_num:
#         max_num=l[i]
# print(max_num)
# ##second
# l=[12,25,2,14]
# total=0#12 37 39 53
# counter=0#1 2 3 4
# for i in range(len(l)):#4
#     total+=l[i]#0 + 12+25+2+14
#     counter+=1#12 3 4
#     print(total)
# print(total/counter)
# sum of nums
# l=int(input())
# total=0
# counter=1
# while counter<=l:
#     total=total+counter
#     counter+=1
#
# print(total)
# # sum of list of nums
# l=[1,2,3,4]
# total=0
#
# for i in range(len(l)):
#     if l[i]%2==0:
#         total=total+l[i]
#         print()
# print(total)
#
# #BIGGEST EVE
# x=[1,3,1,12,122,1222,1,1,1]
# eve=None
# for i in range(len(x)):
#     if x[i]%2==0:
#         if eve is None or x[i]>eve:
#             eve=x[i]
# print(eve)
#
# l=[11,2,3,4,5,6,7,9,100]
# biggest=None
# sec_big=None
#
# for i in range(len(l)):
#     if biggest is None or l[i]>biggest:
#         sec_big=biggest
#         biggest=l[i]
#     elif sec_big is None or l[i]>sec_big:
#         sec_big=l[i]
# print(biggest)
# print(sec_big)

#using while loop print reverse of num
# n=int(input())
# c=0
# while c<=n:
#     print(n)#0<5 1<=5
#     n=n+1




# i=5
# while i>=1:
#     print(i)
#     i-=1
#
# n = 342
# s=0
# while n>0:
#     r = n%10
#     s = r+s
#     n = n//10
# print(s)












