s1 = input()
s2 = input()
print('Yes' if len(set(s1) & set(s2)) == len(s1) else 'No')
