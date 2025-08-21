s=input("Enter").lower()
for i in s:
    if not i.isalnum():
        s.replace(i,"")
if s==s[::-1]:
    print("true")
else:
    print("false")