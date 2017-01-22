def sum_series(n,first,second):
    results=[]
    if n>0:
        results.append(first)
    if n>1:
        results.append(second)
        for count in range(n-2):
            results.append(first+second)
            first,second=second,first+second
    print(results)

def fibonacci(n):
    sum_series(n,0,1)

def lucas(n):
    sum_series(n,2,1)

fibonacci(10)
lucas(10)