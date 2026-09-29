import copy

a=[[1,2],[3,4]]
b=copy.deepcopy(a)
b[0][0]=100
print(a)
print(b)


n=int(input())
total=0
# counter=0
while 0<n:
    digit=n%10
    total=total+digit
    n=n//10
    # total=total+counter
    # counter+=1
print(total)


#prod

n=int(input())
total=1 #4
while n>0:  #234>0  23>0   2>0 T
    digit=n%10  #234%10   4  23%10 =3   2%10=2
    total=total*digit #1*4 =4   4*3=12   12*2=24
    n=n//10 #234//10 23 //10=2    2//10 0
print(total)
#reverse

n=int(input())

total=0 #3
while n>0: #12    1
    digit=n%10 #123%10=3  12%10=2   2%10=2
    total=total*10+digit #0*10+3   30+2=32   32*10
    n=n//10  # 123//10 = 12 //10=1
print(total)


n=int(input())

rev=0
m=n
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print(rev)
if m==rev:
    print("palindrome")
else:
    print("not palindrome")

n=int(input())
count=0
while n>0:
    n=n//10
    count=count+1

print(count)

n=[1,2,3,4,5,6,7]

for num in n:
    count=0
    for i in range(1,len(n)):
        if num%i==0:
            count+=1

    if count==2:
        print(num,"primee")

    else:
        print(num,"not a primt")
n=17
is_prime=True

if n<=2:
    is_prime=False

for i in range(2,n+1):
    if n%i==0:
        is_prime=False
        break

if is_prime:
    print("hhhaa")
else:
    print("NN")