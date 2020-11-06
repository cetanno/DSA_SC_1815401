x,y,n= map(int,input().split())
for i in range(n):
    j = i + 1
    if (j % x == 0):
        if (j % y ==0):
            print("FizzBuzz")
        else:
            print("Fizz")
    elif(j% y == 0):
        print("Buzz")
    else:
        print(j)
