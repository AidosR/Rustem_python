numbers = list(map(int, input("Enter numbers separated by space: ").split()))

multiples_of_3 = [num for num in numbers if num % 3 == 0]

print("Numbers that are multiples of 3:", multiples_of_3)
