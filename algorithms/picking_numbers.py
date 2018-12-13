
def picking_numbers(numbers):
    """Picking Numbers solution. HackerRank.com"""
    result = 0
    numbers.sort()
    for i in range(len(numbers)):
        count = 1
        for j in range(i+1, len(numbers)):
            if numbers[j] - numbers[i] <= 1:
                count += 1
                result = max(result, count)
    return result


# Some tests
assert picking_numbers([4, 6, 5, 3, 3, 1]) == 3, 'Test 1 failed'
assert picking_numbers([1, 2, 2, 3, 1, 2]) == 5, 'Test 2 failed'

print('Done!')
