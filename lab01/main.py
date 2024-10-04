def prblem2():
    n = int(input())
    ans = 1
    for i in range(1,n+1):
        ans *= i
    print(ans)


def problem3():
    n = int(input())
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum+=i
    print(sum == n)

problem3()
    
