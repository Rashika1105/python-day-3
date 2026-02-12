n = int(input("Enter your age: "))
if n >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    if n >= 13:
        print("You are a teenager.")
    else:
        print("You are a child.")
        