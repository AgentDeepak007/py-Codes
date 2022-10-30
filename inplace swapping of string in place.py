# swap characters in string
def swap(str):
    if len(str) <= 1:
        return str
 
    mid = str[1:len(str) - 1]
    return str[len(str) - 1] + mid + str[0]
 
# take string from user
str1 = input("Please Enter String : ")
 
print (swap(str1))
