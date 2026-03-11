class Solution:
    def isScramble(self, s1, s2):
        memo = {}

        def check(a, b):
            if (a, b) in memo:
                return memo[(a, b)]

            if a == b:
                return True

            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):
                if check(a[:i], b[:i]) and check(a[i:], b[i:]):
                    memo[(a, b)] = True
                    return True

                if check(a[:i], b[n-i:]) and check(a[i:], b[:n-i]):
                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return check(s1, s2)