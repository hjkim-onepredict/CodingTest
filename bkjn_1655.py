import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("input", "r") 

n = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(n)]

print(arr)

for i in range(n):
    flag_find = False
    arr_current = arr[:i+1]
    # print(sorted(arr_current))
    # print(list(set(arr_current)))
    for number in arr_current:
        n_lt = sum([number>x for x in arr_current])
        n_gt = sum([number<x for x in arr_current])
        # print(number, n_lt, n_gt)
        if (n_lt == n_gt) | (n_lt+1 == n_gt):
            # print(number, n_lt, n_gt)
            print(number)
            flag_find = True
            break
    if flag_find == False:
        for number in arr_current:
            n_lt = sum([number>x for x in arr_current])
            n_gt = sum([number<x for x in arr_current])
            # print(number, n_lt, n_gt)
            if (n_lt == n_gt+1):
                # print(number, n_lt, n_gt)
                print(number)
                flag_find = True
                break
