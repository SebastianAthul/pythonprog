def rec_fib(n):
    if n<=1:
        return n
    else:
        return rec_fib(n-1)+rec_fib(n-2)
nterms=10
print("Fibanocci series:")
for i in range(nterms):
    print(rec_fib(i))
    