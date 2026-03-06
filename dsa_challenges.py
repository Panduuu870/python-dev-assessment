def find_second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()

    if len(unique_numbers) < 2:
        return None

    return unique_numbers[-2]


nums = [10, 20, 4, 45, 99, 99]
result = find_second_largest(nums)

print("Second largest number:", result)