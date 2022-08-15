def factorial(num):
    result = 1
    if num > 0:
        result = num * factorial(num-1)
    return result
    
    
num = int(input())
print(factorial(num))