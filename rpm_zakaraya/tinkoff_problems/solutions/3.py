n = int(input())
height = [int(input()) for i in range(n)]


def solution(height):
    wrong_coords = {'even': [], 'odd': []}
    for i in range(n):
        if (height[i] % 2 == 0):
            if (i+1) % 2 != 0:
                wrong_coords['even'].append(i)
        else:
            if (i+1) % 2 == 0:
                wrong_coords['odd'].append(i)
    if wrong_coords['even'] == [] or wrong_coords['odd'] == [] or len(wrong_coords['even']) + len(wrong_coords['odd']) != 2:
        return [-1, -1] 
    else:
        height[wrong_coords['even'][0]], height[wrong_coords['odd'][0]] = swap(height[wrong_coords['even'][0]], height[wrong_coords['odd'][0]])
        return height 


def swap(a, b):
    return b, a

print(solution(height))