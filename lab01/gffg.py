n = int(input("Valoare n: "))
s=0
for i in range(1,n):
    if (n%i==0):
        s=s+i
if (s==n):
    print("este numar pefect")
else:
    print("nu este numar perfect")
