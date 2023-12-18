def recursion(s, l, r, count) :
    count += 1
    if l >= r :
        return 1, count
    elif s[l] != s[r] :
        return 0, count
    else :
        return recursion(s, l+1, r-1, count)

def isPalindrome(s) :
    return recursion(s, 0, len(s)-1, 0)

import sys
n = int(sys.stdin.readline())

for _ in range(n) :
    count = 0
    result = isPalindrome(sys.stdin.readline().rstrip())
    print(result[0], result[1])