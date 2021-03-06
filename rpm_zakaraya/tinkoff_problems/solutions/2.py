min = int(input())
max = int(input())
count = 0

def tests(min, max, count):
    for i in range(min, max+1):
        for j in range(len(str(i))):
            if str(i)[0] != str(i)[j]:
                break
            elif j == len(str(i)) - 1:
                count += 1
    return count


print(tests(min, max, count))