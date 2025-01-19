import sys

K, N = map(int, sys.stdin.readline().split())
lans = []

for _ in range (K):
    lans.append(int(sys.stdin.readline()))
    
start = 1
end = max(lans)

while start <= end:
    sum_lans = 0
    middle = (start + end) // 2
    
    for lan in lans:
        sum_lans += lan // middle
    
    if sum_lans >= N:
        start = middle + 1
    else:
        end = middle - 1
        
print(end)