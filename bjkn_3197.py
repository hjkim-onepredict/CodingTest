import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("input", "r") 

# 표준 입력을 파일로 바꿨으므로, 
# input() 함수는 더이상 사용자 입력을 받지 않고, 지정된 입력 파일을 읽게 됨.
n, k = map(int, sys.stdin.readline().split())
arr_wv = [sys.stdin.readline().split() for _ in range(n)]

# 1. 백조들의 위치를 찾는다.
# 2. 백조 두마리가 꼭지점이 되는 직사각형 내 연결된 점선 탐색
# 3. 얼음을 녹인다.
loc_swan1 = [0, 0]
loc_swan2 = [0, 0]
for arr in arr_wv:
    print(arr)

for i, arr in enumerate(arr_wv):
    j_l = arr[0].find('L')
    j_r = arr[0].rfind('L')
    if j_l != -1:
        if j_l == j_r:
            if loc_swan1 == [0,0]:
                loc_swan1 = [i, j_l]
            else:
                loc_swan2 = [i, j_l]
        else:
            loc_swan1 = [i, j_l]
            loc_swan2 = [i, j_r]
    
print(loc_swan1)
print(loc_swan2)

# Swan1이 Swan2로 가는 길을 탐색한다.
# 1. 일단 오른쪽으로 이동 시도
# 2. 막혀있음.

# 포기...
