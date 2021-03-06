n = int(input())
pup = [int(input()) for _ in range(n)]


def solution(arr):
    flag = 0
    coords = []
    if arr[-1] == 1:
        for i in range(len(arr) - 1):
            if flag == 0: 
                if arr[i + 1] != arr[i] + 1:
                    arr[i + 1] = arr[i] + 1
                    flag = 1
                    coords += [i + 1, arr[i] + 1]
            elif arr[i + 1] != arr[i] + 1:
                return [-1, -1]
        return coords
    else: return [-1, -1]
    # else: 
    #     for i in range(len(arr) - 1):
    #         if arr[i + 1] != arr[i] + 1:
    #             return[-1, -1]
    #     arr[-1] = 1
    # return [len(arr)-1, 1] 


print(solution(pup))
print(pup)