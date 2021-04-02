def reverse(s):
    if len(s) <= 1:
        return s
    return s[-1]+reverse(s[:-1])

def isPalindrome(s):
    'return True iff s is a palindrome'
    "your code here"
    
    return reverse(s) == s

print(reverse("hallo"))
print(isPalindrome("rentner"))
