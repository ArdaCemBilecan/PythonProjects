#memo for fibbonacci

def fib(n,memo={}):
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = fib(n-1,memo)+fib(n-2,memo)
        memo[n] = result
        return result
    
    
    
def fib1(n,memo={}):
    if n==0 or n==1:
        return 1
    if n in memo:
        return memo[n]
    else:
        result = fib(n-1,memo)+fib(n-2,memo)
        memo[n] = result
        return result
        
            

print(fib1(15,memo={}))