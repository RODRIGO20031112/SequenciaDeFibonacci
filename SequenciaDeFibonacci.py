def fibonacci(n):
    a, b = 0, 1
    if n == 1:
        print(a)
    elif n <= 0:
        print("ERROR")
    else:
        print(a)
        print(b)
    for i in range(2, n):
        c = a + b
        a, b = b, c
        if c <= n:
            print(c)
num = int(input("Que número deseja encerrar a sequencia de fibonacci: "))
fibonacci(num)