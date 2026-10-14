def second_largest(numbers):
    largest = numbers[0]
    for n in numbers:
        if n > largest:
            largest = n
    secondlargest = float('-inf')
    for n in numbers:
        if n < largest and n > secondlargest:
            secondlargest = n
    return  secondlargest
numbers = [10,5,20,8,15]
result = second_largest(numbers)
print(result)
