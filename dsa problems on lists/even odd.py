def even_odd(numbers):
    even_count = 0
    odd_count = 0
    for n in numbers:
        if n % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    print("even count:",even_count)
    print("odd count:",odd_count)
numbers = [1,2,3,4,5]
even_odd(numbers)
