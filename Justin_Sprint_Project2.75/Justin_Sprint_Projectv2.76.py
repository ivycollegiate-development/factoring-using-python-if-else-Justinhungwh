List all of factors of a values
def list_factors(n):
    return [i for i in range (1, n+1) if n % i == 0]