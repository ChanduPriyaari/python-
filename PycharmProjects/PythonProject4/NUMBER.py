#count of pos,neg,0s

n=[1,2,3,4,5,-1,0,0,8,9]
pos=0
neg=0
zero=0
for i in range(len(n)-1):
    if n[i]>0:

        pos+=1
    elif n[i]<0:

        neg+=1
    elif n[i]==0:

        zero+=1
    else:
        print("invalid")
print(pos)
print(neg)
print(zero)

n=[1,2,3,4,5]
for i in range(len(n)-1,-1,-1):
    print(n[i])

num=int(input())
word=input()
print("njumbere")
for i in range(0,num+1):
    print(i)
print("string")
for i in word:

    print(i)

#break
for i in range(1,11):
    if i==5:
        continue
    print(i)

word="python"
for ch in word:
    if ch=="h":
        continue
    print(ch)



limit=int(input())
target=int(input())

count=0
total=0
found=False

for i in range(1,limit+1):
    if i%3==0:
        count+=1
        total=total+i
    if i==target:
        found=True

print(count)
print(target)
if found:
    print("hii")

#sum of multiples of 3

s=0
for i in range(1,11):
    if i%3==0:
        print(i)
        s+=i
print(s)

#check whether target is present
target=9
found=False

for i in range(0,10):
    if i%3==0:
        if i==target:
            found=True
print(found,i)
##

