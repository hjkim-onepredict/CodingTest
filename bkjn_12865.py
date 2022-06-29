import sys

# 표준 입력을 파일로 설정하기 -> input.txt를 읽어들여옴
sys.stdin = open("input", "r") 

# 표준 입력을 파일로 바꿨으므로, 
# input() 함수는 더이상 사용자 입력을 받지 않고, 지정된 입력 파일을 읽게 됨.
n, k = map(int, sys.stdin.readline().split())
arr_wv = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 1. 가능한 조합의 무게와 가치합 도출
# 2. 무게가 k를 초과하면 버림
# 3. 버리지 않는 경우 해당 가치합과 직전 가치합을 비교, 직전 가치합보다 높으면 저장

from itertools import combinations
sum_v_final = 0
for n_comb in range(n):
    # print(n_comb+1)
    combs = list(combinations(range(n),n_comb+1))
    for idx_comb in combs:
        sum_w = 0
        sum_v = 0
        for i in idx_comb:
            sum_w += arr_wv[i][0]
            sum_v += arr_wv[i][1]
        print(sum_w, sum_v)
        if (sum_w<=k) & (sum_v > sum_v_final):
            sum_v_final = sum_v
print(sum_v_final)