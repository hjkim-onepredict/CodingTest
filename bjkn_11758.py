import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("input", "r") 

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

print(arr)

if arr[1][0] == arr[1][1]:
    # a0 = 


# 답을 찾아보니 외적이라고 한다.