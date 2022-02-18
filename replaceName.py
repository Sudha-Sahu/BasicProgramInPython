# Replace string template with Any Name

print('Hello <<name>>, How are you?')
name = input("Enter your name : ")
if len(name) >= 3:
    print('Hello ', name, ', How are you?')
else:
    print("invalid inputs")
