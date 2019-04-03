def C(P, K, B, T=(-1, )):
    if K == 0:
        return 1 if B == 0 else 0

    return sum(
        (C(P, K - 1, B - P[i], T + (i, )) for i in range(T[-1] + 1, len(P))))


T = int(input())

for i in range(T):
    N = int(input())
    K = int(input())
    B = int(input())
    P = list(map(int, input().strip().split()))
    print('Case %d: %d' % (i + 1, C(P, K, B)))
