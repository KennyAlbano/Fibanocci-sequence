#fib
a=1
b=1
c=a+b
while(a+b+c<100000/3):
    print(a)
    print(b)
    print(c)
    a=c+b
    b=a+c
    c=a+b
    
