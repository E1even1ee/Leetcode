# Write a function that takes a string as input and returns the string reversed.

# Example:
# Given s = "hello", return "olleh".
class Solution(object):
    def reverseString(self, s):
        f = list(s)
        index = len(s) - 1
        new = 0
        while(index >= 0):
            f[new] = s[index]
            index -= 1
            new += 1
        f = "".join(f)
        return f