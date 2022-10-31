def Convert(old):
    l=len(old)
    New=""
    for i in range(0,5):
        if old[i].isupper():
            New=New+old[i].lower()
        elif old[i].islower():
            New=New+old[i].upper()
        elif old[i].isdigit():
            New=New+"'"
    return New

older="InDIa@2020"
Newer=Convert(older)
print("New string is : ",Newer)
        
