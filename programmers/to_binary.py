# 십진수를 이진수로
# 나머지를 연속해서 받아주면 된다.

def change_to_binary(number):
    binary = ''
    while number != 1:
        binary += str(number % 2)
        number //= 2
        
    binary += str(number)
    
    return binary[::-1]

print(change_to_binary(25))