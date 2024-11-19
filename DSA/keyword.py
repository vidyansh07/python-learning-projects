#Assert 

def reverseString(n):
    assert type(n) == str, "Input should be a string"
    return n[::-1]

print(reverseString(12))

