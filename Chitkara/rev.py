set=input("Enter a sentence")
set=set+" "
temp=" "
rev=" "
for i in set:
    if i!=" ":
        temp=i+temp
    else:
        rev=rev+" "+temp
        temp=" "
print(rev)