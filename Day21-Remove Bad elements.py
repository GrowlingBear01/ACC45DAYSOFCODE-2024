import collections

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    count = collections.Counter(a)
    for _, j in count.most_common(1):
        max_count = j
    print(n - max_count)
