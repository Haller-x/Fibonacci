n = int(input("Digite o numero Fibbonacci: "))
def fib(n):
    x = [0,1]
    prox = x[-1] + x[-2]
    x.append(prox)
    while x[-1]<n:
        prox = x[-1] + x[-2]
        x.append(prox)
    print(x)
print(fib(n))
