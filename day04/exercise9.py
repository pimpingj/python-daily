def divisible_by_seven(num = 7):
    result =  [x for x in range(1,101) if x % num == 0]
    return result , len(result)

print(divisible_by_seven())
print(divisible_by_seven(13))