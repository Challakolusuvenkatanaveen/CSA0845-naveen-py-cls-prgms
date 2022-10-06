def ispalindrome(m):
    rev=''.join(reversed(m))
    if(rev==m):
        return True
    return False
m=input("x=")
l=ispalindrome(m)
if(l):
    print("true")
else:
    print("false")
