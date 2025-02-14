# 피보나치 수열
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)
        
        
print(fibonacci(10))