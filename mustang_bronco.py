def mustang_or_bronco(num = int(input("Enter a number: "))):
    result = num
    if num % 3 == 0:
        result = "Mustang"
    elif num % 5 == 0:
        result = "Bronco"
    if (num % 3 == 0) and (num % 5 == 0):
        result = "MustangBronco"
    return result


print(mustang_or_bronco())