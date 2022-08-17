import sys

sys.stdin = open("_파리 퇴치.txt")

list_ = [
    [1, 3, 3, 6, 7],
    [8, 13, 9, 12, 8],
    [4, 16, 11, 12, 6],
    [2, 4, 1, 23, 2],
    [9, 13, 4, 7, 3],
]
N = 5
M = 2
최대영역합 = 0 

# 이중 리스트를 순회하는 이중 반복문
for 기준행 in range(N - M + 1):
    for 기준열 in range(N - M + 1):
        
        # 각 기준 좌표에서의 영역의 합 계산
        영역합 = 0
        for 행 in range(기준행, 기준행 + M):
            for 열 in range(기준열, 기준열 + M):
                영역합 += list_[행][열]

        # print(기준행,기준열,영역합)
        if 영역합 > 최대영역합:
            최대영역합 = 영역합 

print(최대영역합)
