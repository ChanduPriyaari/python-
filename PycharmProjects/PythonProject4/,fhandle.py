file handdling
file=open("data.txt","r")
data=file.read()
print(data)
f.close()
#count eve and odd nums
l=[11,12,13,14,15,16,17]
eve=0
odd=0
for i in range(len(l)):
    if l[i]%2==0:
        eve+=1
    elif l[i]%2!=0:
        odd+=1
print("evev:",eve)
print(odd)

#ele in rev
l=[11,2,3,4]
for i in range(len(l)-1,-1,-1):
    print(l[i])

## sum of odd elements in even index
l=[11,2,13,12,1,2,3,6,7,8]
odd_sum=0
for i in range(len(l)):
    if l[i]%2!=0 and i%2==0:
        odd_sum+=1
print(odd_sum)

##second smallest
l=[11,2,3,4,5,6,7,8]
smallest=l[0]

for i in range(len(l)):
    if l[i]<smallest:
        smallest=l[i]

print(smallest)
