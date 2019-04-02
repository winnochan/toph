#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    while True:
        try:
            n, m = map(int, input().strip().split())
            n, m = min(n, m), max(n, m)
            s = (n + m) * (m - n + 1) // 2
            print('Sum of {0} to {1} is -> {2};'.format(n, m, s))
        except EOFError:
            break
