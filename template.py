n, B = list(map(int, input().strip().split()))
T = 0

# your code here  Brute-Force Search
n = int(input("n="))
B = int(input("B="))
num = list()
xey = list()
zm = 0
t = 1
for i in range(1,n+1):
    if i % 2 != 0:
        p = 3**i + 1
        num.append(p)
        i += 1
        a = 2**i + 1
        num.append(a)
        
for c in range(1,n+1):
    xey.append(c-1)
xey.sort(reverse = True)
while True:
    for i in range(0,n):
        zm += (num[i]**xey[i]) * t
    if (B > zm):
        zm = 0
        t += 1
    else:
        break
print(t) 

#your code here Bisection Search
n = int(input("n="))
B = int(input("B="))
num = list()
xey = list()
zm = 0
low = 0
high = 10000
t = ((low+high)/2)
for i in range(1,n+1):
    if i % 2 != 0:
        p = 3**i + 1
        num.append(p)
        i += 1
        a = 2**i + 1
        num.append(a)
        
for c in range(1,n+1):
    xey.append(c-1)
xey.sort(reverse = True)
k = 0
for i in range (0,n):
    k += (num[i]**xey[i])
zm = k*t
while B != zm:
    if (zm > B):
        high = t
        t = (((low+high)/2))
        zm = k*t
    elif (B > zm):
        low = t
        t = (((low+high)/2))
        zm = k*t
print(t)


# please do not modify the input and print statements
# and make sure that your code does not have any other print statements