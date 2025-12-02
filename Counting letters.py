name = input("Enter your fullname: ")
name = name.lower()
name = name.replace(" ", "")
b=[]
for n in name:
    if n not in b:
        print(f"your name had {name.count(n)} {n}")
        b.append(n)