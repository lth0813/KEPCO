data = "4546793"
numbers = list(map(int, data))
print(numbers)
result = [ ]

for i, num in enumerate(numbers):
    result.append(str(num))
    print(result)
    if i < len(numbers)-1: #i = 0 1 2 3 4 5 6 , len(numbers) = 6
        is_odd = num % 2 == 1 #num = 4 5 4 6 7 9 3
        is_next_odd = numbers[i+1] % 2 == 1 #numbers[i+1] = 5 4 6 7 9 3 을 2로 나눠 나머지가 1
        if is_odd and is_next_odd:
            result.append("-")
        elif not is_odd and not is_next_odd:
            result.append("*")
print("".join(result))
