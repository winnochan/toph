#!/usr/bin/env python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a, b = map(int, input().strip().split())

    if a % 2 == 1:
        print((b - a) // 2 + 1)
    else:
        print((b - a + 1) // 2)
